from dataclasses import dataclass
import json
from typing import List
import requests
from bs4 import BeautifulSoup, ResultSet

from models import Person

# URLEN till vårat api
api_base_url = "http://127.0.0.1:8000/"

# URL som vi scrapar
url = "https://ecutbildning.se/utbildningar/data-scientist/"
url_with_form = "https://ecutbildning.se/intresseanmalan/"

# HTML Från sidan
page = requests.get(url).text
with_form_page = requests.get(url_with_form).text

# Skapar ett sökbart object av HTML:en
data = BeautifulSoup(page, "html.parser")
data_with_form = BeautifulSoup(with_form_page, "html.parser")


page_title = data.find("title")

page_heading = data.find("h1")

# Hittar Alla länkar i htmlen
page_links = data.find_all("a")

# print(page_title.text)
# print(page_heading.text)

# print(page_links)

# Skapar en ny soup instans för att appenda det vi vill ha senare
people_soup = BeautifulSoup()

# Går igenom alla länkar
for link in page_links:
    # Kolla om har en href
    if link.has_attr("href"):
        # Kollar om länken en mail eller telefon länk
        if "tel" in link["href"] or "mailto" in link["href"]:
            # Sparar parent node några nivåer upp i vår nya soppa
            if "card-body" in link.parent.parent.parent["class"]:
                # print(link.parent.parent.parent.prettify())
                # print("____________")
                people_soup.append(link.parent.parent.parent)

# print(people_soup.prettify())

# Skapar en itererbar version av våran soppa
people_tags = people_soup.find_all(attrs={"class": "card-body"})
# print(people_tags)


# @dataclass
# class Person:
#     name: str
#     title: str
#     phone_number: str
#     email: str


# Skapar en ny lista för skapa Person objekt i
people: List[Person] = []

# För varje person leta reda på datan vi vill ha
for person in people_tags:
    # Hämta ett namn
    name = person.find("h3").text
    # print(name)

    # Hämta titel
    title = person.find(itemprop="jobTitle").text
    # print(title)

    # Hämta En mail
    # Hämta Ett telefonnummer
    a_tags = person.find_all("a")
    for a in a_tags:
        if a["href"].startswith("tel"):
            tel_number = a.text.strip()
        if a["href"].startswith("mailto"):
            mail = a.text.strip()
    # print(tel_number)
    # print(mail)
    people.append(Person(name=name, title=title, phone_number=tel_number, email=mail))

# print(people)

# För varje person anropa api:et
for person in people:
    requests.post(api_base_url + "create_person", json.dumps(person.__dict__))
    print(person)
# Skicka till ett api för att spara i en databas

# forms = data_with_form.find_all("form")

# for form in forms:
#     print(form.find_all("input"))
# test = requests.get(api_base_url)
# print(test.text)
