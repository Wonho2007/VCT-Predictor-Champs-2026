import requests
from bs4 import BeautifulSoup

url = "https://www.vlr.gg/team/120/100-thieves"
response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
soup = BeautifulSoup(response.text, "html.parser")
#Hi Sid
#Hi Sid it's wonho again

print(soup.title.text)  # Should print the page title