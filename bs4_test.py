import requests
from bs4 import BeautifulSoup

url = "https://catalog.onliner.by/mobile"

response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=30)


#response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=30, params={"page":2})

response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

print(soup.title)
#html = response.text
#print(html)


