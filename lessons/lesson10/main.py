import requests
from bs4 import BeautifulSoup

url = "https://ecutbildning.se/utbildningar/data-scientist/"
url_with_form = "https://ecutbildning.se/intresseanmalan/"

page = requests.get(url).text
with_form_page = requests.get(url_with_form).text

data = BeautifulSoup(page, "html.parser")
data_with_form = BeautifulSoup(with_form_page, "html.parser")


page_title = data.find("title")

page_heading = data.find("h1")

page_links = data.find_all("a")

print(page_title.text)
print(page_heading.text)

# print(page_links)

for link in page_links:
    if link.has_attr("href"):
        print(link["href"])

# forms = data_with_form.find_all("form")

# for form in forms:
#     print(form.find_all("input"))
