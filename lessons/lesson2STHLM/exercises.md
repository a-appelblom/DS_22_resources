# Övningar

Vi är inte riktigt på en nivå att skriva riktiga program eller script än men vi kommer att börja göra det nästa gång. Men ni ska få experimentera lite är tanken.

## Övning 1

använd variabler av de olika grundtyperna. (int, float, str, bool).

Gör lite aritmetik med dem fast blanda lite och se vad som funkar, läs vad ni får för felmeddelanden när det inte går.

exempelvis addera en `int` med en `str` och se vad som händer.
exempelvis addera en `int` med en `float` och se vad som händer.
exempelvis addera en `float` med en `str` och se vad som händer.
exempelvis addera en `float` med en `bool` och se vad som händer.
osv med andra operationer som multiplikation, subtration och division.

## Övning 2

Lek med strängar. Skapa en sträng försök sedan att extrahera en del av den strängen till en ny sträng. Exempelvis om du har en sträng som heter `s = "Hello World"` så kan du extrahera "Hello" genom att skriva `s[:5]` och "World" genom att skriva `s[6:]`.

Le runt med lite olika strängar och se vad som händer.

## Övning 3

Skapa 2 listor med lite olika element i.

Testa vad som händer om ni kör aritmiska operationer på dessa.
Prova att plussa ihop listorna med `+` och se vad som händer.
Prova att multiplicera listorna med `*` och se vad som händer.

Prova att nästa listor och se hur långt ner ni kan komma :D.
Glömde kankse nämna att för att komma åt element i en nästlad lista så lägger man bara till fler hakar. Exempelvis om du har en lista som heter `l = [[1,2,3],[4,5,6],[7,8,9]]` så kan du komma åt 5 genom att skriva `l[1][1]`. Det är första hakarna som anger vilken lista du vill komma åt och det andra haket som anger vilket element i den listan du vill komma åt. Det är alltså en lista av listor. Detta kan göras flera gånger.

## Övning 4:

Gör samma sak som med listorna fast med dictionaries. Se vad som händer, vad ni får för felkoder.

Prova att lägga till lite olika datatyper både som värde och key i dictionaries. Se vad ni får för felkoder. Prover er fram och se vad som fastnar.

## Övning 5: For loop

Använd en for loop för att iterera över en lista och printa ut alla elementen i listan.
Gör samma sak för alla element i en dictionary genom att använda `min_dict.items()` eller `min_dict.keys()`.

Använd range för att skapa en lista med alla tal mellan 0 och 10. Använd sedan en for loop för att iterera över listan och printa ut alla talen.
DVS 2 for loopar efter varandra.

Lite extra info, en for loop går att bryta med `break` och den går att hoppa över ett steg med `continue`.

## Övning 6: Booleans

Testa att skapa några booleans och testa olika logiska operatorer. Exempelvis `and or not` och `== != < > <= >=`.
Gör helt enkelt vad vi gjorde under föreläsningen fast bygg på det ngra steg.

Finns egentligen inte så mycket mer att göra här än att experimentera lite.

## Övning 7: If statements

Börja med att testa några if-satser som är väldigt enkla. Exempelvis om `x == 5` så printa "x är 5". Lägg även till några elif-satser och en else-sats.
Testa med lite mer komplicerade uttryck som använder logiska operatorer och `or and not`

Testa att skapa några ifsatser som är lite mer komplicerade. Det går exempelvis också att nästla if-satser om nödvändigt, dvs att ha en if-sats i en if-sats, men oftast är det isåfall bättre med att testa för det negativa först. Jag kommer att prata mer om det senare i kursen.

## Övning 8: While loop

Testa att skapa en infinite loop. Bara för att se vad som händer. Det är inte så farligt. Det är bara att stänga ner programmet.

Stänga ner programmet ganske enkelt genom att trycka på `ctrl + c` i terminalen där programmet körs.

Testa nu att skriva en loop som bryter ur sig själv. Det vill säga en loop som inte är en infinite loop. Detta kan göras genom att använda `break` i en if-sats. Exempelvis om du har en while loop som heter `while True:` så kan du skriva `if x == 5: break` och då kommer loopen att bryta när `x` är 5.

## Övning 9: Vi sätter ihop allt (Higher Lower)

Vi har for loopar, while loopar och if-satser. Vi har också variabler och olika typer av variabler. Vi har också listor och dictionaries. Vi ska nu sätta ihop allt detta och skapa ett program som gör något.

Vi kommer använda 1 metod som vi inte pratat om men annars är det fritt fram det ni ni redan kan. Jag skapar en starter i mappen.

Vi ska hur som helst skapa ett spel där vi ska gissa på ett tal och om nästa tal är högre eller lägre än det vi gissat på. Om vi gissar rätt så ska vi få ett meddelande om att vi vunnit.

Målet är också att spelet bara ska fortsätta så längre vi gissar rätt. Vi ska kunna avsluta spelet genom att skriva `exit` när vi gissar.

Vi ska också kunna se hur många gissningar vi gjort. Det vill säga hur många poäng vi har. Det kan lösas med en variabel som sparar score.

!!! OBS !!!
Om det inte finns en fil som heter high_lower.py så vänta lite så kommer den strax. Där finns det mer info. Efter jag föreberett den så kommer denna också att uppdateras med mer info.
