import os
from django.contrib.gis.db import models
from django.contrib.gis.utils import LayerMapping
from django.core.exceptions import ValidationError
from django.contrib.contenttypes.models import ContentType
from django.utils.simplejson import dumps
from django.conf import settings
from madrona.features.models import PolygonFeature, FeatureCollection
from madrona.features import register, alternate
from madrona.async.ProcessHandler import check_status_or_begin, get_process_status
from madrona.raster_stats.models import RasterDataset

@register
class Stand(PolygonFeature):
    RX_CHOICES = (
        ('--', '--'),
        ('CC', 'Clearcut'),
        ('SW', 'Shelterwood'),
    )
    SPP_CHOICES = (
        ('--', '--'),
        ('DF', 'Douglas Fir'),
        ('MH', 'Mountain Hemlock'),
    )
    rx = models.CharField(max_length=2, choices=RX_CHOICES, 
            verbose_name="Presciption", default="--")
    domspp = models.CharField(max_length=2, choices=SPP_CHOICES, 
            verbose_name="Dominant Species", default="--")

    class Options:
        form = "trees.forms.StandForm"
        manipulators = []
        links = (
            # Link to grab property geojson 
            alternate('GeoJSON',
                'trees.views.geojson_features',  
                type="application/json",
                select='multiple single'),
        )

    @property
    def geojson(self):
        '''
        Couldn't find any serialization methods flexible enough for our needs
        So we do it the hard way.
        '''
        d = {
                'uid': self.uid,
                'name': self.name,
                'rx': self.rx,
                'domspp': self.domspp,
                'elevation': self.imputed_elevation,
                'aspect': self.imputed_aspect,
                'gnn': self.imputed_gnn,
                'slope': self.imputed_slope,
                'user_id': self.user.pk,
                'date_modified': str(self.date_modified),
                'date_created': str(self.date_created),
            }
        gj = """{ 
              "type": "Feature",
              "geometry": %s,
              "properties": %s 
        }""" % (self.geometry_final.json, dumps(d))
        return gj

    @property
    def imputed_elevation(self):
        try:
            raster = RasterDataset.objects.get(name="elevation")
            imputed_data = ImputedData.objects.get(raster=raster,feature=self)
            result = imputed_data.val  
        except (ImputedData.DoesNotExist, RasterDataset.DoesNotExist):
            result = None
        return result

    @property
    def imputed_aspect(self):
        import math
        try:
            cos_raster = RasterDataset.objects.get(name="cos_aspect")
            cos_sum = ImputedData.objects.get(raster=cos_raster,feature=self)

            sin_raster = RasterDataset.objects.get(name="sin_aspect")
            sin_sum = ImputedData.objects.get(raster=sin_raster,feature=self)

            avg_aspect_rad = math.atan2(cos_sum.val, sin_sum.val)
            result = math.degrees(avg_aspect_rad)
        except (ImputedData.DoesNotExist, RasterDataset.DoesNotExist):
            result = None
        return result

    @property
    def imputed_slope(self):
        try:
            raster = RasterDataset.objects.get(name="slope")
            imputed_data = ImputedData.objects.get(raster=raster,feature=self)
            result = imputed_data.val  
        except (ImputedData.DoesNotExist, RasterDataset.DoesNotExist):
            result = None
        return result

    @property
    def imputed_gnn(self):
        try:
            raster = RasterDataset.objects.get(name="gnn")
            imputed_data = ImputedData.objects.get(raster=raster,feature=self)
            result = imputed_data.val  
        except (ImputedData.DoesNotExist, RasterDataset.DoesNotExist):
            result = None
        return result


    @property
    def imputed(self):
        return {'aspect': self.imputed_aspect, 
                'elevation': self.imputed_elevation, 
                'slope': self.imputed_slope,
                'gnn': self.imputed_gnn,
               }
    @property
    def status(self):
        status = {}
        for raster in self.imputed.keys():
            name = "imputed_%s" % raster
            url = "%s%s" % (self.get_absolute_url(), name)
            async_status = get_process_status(polling_url=url)
            if self.imputed[raster] is not None:
                status[raster] = "COMPLETED"
            elif async_status is not None:
                # STARTED, PENDING, SUCCESS, FAILURE, RETRY, REVOKED
                # custom: RASTERNOTFOUND, ZONALNULL
                status[raster] = async_status
            else:
                status[raster] = "NOTSTARTED"
        return status

    def _impute(self, force=False, limit_to=None):
        '''
        limit_to: list of rasters to (re)impute
        force: if True, bypass the zonal_stats cache
        '''
        from trees.tasks import impute
        for raster in settings.IMPUTE_RASTERS:
            if limit_to and raster[0] not in limit_to:
                continue
            name = "imputed_%s" % raster[0]
            url = "%s%s" % (self.get_absolute_url(), name)

            status, task_id = check_status_or_begin(impute, 
                    task_args=(self.uid,raster[0],raster[1],force), 
                    polling_url=url)

    def save(self, *args, **kwargs):
        """
        stand.save(impute=True, force=False) <- default; impute only if update is needed
        stand.save(impute=True, force=True) <- will force redo of all imputations
        stand.save(impute=False) <- don't trigger async impute routines, just save the model
        """
        impute = kwargs.pop('impute', True)
        force = kwargs.pop('force', False)

        if self.pk:
            # modifying an existing feature
            orig = Stand.objects.get(pk=self.pk)
            geom_fields = [f for f in Stand._meta.fields if f.attname.startswith('geometry_')]
            same_geom = True  # assume geometries have NOT changed
            for f in geom_fields:
                # Is original value different from form value?
                if orig._get_FIELD_display(f) != self._get_FIELD_display(f):
                    same_geom = False

            all_imputes_done = None not in self.imputed.values()

            # If geom is the same and all imputed fields are completed, don't reimpute unless force=True 
            if same_geom and all_imputes_done and not force:
                impute = False

        super(Stand, self).save(*args, **kwargs)

        if impute:
            self._impute(force=force)

    @property
    def complete(self):
        if self.rx == '--':
            return False
        if self.domspp == '--':
            return False
        return True

class ImputedData(models.Model):
    raster = models.ForeignKey(RasterDataset)
    feature = models.ForeignKey(Stand)
    val = models.FloatField(null=True, blank=True)

@register
class ForestProperty(FeatureCollection):
    geometry_final = models.PolygonField(srid=settings.GEOMETRY_DB_SRID, 
            null=True, blank=True, verbose_name="Stand Polygon Geometry")

    @property
    def geojson(self):
        '''
        Couldn't find any serialization methods flexible enough for our needs
        So we do it the hard way.
        '''
        d = {
                'uid': self.uid,
                'name': self.name,
                'user_id': self.user.pk,
                'bbox': self.bbox,
                'date_modified': str(self.date_modified),
                'date_created': str(self.date_created),
            }
        try:
            geom_json = self.geometry_final.json
        except AttributeError:
            geom_json = 'null'

        gj = """{ 
              "type": "Feature",
              "geometry": %s,
              "properties": %s 
        }""" % (geom_json, dumps(d))
        return gj

    def feature_set_geojson(self):
        featxt = ', '.join([i.geojson for i in self.feature_set()])
        return """{ "type": "FeatureCollection",
        "features": [
        %s
        ]}""" % featxt

    @property
    def bbox(self):
        try:
            return self.geometry_final.extent
        except AttributeError:
            return settings.DEFAULT_EXTENT

    @property
    def file_dir(self):
        '''
        Standard property for determining where supporting files reside
        /feature_file_root/database_name/feature_uid/
        '''
        root = settings.FEATURE_FILE_ROOT
        try:
            dbname = settings.DATABASES['default']['NAME']
        except:
            dbname = settings.DATABASE_NAME

        path = os.path.realpath(os.path.join(root, dbname, self.uid))
        if not os.path.exists(path):
            os.makedirs(path)

        if not os.access(path, os.W_OK):
            raise Exception("Feature file_dir %s is not writeable" % path)

        return path


    def adjacency(self, threshold=1.0):
        from trees.utils import calculate_adjacency
        stands = Stand.objects.filter(
            content_type=ContentType.objects.get_for_model(self),
            object_id=self.pk
        )
        return calculate_adjacency(stands, threshold)


    class Options:
        valid_children = ('trees.models.Stand',)
        form = "trees.forms.PropertyForm"
        links = (
            # Link to grab ALL *stands* associated with a property
            alternate('Property Stands GeoJSON',
                'trees.views.geojson_forestproperty',  
                type="application/json",
                select='single'),
            # Link to grab property geojson 
            alternate('GeoJSON',
                'trees.views.geojson_features',  
                type="application/json",
                select='multiple single'),
        )

class Parcel(models.Model):
    apn = models.CharField(max_length=40)
    geom = models.MultiPolygonField(srid=3857)
    objects = models.GeoManager()

class StreamBuffer(models.Model):
    area = models.FloatField()
    perimeter = models.FloatField()
    str_buf_field = models.IntegerField()
    str_buf_id = models.IntegerField()
    inside = models.IntegerField()
    geom = models.MultiPolygonField(srid=3857)
    objects = models.GeoManager()

stand_mapping = {
    'name': 'STAND_TEXT',
    'geometry_final': 'POLYGON',
    'geometry_original': 'POLYGON'
}

# Auto-generated `LayerMapping` dictionary for Parcel model
parcel_mapping = {
    'apn' : 'APN',
    'geom' : 'MULTIPOLYGON',
}

# Auto-generated `LayerMapping` dictionary for StreamBuffer model
streambuffer_mapping = {
    'area' : 'AREA',
    'perimeter' : 'PERIMETER',
    'str_buf_field' : 'STR_BUF_',
    'str_buf_id' : 'STR_BUF_ID',
    'inside' : 'INSIDE',
    'geom' : 'MULTIPOLYGON',
}

def run():
    verbose = True

    parcel_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../data/landowner_demo/merc/Parcels.shp'))
    for p in Parcel.objects.all():
        p.delete()
    map1 = LayerMapping(Parcel, parcel_shp, parcel_mapping, transform=False, encoding='iso-8859-1')
    map1.save(strict=True, verbose=verbose)

    streambuffer_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../data/landowner_demo/merc/stream_buffer_clip.shp'))
    for sb in StreamBuffer.objects.all():
        sb.delete()
    map2 = LayerMapping(StreamBuffer, streambuffer_shp, streambuffer_mapping, transform=False, encoding='iso-8859-1')
    map2.save(strict=True, verbose=verbose)

def import_stands():
    stands_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../data/sixes/sixes_stands_3857b.shp'))
    for s in Stand.objects.all():
        s.delete()
    map1 = LayerMapping(Stand, stands_shp, stand_mapping, transform=False, encoding='iso-8859-1')
    map1.save(strict=True, verbose=True)

