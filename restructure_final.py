import os
import json
import shutil

# Paths
base_dir = "c:/chatgpt free ai/barcelona_graphics"
old_faces_dir = os.path.join(base_dir, "Leagues/La Liga/FC Barcelona/faces")
new_league_dir = os.path.join(base_dir, "La Liga")
json_path = os.path.join(new_league_dir, "Barcelona.json")

# Load JSON to get exact names
with open(json_path, "r", encoding="utf-8") as f:
    players = json.load(f)

# Move and rename images
repo_base = "https://raw.githubusercontent.com/leo997a/graphicsplayer2026/main/La%20Liga/"
updated_players = {}

for name, old_url in players.items():
    # Old filename was sanitized
    old_filename = old_url.split("/")[-1]
    old_file_path = os.path.join(old_faces_dir, old_filename)
    
    # New filename is exact name
    new_filename = name + ".png"
    new_file_path = os.path.join(new_league_dir, new_filename)
    
    if os.path.exists(old_file_path):
        shutil.move(old_file_path, new_file_path)
        # Update JSON with new URL
        safe_url_name = name.replace(" ", "%20")
        updated_players[name] = repo_base + safe_url_name + ".png"
    else:
        print(f"Warning: {old_file_path} not found")

# Write new JSON
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(updated_players, f, indent=2, ensure_ascii=False)

# Cleanup
shutil.rmtree(os.path.join(base_dir, "Leagues"))
for f in ["update_paths.py", "download_images.py", "restructure.py"]:
    p = os.path.join(base_dir, f)
    if os.path.exists(p):
        os.remove(p)

print("Restructured successfully to La Liga/ folder with exact names.")
