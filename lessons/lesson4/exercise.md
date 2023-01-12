# Övningar

Den stegvisa övningen här kommer att vara tt skapa en kursplan/organiserare, mest för att få lite bättre kläm på klasser, vad de är och hur de används.

Utmaningen kommer vara ett finns i sjön spel.

## Kursplan del 1

Vi börjar med att skapa en klass för att hålla reda på en kurs. Vi kommer att använda den här klassen för att hålla reda på kursens namn, kursens kod, antalet poäng som kursen är värd och hur många poäng som kursen har.

Vi kommer att skapa en klass som heter `Course` och den kommer att ha följande attribut:

- `name` - Kursens namn
- `code` - Kursens kod
- `credits` - Antalet poäng som kursen är värd

Skapa sen en i klassen som kan skriva ut denna info om den här kursen aningen snyggt och formatterat.

Exempelvis,
Kurs: Python
Kurskod: DS_22_python
Poäng: 40

Skapa en main funktion, skapa en instans av klassen med hjälp av konstruktorn och skriv ut den med hjälp av din metod.

## Kursplan del 2

En kurs har också en lärare som undervisar den här kursen. Vi vill kunna hålla reda på lärarens namn och e-postadress. Vi vill också kunna skriva ut lärarens namn och e-postadress.

Skapa en klass som heter `Teacher`. Ni kan hitta på vad ni vill att det ska finnas på denna. Men även här skapa en method för att skriva ut det lite snyggare.

lägg till en lärare på `Course` klassen och skriv ut den med hjälp av din metod.

## Kursplan del 3

Vad är väl en kurs utan studenter? Vi vill kunna hålla reda på vilka studenter som går den här kursen. Vi vill också kunna skriva ut vilka studenter som går den här kursen.

Skapa en klass för elever. Jag tror ni börjar få kläm på detta nu.

Eftersom en klass sällan bara har en elev så kommer det att behövas en annnan datastruktur än en simpel instans i `Course` klassen. Ni har nog koll på vilken.

## Kursplan del 4

Gör samma sak som ovan men gör för Lektioner under kursen.

Skapa sedan metoder på `Course` klassen för att lägga till och ta bort elever och lektioner.

## Kursplan del 5

Skapa en meny i main som där användaren får välja några options.

- Lägg till en lärare till en kurs
- Lägg till en elev till en kurs
- Lägg till en lektion till en kurs
- Skriv ut en kurs
- Avsluta

Kom ihåg att varje gång programmet avslutas så kommer allt att försvinna då vi inte lärt oss att spara data än. Men det kommer härnäst.

## Finns i sjön

Kommer inom kort.
