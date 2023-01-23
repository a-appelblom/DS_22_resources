import os
import csv
from gtts import gTTS


def main():
    with open("data.csvt", encoding="utf-8") as file:
        csvreader = csv.reader(file)
        headings = next(csvreader)
        # print(headings)
        data = []
        for row in csvreader:
            data_object = {headings[i]: col for i, col in enumerate(row)}
            data.append(data_object)
        print(data[0]["avsnittsrubrik"])

        searchword = input("Search word: ")

        for obj in data:
            if searchword in obj["anforandetext"]:
                print(f"Rubrik: {obj['avsnittsrubrik']}")
                print(f"Talare: {obj['talare']}")
                print(obj['anforandetext'])
                print("____________________________________")
                sound = gTTS(text=obj['anforandetext'], lang="sv", slow=False)
                filename = f"{obj['avsnittsrubrik']}.mp3"
                sound.save(filename)


main()
