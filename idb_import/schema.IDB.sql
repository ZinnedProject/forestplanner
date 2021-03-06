-------------------------------------------------------------
-- MDB Tools - A library for reading MS Access database files
-- Copyright (C) 2000-2004 Brian Bruns
-- Files in libmdb are licensed under LGPL and the utilities under
-- the GPL, see COPYING.LIB and COPYING files respectively.
-- Check out http://mdbtools.sourceforge.net
-------------------------------------------------------------

DROP TABLE IDB_SUMMARY;
CREATE TABLE IDB_SUMMARY
 (
	PLOT_ID			Int8, 
	COND_ID			Int8, 
	SumOfBA_FT2			Float8, 
	AvgOfBA_FT2_AC			Float8, 
	AvgOfHT_FT			Float8, 
	AvgOfTPA			Float8, 
	AvgOfDBH_IN			Float8, 
	State_name			varchar (40), 
	County_name			varchar (100), 
	Halfstate_name			varchar (100), 
	Forest_name			varchar (510), 
	ACRES			Float4, 
	ACRES_VOL			Float4, 
	FIA_FOREST_TYPE_NAME			varchar (60), 
	LATITUDE_FUZZ			Float8, 
	LONGITUDE_FUZZ			Float8, 
	ASPECT_DEG			Int4, 
	StDevOfASPECT_DEG			Float8, 
	FirstOfASPECT_DEG			Int4, 
	SLOPE			Int4, 
	StDevOfSLOPE			Float8, 
	AvgOfSLOPE			Float8, 
	ELEV_FT			Int4, 
	FVS_VARIANT			varchar (4), 
	SITE_SPECIES			Int4, 
	SITE_INDEX_FIA			Int4, 
	PLANT_ASSOC_CODE			varchar (20), 
	CountOfSUBPLOT_ID			Int8, 
	QMD_HWD_CM			Float4, 
	QMD_SWD_CM			Float4, 
	QMD_TOT_CM			Float4, 
	Calc_ASPECT			Int4, 
	Calc_SLOPE			Int4, 
	STAND_SIZE_CLASS			Int4, 
	SITE_CLASS_FIA			Int4, 
	STAND_AGE_EVEN_YN			varchar (2), 
	STAND_AGE			Int4, 
	FOR_TYPE			Int4, 
	FOR_TYPE_SECDRY			Int4, 
	FOR_TYPE_NAME			varchar (60), 
	FOR_TYPE_SECDRY_NAME			varchar (60), 
	QMDC_DOM			double precision, 
	QMDH_DOM			double precision, 
	QMDA_DOM			double precision, 
	CANCOV			double precision, 
	STNDHGT			double precision, 
	SDI			double precision, 
	SDI_REINEKE			double precision, 
	AGE_DOM			double precision, 
	VEGCLASSR			Int2, 
	VEGCLASS			Int2, 
	STRUCCONDR			Int2, 
	STRUCCOND			Int2, 
	SIZECL			Int2, 
	COVCL			Int2, 
	OGSI			double precision, 
	BAC_PROP			double precision, 
	TPH_GE_3			double precision, 
	MAI			Float4, 
	OWNER			Int4, 
	OWN_GROUP			Int4, 
	BAH_GE_3			double precision, 
	BAC_GE_3			double precision, 
	BAA_GE_3			double precision, 
	qmda_dom_stunits			double precision, 
	stndhgt_stunits			double precision, 
	baa_ge_3_stunits			double precision, 
	tph_ge_3_stunits			double precision
);
-- CREATE ANY INDEXES ...



-- CREATE ANY Relationships ...

-- relationships are not supported for postgres
