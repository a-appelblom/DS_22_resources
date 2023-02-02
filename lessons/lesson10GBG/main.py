from dataclasses import dataclass
import re
from typing import List
import requests
from bs4 import BeautifulSoup


@dataclass
class Person:
    name: str
    title: str
    mail: str
    tel: str


url = "https://ecutbildning.se/utbildningar/data-scientist/"

res = requests.get(url)

page = res.text

soup = BeautifulSoup(page, "html.parser")

title = soup.find("title").text

heading = soup.find("h1").text  # DET STÅR H1

headings = soup.find_all("h2")

# print(title)
# print(heading)
# print(headings)

# for element in headings:
#     print(element)

# p_tags = soup.find_all("p")

# for tag in p_tags:
#     # print(tag)
#     test = tag.find("em")
#     print(test)

# test = soup.find_all(string=re.compile("card"))
# print(test)

# Resultatet vi vill ha, men inte förtjänar
# cards = soup.find_all("article", class_="card")
# print(cards)

a_tags = soup.find_all("a")

people_soup = []
for tag in a_tags:
    if tag.has_attr("href"):
        if "mailto" in tag["href"] or "tel" in tag["href"]:
            if "card-body" in tag.parent.parent.parent["class"]:
                tag = tag.parent.parent.parent
                people_soup.append(tag)

# print(people_soup.prettify())

people: List[Person] = []
for person in people_soup:
    # print("___")
    # print(person.prettify())
    name = person.find("h3").text.strip()
    title = person.find("p", itemprop="jobTitle").text.strip()
    tel = ""
    phone = ""
    person_links = person.find_all("a")
    # print(person_links)
    for link in person_links:
        if link["href"].startswith("tel"):
            phone = link.text.strip()
        elif link["href"].startswith("mailto"):
            mail = link.text.strip()

    people.append(Person(name, title, mail, phone))
    # print(name)
    # print(title)
    # print(mail)
    # print(phone)

# En person
# Namn
# Titel
# Tel
# Mail

for person in people:
    print(person)
