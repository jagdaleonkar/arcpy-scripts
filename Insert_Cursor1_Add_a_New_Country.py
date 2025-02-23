import arcpy

countries = r'C:\GIS ArcMap\Data\ne_10m_admin_0_countries.shp'

with arcpy.da.InsertCursor(countries,["Name", "Shape", "LABELRANK", "LEVEL"]) as cursor:

    cursor.insertRow(["Kalamboli", "Polygon", 1, 1])