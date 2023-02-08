# Frågor och svar om uppgiften

## Ska jag skapa en environment för min uppgift?

Svaret är helst men inget krav. Jag rekomenderar att ni skapar en mapp någonstans på era datorer där ni har alla projekt ni vill köra. Då kan ni enkelt skapa en environment för alla projekt och sedan aktivera den när ni vill köra projektet. Detta gör att ni inte behöver installera alla paket för alla projekt varje gång ni vill köra ett projekt. Detta är särskilt bra om ni har flera projekt som använder samma paket. 

Uppgiften skulle jag bara säga är ett av dessa projekt. Men kör ni globala installationer osv så spelar det inte så stor roll. Bara ni lyckas zippa eller ladda upp till github för att lämna in så är det bra.

## Vilka filer kommer jag att behöva skapa?

Det finns egentligen bara 3 grundstenar som ni behöver skapa. 

- Minst 1 fil som innehåller api:et, det är helt okej att dela upp i flera
- Minst 1 fil som är programmet/scriptet som pratar med api:et. Denna är dock väldigt fri, tänk todo-appen vi gjorde.
- Minst 1 fil som är grundatan som ska läsas in i databasen, kan vara csv, json, xml eller vad ni vill.

- Vill ni underlätta arbetet så skulle jag också separera databaslogiken från api:et. Detta gör att ni kan byta ut databasen utan att behöva ändra api:et. Detta är dock inget krav. Tänk todo-appen vi gjorde.
- Ni kan också ha en separat sql-fil för att skapa databasen och tabellerna. Detta är dock inget krav.
- Ett separat script för att seeda databasen skulle också vara att rekomendera för att inte blanda in denna logik i api:et eller programmet.

## Hur mycket får jag kopiera från lektionen?

Svaret på denna fråga är tyvär inte helt solklar. För G-nivå får den vara ganska lik, men ni får inte använda samma db-schema som jag gjort på demolektioner, dvs, todo eller det konstiga strukturlösa vi använde på första api-lektionen. Bara genom att byta ut hur databasen ser ut så är det inte längre samma api och ni kommer att behöva ändra saker för att passa till det nya schemat. Ni kommer behöva anpassa routes och liknande för att passa eran databas. Ser jag att ni queryar exempelvis get/bananas och har en route som är /todos så kommer jag inte bli speciellt imponerad. Detta tyder på att ni inte har förstått vad ni gör och kan leda till underkänt om det inte är så att det bara är en genuin miss som uppdagas när ni demoar.

Satsar ni å andra sidan på VG så vill jag se lite påpyggnad på det jag gjort. Inga hårda krav, men det ska finnas självständighet i arbetet. Vissa metoder kan vara lika, databasen kommer alltid vara databasen, en route kommer alltid att vara en route, men ni kanske har kedjat ihop anrop exempelvis, eller har byggt ut api:et med flera extra routes med varierande logik. Mitt tips är att försöka bygga något ni kanske rent utav kan få användning för. Brukar vara roligare då. Ni kanske skapar logik för att skapa användare med login till exempel.

## Hur ska jag lämna in?

Jag ser helst att ni lämnar in en länk till ett github-repo, men ni får såklart zippa och lämna in också. Men Det kan vara bra att börja bygga upp era github-profiler nu. Det är ett bra verktyg att ha i framtiden.
