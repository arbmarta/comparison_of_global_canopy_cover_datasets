import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import pandas as pd
import numpy as np

# -----------------------------
# Create DataFrame
# -----------------------------
data = [
    ("Winnipeg", "CA", 462, 49.8954, -97.1385),
    ("Cape Town", "ZA", 2461, -33.9221, 18.4231),
    ("Virginia Beach", "US", 634, 36.8516, -75.9792),
    ("Chesapeake", "US", 909, 36.7682, -76.2875),
    ("Norfolk", "US", 250, 36.8508, -76.2859),
    ("Baltimore", "US", 238.41, 39.2905, -76.6104),
    ("London", "GB", 1572, 51.5072, -0.1276),
    ("Manchester", "GB", 116, 53.7808, -2.2426),
    ("Victoria", "CA", 19, 48.4284, -123.3656),
    ("Ottawa", "CA", 2790, 45.4201, -75.7003),
    ("Christchurch", "NZ", 1426, -43.5320, 172.6366),
    ("Wellington", "NZ", 290, -41.2924, 174.7787),
    ("Washington D.C.", "US", 68, 38.9073, -77.0369),
    ("Brussels-Capital Region", "BE", 161, 50.8260, 4.3802),
    ("Melbourne", "AU", 38, -37.8136, 144.9631),
    ("Sao Paulo", "BR", 1521, -23.5558, -46.6396),
    ("Philadelphia", "US", 367, 39.9526, -75.1652),
    ("Pittsburg", "US", 151, 40.4387, -79.9972),
    ("Harrisburg", "US", 31, 40.2732, -76.8867),
    ("Tokyo", "JP", 2194, 35.6764, 139.6500),
    ("Los Angeles", "US", 1299, 34.0549, -118.2426),
]

df = pd.DataFrame(data, columns=["City", "Country", "LandArea", "Latitude", "Longitude"])

# Normalize marker sizes for visual clarity
size_scale = 0.5
sizes = np.sqrt(df["LandArea"]) * 10  # sqrt scaling improves visual balance

# -----------------------------
# Create Figure
# -----------------------------
fig = plt.figure(figsize=(14, 7))
ax = plt.axes(projection=ccrs.Robinson())  # Good global projection for papers
ax.set_global()

# Add map features
ax.add_feature(cfeature.LAND, facecolor='lightgray')
ax.add_feature(cfeature.OCEAN, facecolor='white')
ax.add_feature(cfeature.BORDERS, linewidth=0.5)
ax.add_feature(cfeature.COASTLINE, linewidth=0.5)

# Plot points
scatter = ax.scatter(
    df["Longitude"],
    df["Latitude"],
    s=sizes,
    c=df["LandArea"],
    cmap="viridis",
    alpha=0.8,
    edgecolor="black",
    transform=ccrs.PlateCarree()
)

# Colorbar
cbar = plt.colorbar(scatter, orientation='horizontal', pad=0.05)
cbar.set_label("Land Area (km²)")

# Title
plt.title("Global Distribution of Selected Cities\nMarker Size Scaled by Land Area", fontsize=14)

# Save high-resolution figure
plt.savefig("global_cities_map.png", dpi=300, bbox_inches='tight')

plt.show()
