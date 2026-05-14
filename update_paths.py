import json
import os

path = "Leagues/La Liga/FC Barcelona/players.json"
repo_base = "https://raw.githubusercontent.com/leo997a/graphicsplayer2026/main/Leagues/La%20Liga/FC%20Barcelona/faces/"

with open(path, "r", encoding="utf-8") as f:
    data = json.load(f)

updated_data = {}
for name, url in data.items():
    filename = url.split("/")[-1]
    updated_data[name] = repo_base + filename

with open(path, "w", encoding="utf-8") as f:
    json.dump(updated_data, f, indent=2, ensure_ascii=False)

print("players.json updated with new paths.")
