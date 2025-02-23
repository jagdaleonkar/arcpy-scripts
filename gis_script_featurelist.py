import arcpy
arcpy.env.workspace = r'C:\GIS ArcMap\Data'
feature_list = arcpy.ListFeatureClasses()
print(feature_list)