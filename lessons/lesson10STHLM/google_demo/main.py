from dataclasses import dataclass
from typing import List
import requests
from bs4 import BeautifulSoup


@dataclass
class TopSite:
    rank: int
    url: str
    google_text: str


cookies = {"SOCS": "CAESHAgCEhJnd3NfMjAyMjEyMDUtMF9SQzMaAnN2IAEaBgiAvI6dBg"}
url = "https://www.google.com/search?q=webbbyr%C3%A5+stockholm"

page = requests.get(url, headers={"USer-Agent": "Mozilla/5.0"}, cookies=cookies)

soup = BeautifulSoup(page.text, "html.parser")
tags = soup.find_all("a")

rank = 1
top_sites: List[TopSite] = []
for tag in tags:
    if tag["href"] == "#":
        continue
    elif "google" in tag["href"]:
        continue
    elif "search" in tag["href"]:
        continue
    elif tag["href"].startswith("/?"):
        continue

    # Hämtar url till sidan
    site_rank = rank
    url = tag["href"].split("=")[1].split("&")[0]
    text = tag.text

    # url = url.split("=")[1]
    # url = url.split("&")[0]
    site = TopSite(site_rank, url, text)
    top_sites.append(site)
    rank += 1

print(top_sites)
for site in top_sites:
    print(site)
