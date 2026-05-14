import os
import shutil
import json

base_dir = "c:/chatgpt free ai/barcelona_graphics"
la_liga_dir = os.path.join(base_dir, "La Liga")
barca_dir = os.path.join(la_liga_dir, "Barcelona")

if not os.path.exists(barca_dir):
    os.makedirs(barca_dir)

# Move all png files from La Liga/ to La Liga/Barcelona/
for f in os.listdir(la_liga_dir):
    if f.endswith(".png"):
        shutil.move(os.path.join(la_liga_dir, f), os.path.join(barca_dir, f))

# Move JSON
old_json = os.path.join(la_liga_dir, "Barcelona.json")
new_json = os.path.join(barca_dir, "Barcelona.json")
if os.path.exists(old_json):
    shutil.move(old_json, new_json)

# Update JSON URLs
repo_base = "https://raw.githubusercontent.com/leo997a/graphicsplayer2026/main/La%20Liga/Barcelona/"
with open(new_json, "r", encoding="utf-8") as f:
    data = json.load(f)

updated_data = {}
for name, url in data.items():
    filename = name + ".png"
    safe_name = name.replace(" ", "%20")
    updated_data[name] = repo_base + safe_name + ".png"

with open(new_json, "w", encoding="utf-8") as f:
    json.dump(updated_data, f, indent=2, ensure_ascii=False)

print("Moved everything to La Liga/Barcelona/ and updated JSON.")
