# Övningar lektion 3

Alla övningar utom utmaningen hänger ihop.

## Övning 1: miniräknare steg 1

skapa en main funktion. Gör en print som bara säger exempelvis "Miniräknare" eller "kalkylator". Anropa sedan funktionen när programmet körs.

För att öva på funktioner så får utskrifter till terminalen (annat än input utskriften) inte ske någon annanstans än i main() funktionen.

Skapa en funktion som kan addera ihop två tal och returnera resultatet. Skriv ut resultatet i main funktionen.

När detta funkar så fortsätt fast med att ta input från användaren för att addera ihop två tal. Input från användaren ska dock hämtas i en annan funktion.

## Övning 2: miniräknare steg 2

Skapa en funktion för att validera användarens input. Funktionen ska ta in en sträng och returnera True om strängen är ett heltal annars False. Använd funktionen för att validera input från användaren. Om input är ogiltig så ska användaren få ett felmeddelande och få försöka igen.

## Övning 3: miniräknare steg 3

Bygg nu vidare funktioner för att utföra andra beräkningar. Skapa funktioner för att subtrahera, multiplicera och dividera två tal.

När dessa funkar låt då användaren få välja vilken beräkning som ska utföras.

## Övning 4: miniräknare steg 4

Se om du nu kan skriva ett alternativ som gör det möjligt att använda resultatet från förra beräkningen som input till nästa beräkning. Detta ska fungera så länge användaren vill och med vilken beräkning som helst.

Målet här är därför att få funktionerna så generella som möjligt så att de kan återanvändas.

## Utmaningen: Tic Tac Toe / Luffarschack

!! Kommer mer strax tsms med en liten starter fil kallad tic_tac_toe_hint.py !!

Detta är en utmaning som är lite mer avancerad. Det kommer kräva lite jobb med listor, strängar och loopar.

Lite tips för att komma igång.
Lös uppgiften stegvis. Några funktioner som kanske kan vara bra att skapa är:
print_board() - skriver ut spelplanen

Det är enklast att börja med att skapa en funktion som kan skriva ut spelplanen. Hur ni löser detta är upp till er men jag kan tipsa om en lista med listor.

Mitt förslag till tecken att representera tomma rutor är `#` och för spelare 1 och 2 är det `X` och `O` respektive.
