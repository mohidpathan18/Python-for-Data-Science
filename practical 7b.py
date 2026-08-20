import requests
from bs4 import BeautifulSoup
url = "https://www.wikipedia.org/"

headers = {
    "User-Agent": "Mozilla/5.0"
}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
print ("mohid pathan")
print("----- FIRST 3 PARAGRAPHS -----")
paragraphs = soup.find_all("p")
for p in paragraphs[:3]:
    print(p.get_text(strip=True))
print("\n----- IMAGE SRC URLs -----")
images = soup.find_all("img")
for img in images:
    print(img.get("src"))
print("\n----- TOTAL LINKS -----")
links = soup.find_all("a")
print("Total Links:", len(links))
print("\n----- HEADINGS -----")
headings = soup.find_all(["h1", "h2", "h3"])
for heading in headings:
    print(heading.get_text(strip=True))
print("\n----- LANGUAGES -----")
languages = soup.select(".central-featured-lang strong")
for language in languages:
    print(language.get_text(strip=True))
