from dataclasses import dataclass
from typing import List
import requests
from bs4 import BeautifulSoup


@dataclass
class Contact:
    mail: str = None
    tel: str = None


@dataclass
class TopSite:
    rank: int
    title: str
    url: str
    google_text: str
    contact: Contact = None


cookies = {"SOCS": "CAESHAgCEhJnd3NfMjAyMzAxMzAtMF9SQzEaAnN2IAEaBgiA-uueBg"}
url = "https://www.google.com/search?q=webbyr%C3%A5+stockholm"

res = requests.get(url, cookies=cookies)
# print(res)
page = res.text
# print(page)
soup = BeautifulSoup(page, "html.parser")
# print(soup.prettify())
# print(soup.find("h2"))

# Målet är:
# Hämta alla sökresultat som inte är annonser - DONE
# Hämta text från sökresultatet
# Hämta url till sökresultaten
# Lägga till en rank

top_sites: List[TopSite] = []
rank = 1
a_tags = soup.find_all("a")
for tag in a_tags:
    # Ta bort alla search relaterade taggar
    if "search" in tag["href"]:
        continue
    # Tar bort alla interna länkar på sidan
    if tag["href"].startswith("#"):
        continue
    # Tar bort alla länkar till google
    if "google" in tag["href"]:
        continue
    # Ta bort edgecase /?
    if tag["href"].startswith("/?"):
        continue

    text = tag.text
    # print(text)

    url = tag["href"].split("=")[1].split("&")[0]

    # ALternativ till raden ovanför
    # url = tag["href"]
    # url = url.split("=")[1]
    # url = url.split("&")[0]
    # print(url)
    # print(rank)
    title = url.split("//")[1]
    if title.startswith("www"):
        title = title.split(".")[1].capitalize()
    else:
        title = title.split(".")[0].capitalize()
    # print(title)
    site = TopSite(rank, title, url, text)
    top_sites.append(site)
    # print(site)
    rank += 1

for site in top_sites:
    if site.title == "Wasabiweb":
        continue
    res = requests.get(site.url)
    # print(res.status_code)
    if res.status_code != 200:
        # print("Innacesible")
        continue

    page = res.text
    soup = BeautifulSoup(page, "html.parser")
    # print(soup.find("title").text)
    tel = ""
    mail = ""
    a_tags = soup.find_all("a")
    for tag in a_tags:
        if not tag.has_attr("href"):
            continue
        if "tel" in tag["href"] or "mailto" in tag["href"]:
            if not tel and tag["href"].startswith("tel"):
                tel = tag.text.strip()
                # print(tag.text.strip())
            if not mail and tag["href"].startswith("mailto"):
                mail = tag.text.strip()
                # print(tag.text.strip())

    if mail or tel:
        site.contact = Contact(mail, tel)

for site in top_sites:
    print(site)
