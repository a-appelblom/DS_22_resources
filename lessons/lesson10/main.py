from dataclasses import dataclass
from typing import List
import requests
from bs4 import BeautifulSoup, ResultSet

url = "https://ecutbildning.se/utbildningar/data-scientist/"
url_with_form = "https://ecutbildning.se/intresseanmalan/"

page = requests.get(url).text
with_form_page = requests.get(url_with_form).text

data = BeautifulSoup(page, "html.parser")
data_with_form = BeautifulSoup(with_form_page, "html.parser")


page_title = data.find("title")

page_heading = data.find("h1")

page_links = data.find_all("a")

# print(page_title.text)
# print(page_heading.text)

# print(page_links)

people_soup = BeautifulSoup()

for link in page_links:
    if link.has_attr("href"):
        if "tel" in link["href"] or "mailto" in link["href"]:
            if "card-body" in link.parent.parent.parent["class"]:
                # print(link.parent.parent.parent.prettify())
                # print("____________")
                people_soup.append(link.parent.parent.parent)

# print(people_soup.prettify())
people_tags = people_soup.find_all(attrs={"class": "card-body"})
# print(people_tags)


@dataclass
class Person:
    name: str
    title: str
    phone_number: str
    email: str


people: List[Person] = []
for person in people_tags:
    # Hämta ett namn
    name = person.find("h3").text
    # print(name)

    # En titel
    title = person.find(itemprop="jobTitle").text
    # print(title)

    # En mail
    # Ett telefonnummer
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
for person in people:
    print(person)
# Skicka till ett api för att spara i en databas

# forms = data_with_form.find_all("form")

# for form in forms:
#     print(form.find_all("input"))
