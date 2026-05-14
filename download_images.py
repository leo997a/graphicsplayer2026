import os
import requests
import json

players_data = [
    {"name": "Alejandro Balde", "url": "https://sortitoutsidospaces.b-cdn.net/megapacks/cutoutfaces/originals/2026.03/67296654.png"},
    {"name": "Andreas Christensen", "url": "https://sortitoutsidospaces.b-cdn.net/megapacks/cutoutfaces/originals/2026.03/27066387.png"},
    {"name": "Dani Olmo", "url": "https://sortitoutsidospaces.b-cdn.net/megapacks/cutoutfaces/originals/2026.03/24048100.png"},
    {"name": "Eric García", "url": "https://sortitoutsidospaces.b-cdn.net/megapacks/cutoutfaces/originals/2026.03/28116427.png"},
    {"name": "Fermín", "url": "https://sortitoutsidospaces.b-cdn.net/megapacks/cutoutfaces/originals/2026.03/2000141742.png"},
    {"name": "Ferran Torres", "url": "https://sortitoutsidospaces.b-cdn.net/megapacks/cutoutfaces/originals/2026.03/89056845.png"},
    {"name": "Frenkie de Jong", "url": "https://sortitoutsidospaces.b-cdn.net/megapacks/cutoutfaces/originals/2024.09/37047745.png"},
    {"name": "Gavi", "url": "https://sortitoutsidospaces.b-cdn.net/megapacks/cutoutfaces/originals/2026.03/2000049413.png"},
    {"name": "Gerard Martín", "url": "https://sortitoutsidospaces.b-cdn.net/megapacks/cutoutfaces/originals/2026.03/2000101061.png"},
    {"name": "Joan García", "url": "https://sortitoutsidospaces.b-cdn.net/megapacks/cutoutfaces/originals/2026.03/67277675.png"},
    {"name": "João Cancelo", "url": "https://sortitoutsidospaces.b-cdn.net/megapacks/cutoutfaces/originals/2025.07/55041623.png"},
    {"name": "Jofre Torrents", "url": "https://sortitoutsidospaces.b-cdn.net/megapacks/cutoutfaces/originals/2026.03/2000297306.png"},
    {"name": "Jules Koundé", "url": "https://sortitoutsidospaces.b-cdn.net/megapacks/cutoutfaces/originals/2026.01/48036304.png"},
    {"name": "Lamine Yamal", "url": "https://sortitoutsidospaces.b-cdn.net/megapacks/cutoutfaces/originals/2026.03/2000256231.png"},
    {"name": "Marc Bernal", "url": "https://sortitoutsidospaces.b-cdn.net/megapacks/cutoutfaces/originals/2026.03/2000295603.png"},
    {"name": "Marc Casadó", "url": "https://sortitoutsidospaces.b-cdn.net/megapacks/cutoutfaces/originals/2026.03/2000058198.png"},
    {"name": "Pau Cubarsí", "url": "https://sortitoutsidospaces.b-cdn.net/megapacks/cutoutfaces/originals/2026.03/2000296497.png"},
    {"name": "Pedri", "url": "https://sortitoutsidospaces.b-cdn.net/megapacks/cutoutfaces/originals/2026.04/67293495.png"},
    {"name": "Raphinha", "url": "https://sortitoutsidospaces.b-cdn.net/megapacks/cutoutfaces/originals/2026.03/19242277.png"},
    {"name": "Robert Lewandowski", "url": "https://sortitoutsidospaces.b-cdn.net/megapacks/cutoutfaces/originals/2026.03/719601.png"},
    {"name": "Ronald Araujo", "url": "https://sortitoutsidospaces.b-cdn.net/megapacks/cutoutfaces/originals/2026.03/78085068.png"},
    {"name": "Wojciech Szczęsny", "url": "https://sortitoutsidospaces.b-cdn.net/megapacks/cutoutfaces/originals/2024.10/28009478.png"}
]

repo_url_base = "https://raw.githubusercontent.com/leo997a/graphicsplayer2026/main/images/"
output_json = {}

if not os.path.exists("images"):
    os.makedirs("images")

replacements = {
    "í": "i", "é": "e", "á": "a", "ó": "o", "ú": "u", "ñ": "n", 
    "ç": "c", "à": "a", "ã": "a", "ē": "e", "ō": "o", "ę": "e", "ś": "s"
}

for player in players_data:
    name = player["name"]
    url = player["url"]
    
    filename = name.lower().replace(" ", "_")
    for char, rep in replacements.items():
        filename = filename.replace(char, rep)
    
    filename += ".png"
    filepath = os.path.join("images", filename)
    
    try:
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(filepath, "wb") as f:
                for chunk in response.iter_content(1024):
                    f.write(chunk)
            output_json[name] = repo_url_base + filename
    except:
        pass

with open("players.json", "w", encoding="utf-8") as f:
    json.dump(output_json, f, indent=2, ensure_ascii=False)
