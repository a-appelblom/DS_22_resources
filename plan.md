# Python kurs

## Översikt

- [Föreläsning 1](#föreläsning-1-intro--installation), gemensam, Intro + installation
  - Presentation
  - Förväntningar undersökning
  - Kursplanen / Målen
  - Lektionsplanen
  - Inlämning - kort förklaring
  - Python
    - historia
    - användningsområden
  - Installation
    - Python
    - vscode
      - Python extension
    - Terminal
  - "Övning" 1 : Installlera
- [Föreläsning 2](#föreläsning-2), delad, Terminal, Variabler, Grundläggande Datatyper
  - Terminal
    - Navigering
    - Skapa mappar
    - skapa filer
    - Köra python
  - Python vad händer med min kod
  - Grundläggande Datatyper
    - Int
    - Float
    - String
    - Boolean
    - None
  - Aritmetik
- [Föreläsning 3](#föreläsning-3), gemensam, Datastrukturer, Logik
  - Listor
    - nesting / dimensioner
    - slicing
  - Set
    - Skapa
    - Set operationer
  - Dictionaries
    - . syntax
    - string syntax
    - nesting
  - tuples
    - Skapa
    - Unpacking
  - operatorer
    - "=="
    - "!="
    - ">"
    - ">="
    - "<"
    - "<="
  - if
    - if
    - elif
    - else
- [Föreläsning 4](#föreläsning-4): gemensam, funktioner, kodstruktur
  - DRY
  - Struktur i fil
  - Filstruktur
- [Föreläsning 5](#föreläsning-5): gemensam, Installera och använda bibliotek
  - ENV
    - PIP
    - Anaconda
    - PIPENV / VENV / CONDA
  - Bibliotek
    - Standard
      - enum
      - Datetim
      - ...mfl
    - Requests
- [Föreläsning 6](#föreläsning-6): delad, Hämta data
  - Fil
  - API
  - Scraping\*
- [Föreläsning 7](#föreläsning-7):, gemensam, Arbeta med databas
  - Typer av databas
  - Koppla till databas
  - SQL i python
  - ORM
    - SQLAlchemy
    - övriga
- [Föreläsning 8](#föreläsning-8): delad, DS bibliotek
  - Numpy
  - Pandas
  - Matlibplot
- [Föreläsning 9](#föreläsning-9): gemensam, Bygger webscraper
- [Föreläsning 10](#föreläsning-10): delad, Bygger API
- [Föreläsning 11](#föreläsning-11): TBD
- [Föreläsning 12](#föreläsning-12): TBD
- [Föreläsning 13](#föreläsning-13): TBD
- [Föreläsning 14](#föreläsning-14): TBD
- [Föreläsning 15](#föreläsning-15): TBD
- [Förläsning 16](#föreläsning-16): Projekt demo.

Ska läggas till

Klasser, Objekt

## Föreläsningar

---

### Föreläsning 1: Intro & Installation

#### Presentation

Jag presenterar mig. Vem jag är, vad jag gör och varför jag är här.

#### Förväntningar

Jag kommer att ge er lite frågot för att få lite koll på vad ni har för förväntningar på kursen.

#### Kursplan och kursmål

Vi går igenom kursplanen och kursmålen.

#### Lektionsplaneringen och hur jag lär ut

Jag visar upp min plan för hur lektionerna kommer att var och vad de kommer att innehålla.

Jag kommer också prata om hur jag brukar gå tillväga när jag lär ut. Livekodning, övningar och liknande.

#### Inlämningen - Kort

Jag kommer snabbt bara presentera vad inlämningen i kursen kommer att vara men jag kommer inte att ge ut uppgiften riktigt än. Detta för att uppgiften inte ska distrahera från det andra materialet som ska tas in.

#### Python

##### Historia

Jag går igenom vad Python är, var det kommer ifrån och hur det förändrats

##### Användningsområden

Jag kommer att visa några exempel på användningområden av python som språk. Jag kommer ocskå att visa lite exempel i kod.

#### Installation

##### Python

Jag kommer att demonstrerara hur n installerar python samt att gå igenom saker att vara försiktig med när man installerar.

##### Visual Studio Code

Jag kommer att visa er hur ni installerar visual studio code samt gå igenom vad det är. Vill ni använda ett alternativ till detta så får ni det men all livekodning jag gör kommer att vara i denna editor.

###### Python extension

I visual studio code så kan man ha extensions som ändrar beteendet av editorn. Jag kommer visa er hur ni installerar en extension för just Python för att förbättra upplevelsen.

##### Terminal

Jag kommer att gå igenom vilka terminaler vi kan avnända och vilka jag rekomenderar att ni installerar.

---

### Föreläsning 2: Terminal, Variable, Grundläggande datatyper

#### Terminal

Vi kommer att gå igenom och öva på att naviger i terminalen. Vi ska även titta på att skapa filer och hur vi kan köra Python genom terminalen, med filer och som interpreterare.

#### Vad händer med koden

Jag kommer prata om hur python exekveras och hur det man ser blir det som händer.

#### Grundläggande datatyper

Vi kommer prata om de grundläggande datatyperna i python.

Int: är en numerisk datatyp för att representera hela nummer.
Float: float är en numerisk datatyp för att representera decimaltal
String: datatyp som representerar text
Boolean: en boolean kan bara vara 2 värden, 1/0 AKA True / False
None: Representerar avsaknaden av data, är en global konstant i Python

#### Aritmetik

Med de datatyper vi gått igenom så ska vi prova lite aritmetik. Det vill säga lägga ihop, dividera och leka med datatyper i Python.

---

### Föreläsning 3: Datastrukturer & Logik

#### Listor

Vi kommer att gå igenom hur listobjekt funkar i python. Relatera det till annat samt gå igenom vad det är bra till. Vi kommer även gå igenom vad dimensioner i listor är.

#### Set

Vi kommer att gå igenom vad set är och hur vi kan använda dem i python. Vi kommer även att gå igenom vad det är bra till och vad det inte är bra till. Som unika värden och vad som händer om vi försöker lägga till samma värde flera gånger.

#### Dictionaries

Vi kommer att prata om vad dictionaries är och hur vi kan använda dem i python. Hur vi kommer åt värden i den, vad det får finnas för keys och vad de har för begränsningar.

#### Tuple

Vi ska prata om tuples. Dessa utmärker sig lite från andra objekt i vad de kan användas till.

#### Operatorer

Operatorer eller logiska operatorer i detta fall är vad som används för att jämföra värden i Python.

#### If-satser

Vi kommer att gå igenom hur vi kan använda if-satser i python. Vi kommer att gå igenom hur vi kan använda dem för att göra olika saker beroende på om ett värde är större eller mindre än ett annat värde.

### Föreläsning 4: Funktioner, Klasser, kodstruktur

---

### Föreläsning 5: Installera, hämta & använda paket

---

### Föreläsning 6: Hämta data

---

### Föreläsning 7: Arbeta med databaser

---

### Föreläsning 8: DataScience bibliotek

---

### Föreläsning 9: Bygga en enkel webscraper

---

### Föreläsning 10: Bygga ett API

---

### Föreläsning 11

---

### Föreläsning 12

---

### Föreläsning 13

---

### Föreläsning 14

---

### Föreläsning 15

---

### Föreläsning 16: ProjektDemo

Målet med denna föreläsning är att alla ska ha en chans att visa upp koden för mig och demonstrera att det finns en förståelse för hur den funkar.

Jag kommer sätta upp att var elev kan boka in en tid för en demo med mig.
