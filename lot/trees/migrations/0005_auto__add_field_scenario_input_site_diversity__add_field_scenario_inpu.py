# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Scenario.input_site_diversity'
        db.add_column('trees_scenario', 'input_site_diversity', self.gf('django.db.models.fields.FloatField')(default=0), keep_default=False)

        # Adding field 'Scenario.input_age_class'
        db.add_column('trees_scenario', 'input_age_class', self.gf('django.db.models.fields.FloatField')(default=0), keep_default=False)

        # Changing field 'Scenario.input_target_carbon'
        # vvv this doesn't work due to typecasting error
        # db.alter_column('trees_scenario', 'input_target_carbon', self.gf('django.db.models.fields.BooleanField')())
        # instead we delete and re-add the column as a boolean
        db.delete_column('trees_scenario', 'input_target_carbon')
        db.add_column('trees_scenario', 'input_target_carbon', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True))


    def backwards(self, orm):
        
        # Deleting field 'Scenario.input_site_diversity'
        db.delete_column('trees_scenario', 'input_site_diversity')

        # Deleting field 'Scenario.input_age_class'
        db.delete_column('trees_scenario', 'input_age_class')

        # Changing field 'Scenario.input_target_carbon'
        db.alter_column('trees_scenario', 'input_target_carbon', self.gf('django.db.models.fields.FloatField')())


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 9, 17, 10, 52, 18, 669488)'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 9, 17, 10, 52, 18, 669358)'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'trees.county': {
            'Meta': {'object_name': 'County'},
            'cnty_fips': ('django.db.models.fields.IntegerField', [], {}),
            'cntyname': ('django.db.models.fields.CharField', [], {'max_length': '23'}),
            'fips': ('django.db.models.fields.IntegerField', [], {}),
            'geom': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'srid': '3857'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'polytype': ('django.db.models.fields.IntegerField', [], {}),
            'soc_cnty': ('django.db.models.fields.IntegerField', [], {}),
            'st_fips': ('django.db.models.fields.IntegerField', [], {}),
            'stname': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        'trees.forestproperty': {
            'Meta': {'object_name': 'ForestProperty'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'trees_forestproperty_related'", 'null': 'True', 'to': "orm['contenttypes.ContentType']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'geometry_final': ('django.contrib.gis.db.models.fields.PolygonField', [], {'srid': '3857'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'255'"}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sharing_groups': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'trees_forestproperty_related'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['auth.Group']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'trees_forestproperty_related'", 'to': "orm['auth.User']"})
        },
        'trees.fvsspecies': {
            'AK': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'BM': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'CA': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'CI': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'CR': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'EC': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'EM': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'IE': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'KT': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'Meta': {'object_name': 'FVSSpecies'},
            'NC': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'NI': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'PN': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'SO': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'TT': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'UT': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'WC': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'WS': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'common': ('django.db.models.fields.TextField', [], {}),
            'fia': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'fvs': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'scientific': ('django.db.models.fields.TextField', [], {}),
            'usda': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'})
        },
        'trees.fvsvariant': {
            'Meta': {'object_name': 'FVSVariant'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'fvsvariant': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'geom': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'srid': '3857'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'trees.gnn_orwa': {
            'Meta': {'object_name': 'GNN_ORWA'},
            'count': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'value': ('django.db.models.fields.IntegerField', [], {})
        },
        'trees.parcel': {
            'Meta': {'object_name': 'Parcel'},
            'apn': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'geom': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'srid': '3857'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'trees.plotsummary': {
            'Meta': {'object_name': 'PlotSummary', 'db_table': "u'sppsz_attr_all'"},
            'age_dom': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'age_dom_no_rem': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'assessment_year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'baa_25_50': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'baa_3_25': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'baa_50_75': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'baa_75_100': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'baa_ge_100': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'baa_ge_3': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'bac_25_50': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'bac_3_25': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'bac_50_75': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'bac_75_100': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'bac_ge_100': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'bac_ge_3': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'bac_prop': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'bah_25_50': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'bah_3_25': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'bah_50_75': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'bah_75_100': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'bah_ge_100': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'bah_ge_3': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'bah_prop': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'bph_ge_3': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'cancov': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'cancov_con': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'cancov_dom': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'cancov_hdw': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'cnty': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'conplba': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'conplcov': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'conpliv': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'conr': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'covcl': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'data_source': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'dcov_12_25': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dcov_25_50': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dcov_50_75': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dcov_75_100': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dcov_ge_100': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dcov_ge_12': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dcov_ge_25': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dcov_ge_50': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dcov_ge_75': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'ddi': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dvph_12_25': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dvph_25_50': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dvph_50_75': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dvph_75_100': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dvph_ge_100': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dvph_ge_12': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dvph_ge_25': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dvph_ge_50': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dvph_ge_75': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'eslf_code': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'eslf_name': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'fcid': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'}),
            'fortypba': ('django.db.models.fields.CharField', [], {'max_length': '42', 'null': 'True', 'blank': 'True'}),
            'fortypcov': ('django.db.models.fields.CharField', [], {'max_length': '42', 'null': 'True', 'blank': 'True'}),
            'fortypiv': ('django.db.models.fields.CharField', [], {'max_length': '42', 'null': 'True', 'blank': 'True'}),
            'half_state': ('django.db.models.fields.CharField', [], {'max_length': '6', 'null': 'True', 'blank': 'True'}),
            'hcb': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'hdwplba': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'hdwplcov': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'hdwpliv': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'hdwr': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'idb_plot_id': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'imap_domspp': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'imap_layers': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'imap_qmd': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'iv_100': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'iv_con': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'iv_hdw': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'iv_vs': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'lsog': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'lsog_tphc_50': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'map_source': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'mndbhba_all': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'mndbhba_con': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'mndbhba_hdw': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'occasion_num': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ogsi': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'plot': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'qmda_dom': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'qmda_ge_3': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'qmdc_75pct': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'qmdc_dom': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'qmdc_ge_3': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'qmdh_dom': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'qmdh_ge_3': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'rem_pctd': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'rem_pctl': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'rem_pcts': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'sbph_5_9_in': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'sbph_9_20_in': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'sbph_ge_12': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'sbph_ge_20_in': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'sc': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sc_decaid': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'sdba': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'sddbh': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'sdi': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'sdi_reineke': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'sizecl': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'stndhgt': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'stph_12_25': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'stph_25_50': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'stph_50_75': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'stph_75_100': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'stph_ge_100': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'stph_ge_12': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'stph_ge_25': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'stph_ge_50': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'stph_ge_75': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'struccond': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'struccondr': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'svph_12_25': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'svph_25_50': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'svph_50_75': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'svph_75_100': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'svph_ge_100': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'svph_ge_12': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'svph_ge_25': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'svph_ge_50': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'svph_ge_75': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'tph_25_50': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'tph_3_25': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'tph_50_75': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'tph_75_100': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'tph_ge_100': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'tph_ge_3': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'tph_reml': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'tph_rems': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'tphc_ge_100': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'tphc_ge_3': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'tphc_ge_50': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'tphc_ge_75': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'tphh_ge_3': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'tphintol_ge_3': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'tphtol_ge_3': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'treer': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'uplcov': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'value': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'vc_qmda': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'vc_qmdc': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'vegclass': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'vegclassr': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'vph_25_50': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'vph_3_25': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'vph_50_75': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'vph_75_100': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'vph_ge_100': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'vph_ge_3': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'vph_remd': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'vph_reml': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'vph_rems': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'vphc_ge_3': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'vphh_ge_3': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        'trees.scenario': {
            'Meta': {'object_name': 'Scenario'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'trees_scenario_related'", 'null': 'True', 'to': "orm['contenttypes.ContentType']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'input_age_class': ('django.db.models.fields.FloatField', [], {}),
            'input_property': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['trees.ForestProperty']"}),
            'input_rxs': ('trees.models.JSONField', [], {}),
            'input_site_diversity': ('django.db.models.fields.FloatField', [], {}),
            'input_target_boardfeet': ('django.db.models.fields.FloatField', [], {}),
            'input_target_carbon': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'255'"}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'output_scheduler_results': ('trees.models.JSONField', [], {'null': 'True', 'blank': 'True'}),
            'sharing_groups': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'trees_scenario_related'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['auth.Group']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'trees_scenario_related'", 'to': "orm['auth.User']"})
        },
        'trees.stand': {
            'Meta': {'object_name': 'Stand'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'trees_stand_related'", 'null': 'True', 'to': "orm['contenttypes.ContentType']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'domspp': ('django.db.models.fields.CharField', [], {'default': "'--'", 'max_length': '2'}),
            'geometry_final': ('django.contrib.gis.db.models.fields.PolygonField', [], {'srid': '3857', 'null': 'True', 'blank': 'True'}),
            'geometry_orig': ('django.contrib.gis.db.models.fields.PolygonField', [], {'srid': '3857', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'manipulators': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'255'"}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rx': ('django.db.models.fields.CharField', [], {'default': "'--'", 'max_length': '2'}),
            'sharing_groups': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'trees_stand_related'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['auth.Group']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'trees_stand_related'", 'to': "orm['auth.User']"})
        },
        'trees.streambuffer': {
            'Meta': {'object_name': 'StreamBuffer'},
            'area': ('django.db.models.fields.FloatField', [], {}),
            'geom': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'srid': '3857'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inside': ('django.db.models.fields.IntegerField', [], {}),
            'perimeter': ('django.db.models.fields.FloatField', [], {}),
            'str_buf_field': ('django.db.models.fields.IntegerField', [], {}),
            'str_buf_id': ('django.db.models.fields.IntegerField', [], {})
        },
        'trees.treelive': {
            'Meta': {'object_name': 'TreeLive', 'db_table': "u'tree_live'"},
            'age_bh': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'assessment_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'ba_m2': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'baph_cc': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'baph_fc': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'baph_plt': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'baph_pnt': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'biomph_cc': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'biomph_fc': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'biomph_plt': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'biomph_pnt': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'ccid': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'con': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'crown_class': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'crown_ratio': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cull_cubic': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'data_source': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'dbh_class': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dbh_cm': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dbh_est_method': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'fcid': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'for_spec': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'hcb': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'ht_est_method': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ht_m': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'iv_cc': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'iv_fc': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'iv_plt': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'iv_pnt': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'live_id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'}),
            'loc_id': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'mod_htm_fvs': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pctcov_cc': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pctcov_fc': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pctcov_plt': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pctcov_pnt': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'plot': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'plot_size': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'plot_type': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'pltid': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pnt_num': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pntid': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rem_cc': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'rem_fc': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'rem_plt': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'rem_pnt': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'scientific_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'source_db': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'source_id': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'spp_symbol': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '4', 'blank': 'True'}),
            'tph_cc': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'tph_fc': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'tph_plt': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'tph_pnt': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'tree_count': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ucc': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'vol_m3': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'volph_cc': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'volph_fc': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'volph_plt': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'volph_pnt': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['trees']
