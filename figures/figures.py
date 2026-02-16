import json
import os
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import pandas as pd
import numpy as np

# Load cities from JSON
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../data"))
json_path = os.path.join(BASE_DIR, "study_cities.json")

with open(json_path, "r", encoding="utf-8") as f:
    cities = json.load(f)

# Convert JSON to DataFrame
df = pd.DataFrame(cities)

# Rename columns to match previous structure (optional but keeps code clean)
df = df.rename(columns={
    "city": "City",
    "country": "Country",
    "land_area_km2": "LandArea",
    "latitude": "Latitude",
    "longitude": "Longitude"
})

# Scale marker sizes
sizes = np.sqrt(df["LandArea"]) * 10

# Create figure
fig = plt.figure(figsize=(12, 7))
ax = plt.axes(projection=ccrs.Robinson())
ax.set_global()

# Add map features
ax.add_feature(cfeature.LAND, facecolor="lightgray")
ax.add_feature(cfeature.OCEAN, facecolor="white")
ax.add_feature(cfeature.BORDERS, linewidth=0.5)
ax.add_feature(cfeature.COASTLINE, linewidth=0.5)

# Plot points sized by land area
ax.scatter(
    df["Longitude"],
    df["Latitude"],
    s=sizes,
    color="steelblue",
    alpha=0.8,
    edgecolor="black",
    transform=ccrs.PlateCarree()
)

# Save figure
output_dir = os.path.dirname(__file__)

plt.savefig(os.path.join(output_dir, "figure_1.png"), dpi=450, bbox_inches="tight")
plt.savefig(os.path.join(output_dir, "figure_1.pdf"), dpi=450, bbox_inches="tight")

plt.show()
