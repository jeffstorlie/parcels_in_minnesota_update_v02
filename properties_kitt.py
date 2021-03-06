from parcels_base_classes import countyEtlParams

class countyEtl(countyEtlParams):

    '''Class per county with unique parameters defined.'''
    def __init__(self):
        self.county_name = 'Kittson'
        self.cty_fips = r'69'
        self.county_id = r'069'
        self.cty_abbr = r'KITT'
        self.mngeo_web_id = r'Kittson 069'
        self.sourceZipFile = r'KITT_parcels.zip'
        self.sourcePolygons = r'Parcels.shp'
        self.sourceOwnershipZipFile = r''
        self.sourceOwnershipTable = r''
        self.joinInField = r''
        self.joinJoinField = r''
        self.PIN_exists.fieldTransferList = ['Parcel_Num']
        self.BLDG_NUM_exists.fieldTransferList = []
        self.BLDG_NUM_exists.transferType = ''
        self.PREFIX_DIR_exists.fieldTransferList = []
        self.PREFIX_DIR_exists.transferType = ''
        self.PREFIXTYPE_exists.fieldTransferList = []
        self.PREFIXTYPE_exists.transferType = ''
        self.STREETNAME_exists.fieldTransferList = []
        self.STREETNAME_exists.transferType = ''
        self.STREETTYPE_exists.fieldTransferList = []
        self.STREETTYPE_exists.transferType = ''
        self.SUFFIX_DIR_exists.fieldTransferList = []
        self.SUFFIX_DIR_exists.transferType = ''
        self.UNIT_INFO_exists.fieldTransferList = []
        self.UNIT_INFO_exists.transferType = ''
        self.CITY_exists.fieldTransferList = []
        self.CITY_exists.transferType = ''
        self.CITY_USPS_exists.fieldTransferList = []
        self.CITY_USPS_exists.transferType = ''
        self.ZIP_exists.fieldTransferList = []
        self.ZIP_exists.transferType = ''
        self.ZIP4_exists.fieldTransferList = []
        self.ZIP4_exists.transferType = ''
        self.PLAT_NAME_exists.fieldTransferList = ['SUBDIVISIO']
        self.PLAT_NAME_exists.transferType = ''
        self.BLOCK_exists.fieldTransferList = ['BLOCK']
        self.BLOCK_exists.transferType = ''
        self.LOT_exists.fieldTransferList = ['LOT']
        self.LOT_exists.transferType = ''
        self.ACRES_POLY_exists.fieldTransferList = ['ACRES']
        self.ACRES_DEED_exists.fieldTransferList = []
        self.USE1_DESC_exists.fieldTransferList = []
        self.USE1_DESC_exists.transferType = ''
        self.USE2_DESC_exists.fieldTransferList = []
        self.USE2_DESC_exists.transferType = ''
        self.USE3_DESC_exists.fieldTransferList = []
        self.USE3_DESC_exists.transferType = ''
        self.USE4_DESC_exists.fieldTransferList = []
        self.USE4_DESC_exists.transferType = ''
        self.MULTI_USES_exists.fieldTransferList = []
        self.MULTI_USES_exists.transferType = ''
        self.LANDMARK_exists.fieldTransferList = []
        self.LANDMARK_exists.transferType = ''
        self.OWNER_NAME_exists.fieldTransferList = []
        self.OWNER_NAME_exists.transferType = ''
        self.OWNER_MORE_exists.fieldTransferList = []
        self.OWNER_MORE_exists.transferType = ''
        self.OWN_ADD_L1_exists.fieldTransferList = ['PROPERTY_A']
        self.OWN_ADD_L1_exists.transferType = ''
        self.OWN_ADD_L2_exists.fieldTransferList = ['PROPERTY_1']
        self.OWN_ADD_L2_exists.transferType = ''
        self.OWN_ADD_L3_exists.fieldTransferList = ['PROPERTY_2']
        self.OWN_ADD_L3_exists.transferType = ''
        self.OWN_ADD_L4_exists.fieldTransferList = ['PROPERTY_C', 'PROPERTY_S', 'PROPERTY_Z']
        self.OWN_ADD_L4_exists.transferType = 'concatTruncateLastAddrLine'
        self.TAX_NAME_exists.fieldTransferList = ['TAXPAYER_N']
        self.TAX_NAME_exists.transferType = ''
        self.TAX_ADD_L1_exists.fieldTransferList = ['TAXPAYER_A']
        self.TAX_ADD_L1_exists.transferType = ''
        self.TAX_ADD_L2_exists.fieldTransferList = ['TAXPAYER_2']
        self.TAX_ADD_L2_exists.transferType = ''
        self.TAX_ADD_L3_exists.fieldTransferList = ['TAXPAYER_3']
        self.TAX_ADD_L3_exists.transferType = ''
        self.TAX_ADD_L4_exists.fieldTransferList = ['TAXPAYER_C', 'TAXPAYER_S', 'TAXPAYER_Z']
        self.TAX_ADD_L4_exists.transferType = 'concatTruncateLastAddrLine'
        self.OWNERSHIP_exists.fieldTransferList = []
        self.OWNERSHIP_exists.transferType = ''
        self.HOMESTEAD_exists.fieldTransferList = []
        self.HOMESTEAD_exists.transferType = ''
        self.TAX_YEAR_exists.fieldTransferList = ['TAX_YEAR']
        self.MARKET_YEAR_exists.fieldTransferList = []
        self.EMV_LAND_exists.fieldTransferList = []
        self.EMV_BLDG_exists.fieldTransferList = []
        self.EMV_TOTAL_exists.fieldTransferList = []
        self.TAX_CAPAC_exists.fieldTransferList = []
        self.TOTAL_TAX_exists.fieldTransferList = []
        self.SPEC_ASSES_exists.fieldTransferList = []
        self.TAX_EXEMPT_exists.fieldTransferList = []
        self.TAX_EXEMPT_exists.transferType = ''
        self.XUSE1_DESC_exists.fieldTransferList = []
        self.XUSE1_DESC_exists.transferType = ''
        self.XUSE2_DESC_exists.fieldTransferList = []
        self.XUSE2_DESC_exists.transferType = ''
        self.XUSE3_DESC_exists.fieldTransferList = []
        self.XUSE3_DESC_exists.transferType = ''
        self.XUSE4_DESC_exists.fieldTransferList = []
        self.XUSE4_DESC_exists.transferType = ''
        self.DWELL_TYPE_exists.fieldTransferList = []
        self.DWELL_TYPE_exists.transferType = ''
        self.HOME_STYLE_exists.fieldTransferList = []
        self.HOME_STYLE_exists.transferType = ''
        self.FIN_SQ_FT_exists.fieldTransferList = []
        self.GARAGE_exists.fieldTransferList = []
        self.GARAGE_exists.transferType = ''
        self.GARAGESQFT_exists.fieldTransferList = []
        self.BASEMENT_exists.fieldTransferList = []
        self.BASEMENT_exists.transferType = ''
        self.HEATING_exists.fieldTransferList = []
        self.HEATING_exists.transferType = ''
        self.COOLING_exists.fieldTransferList = []
        self.COOLING_exists.transferType = ''
        self.YEAR_BUILT_exists.fieldTransferList = []
        self.NUM_UNITS_exists.fieldTransferList = []
        self.SALE_DATE_exists.fieldTransferList = []
        self.SALE_DATE_exists.transferType = 'Date'
        self.SALE_VALUE_exists.fieldTransferList = []
        self.SCHOOL_DST_exists.fieldTransferList = ['SCHOOL_DIS']
        self.SCHOOL_DST_exists.transferType = ''
        self.WSHD_DIST_exists.fieldTransferList = ['WATERSHED_']
        self.WSHD_DIST_exists.transferType = ''
        self.GREEN_ACRE_exists.fieldTransferList = []
        self.GREEN_ACRE_exists.transferType = ''
        self.OPEN_SPACE_exists.fieldTransferList = []
        self.OPEN_SPACE_exists.transferType = ''
        self.AG_PRESERV_exists.fieldTransferList = []
        self.AG_PRESERV_exists.transferType = ''
        self.AGPRE_ENRD_exists.fieldTransferList = []
        self.AGPRE_ENRD_exists.transferType = 'Date'
        self.AGPRE_EXPD_exists.fieldTransferList = []
        self.AGPRE_EXPD_exists.transferType = 'Date'
        self.PARC_CODE_exists.fieldTransferList = []
        self.SECTION_exists.fieldTransferList = ['SECTION_']
        self.TOWNSHIP_exists.fieldTransferList = ['TOWNSHIP']
        self.RANGE_exists.fieldTransferList = ['RANGE']
        self.RANGE_DIR_exists.fieldTransferList = []
        self.LEGAL_DESC_exists.fieldTransferList = ['LEGAL_DESC']
        self.LEGAL_DESC_exists.transferType = ''
        self.EDIT_DATE_exists.fieldTransferList = []
        self.EDIT_DATE_exists.transferType = 'Date'
        self.EXPORT_DATE_exists.fieldTransferList = []
        self.EXPORT_DATE_exists.transferType = 'Date'
        self.ORIG_PIN_exists.fieldTransferList = ['Parcel_Num']
        self.ORIG_PIN_exists.transferType = ''

    def returnCountyBase(self):
        return county_name
