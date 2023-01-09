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

En liten note om spel som övning:
Jag gillar att använda spel som övningar och utmaningar under mina programmeringskurser, inte för att de är de mest användbara, utan för att de är väldigt tydligt definierade problem att lösa. Det är tydligt vad som är slutet och det är ganska lätt att planera inkrementen dit.

Ta detta spel så kan stegen vara.

1. Skriv ut spelplanen.
2. Ta input från användaren.
3. Ändra spelplanen med användarens input.
4. Validera inputen så inget kan skrivas över.
5. Kolla om någon har vunnit.
   5.1 kolla per rad
   5.2 kolla per kolumn
   5.3 kolla diagonalt

!!! Se tic_tac_toe_hint.py för fler tips.

Detta är en utmaning som är lite mer avancerad. Det kommer kräva lite jobb med listor, strängar och loopar.

Lite tips för att komma igång.
Lös uppgiften stegvis. Några funktioner som kanske kan vara bra att skapa är:
`print_board()` - skriver ut spelplanen
`get_input()` - tar input från användaren
`validate_input()` - validerar input från användaren, kom ihåg att det ska både vara ett valid input och att det ska vara en tom ruta
`update_board()` - uppdaterar spelplanen med användarens input
`check_winner()` - kollar om någon har vunnit

Det är enklast att börja med att skapa en funktion som kan skriva ut spelplanen. Hur ni löser detta är upp till er men jag kan tipsa om en lista med listor.

Mitt förslag till tecken att representera tomma rutor är `#` och för spelare 1 och 2 är det `X` och `O` respektive.

Lyckas ni lösa uppgiften väldigt enkelt kan ni testa att bygga ut det till ett spel mot datorn. Då kan ni använda `random` modulen för att slumpa vilken ruta som datorn ska välja.

Vill ni göra det ännu större kan ni sedan bygga vidare till ett fyra i rad spel istället. Då tillkommer det flere vinstkombinationer och fler regler.
