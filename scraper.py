import requests
from bs4 import BeautifulSoup

url = "https://www.vlr.gg/team/120/100-thieves"
response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
soup = BeautifulSoup(response.text, "html.parser")

# scraper.py
def get_team_data():
    rows = []
    for team_id, name in TEAMS.items():   # TEAMS = {120: "100 Thieves", ...}
        # ... fetch and parse the page here ...
        rows.append({
            "team": name,
            "elo": 1720,
            "recent_win_rate": 0.65,
            "maps_played": 40,
        })
    return rows


print(soup.title.text)  # Should print the page title