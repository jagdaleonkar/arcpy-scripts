import arcpy

countries = r'C:\ArcPy\Data\ne_10m_admin_0_countries.shp'

field_name = "SOVEREIGNT"

with arcpy.da.UpdateCursor(countries, [field_name]) as cursor:
    for row in cursor:
        # Update the country name to uppercase
        row[0] = row[0].upper()
        cursor.updateRow(row)

print("Country names updated to uppercase.")
