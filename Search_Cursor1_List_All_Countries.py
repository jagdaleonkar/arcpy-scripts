import arcpy 

points = r'C:\GIS ArcMap\Data\ne_10m_populated_places.shp'
countries = r'C:\GIS ArcMap\Data\ne_10m_admin_0_countries.shp'
outpath = r'C:\GIS ArcMap\outputs'

field = ['NAME']

with arcpy.da.SearchCursor(countries, field) as countries_cursor:
    for row in countries_cursor:
	    print(f'{row[0]}')