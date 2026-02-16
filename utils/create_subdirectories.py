from pathlib import Path

# Base directory
base_dir = Path("../data")

# Folders to create in each subdirectory
new_dirs = [
    "city_boundary",
    "canopy_cover_map",
    "buildings",
    "grids",
    "global_canopy_cover_data"
]

# Loop through all subdirectories in data/
for subdir in base_dir.iterdir():
    if subdir.is_dir():
        for folder in new_dirs:
            (subdir / folder).mkdir(exist_ok=True)

print("Directories created successfully.")
