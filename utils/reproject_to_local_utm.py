import os
import glob
import json
import geopandas as gpd

# Paths
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../data"))
JSON_PATH = os.path.join(BASE_DIR, "study_cities.json")

# Load city metadata
with open(JSON_PATH, "r", encoding="utf-8") as f:
    cities = json.load(f)

# UTM helper
def get_utm_epsg(lat, lon):
    zone = int((lon + 180) / 6) + 1
    if lat >= 0:
        return f"EPSG:326{zone:02d}"  # Northern hemisphere
    else:
        return f"EPSG:327{zone:02d}"  # Southern hemisphere


# Process cities
for city in cities:
    city_name = city["city"]
    lat = city["latitude"]
    lon = city["longitude"]
    folder_name = city["directory"]

    city_path = os.path.join(BASE_DIR, folder_name)

    if not os.path.exists(city_path):
        print(f"⚠ Folder not found: {city_path}")
        continue

    utm_epsg = get_utm_epsg(lat, lon)
    print(f"\nProcessing {city_name} → {utm_epsg}")

    shp_files = glob.glob(os.path.join(city_path, "*.shp"))

    if not shp_files:
        print("  No shapefiles found.")
        continue

    output_dir = os.path.join(city_path, "utm")
    os.makedirs(output_dir, exist_ok=True)

    for shp in shp_files:
        print(f"  Reprojecting {os.path.basename(shp)}")

        gdf = gpd.read_file(shp)

        # If CRS missing, assume WGS84
        if gdf.crs is None:
            print("    WARNING: No CRS found. Assuming EPSG:4326")
            gdf = gdf.set_crs("EPSG:4326")

        # Skip if already in correct CRS
        if gdf.crs and gdf.crs.to_string() == utm_epsg:
            print("    Already in correct UTM. Skipping.")
            continue

        gdf_utm = gdf.to_crs(utm_epsg)

        output_path = os.path.join(output_dir, os.path.basename(shp))
        gdf_utm.to_file(output_path)

    print("  Done.")

print("\nAll cities processed.")
