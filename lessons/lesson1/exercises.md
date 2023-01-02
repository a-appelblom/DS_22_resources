## Övning 1 / undersökning:

Finns separat

## Övning 2 / Installation:

### Terminal

Någon av dessa terminaler behöver ni ha installerade. Jag tror inte att ni faktiskt kommer att behöva göra någon, för både powershell och windowsterminalen finns förinstallerade i alla windows installationer jag kommit över den senaste tiden.
Gör den inte det så kan ni ladda ner den från länkarna nedan. Git bash är inget krav men kan vara bra att ha dels för att kommandon är mer lika de som hittas i unix (Linux/Mac) och dels för att det är ett bra verktyg för att jobba med git. Bra att kunna då servrar och virtuella miljöer av olika slag oftast är unix (Linux).

- [Windows Terminal](https://www.microsoft.com/en-us/p/windows-terminal/9n0dx20hk701?activetab=pivot:overviewtab)
- [powershell](https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell?view=powershell-7.1)
- [Git Bash](https://git-scm.com/downloads)

### IDE (Integrated Development Environment) / Text editor

Ni får använda exakt vilken editor ni vill. Men, och det kan vara ett stort men, jag kan lättast hjälpa er om ni använder visual studio code, det är också den som är absolut lättast att komma igång med. PyCharm är populär för python annars, Vim är en avancerad editor som kan vara kul att lära sig om man vill ha en utmaning. Men jag rekomenderar starkt att ni använder visual studio code.

- [Visual Studio Code](https://code.visualstudio.com/download)
- [Pycharm](https://www.jetbrains.com/pycharm/download/#section=windows)
- [Vim](https://www.vim.org/download.php) / [Neovim](https://neovim.io/)

#### Extensions

Se till att ni har följande extensions installerade i eran editor:

- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

### Python

#### Windows

Vad gäller själva python delen här så kan det bli lite mer komplicerat. Det finns två versioner av python, 2 och 3. Det är version 3 som är den som används idag och som vi kommer att använda i denna kurs.

Många operativsystem, däribland windows har ofta Python förisntallerat, åtminstone sedan senare versionerna av windows 10. Om ni lyckats att få igång någon av terminalerna ovan så kan ni testa att skriva `python --version` i terminalen och se om det fungerar och vilken version som kommer upp. Om det inte fungerar så kan ni ladda ner python från [här](https://www.python.org/downloads/windows/). Det är viktigt att ni väljer rätt version, 32 eller 64 bitar beroende på vilken version av windows ni har. Om ni inte vet vilken version ni har så kan ni kolla det [här](https://support.microsoft.com/en-us/help/13443/windows-which-operating-system). Om ni har en 64 bitars version av windows så är det 64 bitars version av python ni ska ladda ner.

Vi kommer i kursen att använda python 3.10.X, så se till att ni har den versionen eller senare. Se också till att installera PIP när ni installerar python. Det är ett verktyg som kommer att användas för att installera olika python paket senare i kursen. Har ni uppdaterat men ser ingen ändring, prova att starta om terminalen. Annars se nedan.

##### Path i windows

Windows är ofta inte din vän när det kommer till att automatiskt lägga till saker i din path och det händer ibland att man manuellt måste gå in och justera. Öppnar ni windows menyn och skriver in path borde det finnas ett alternativ som har med att redigera systemvariabler att göra. Klicka på det och gå in på fliken "Path" och kolla om python finns där. Om inte så kan ni lägga till den manuellt genom att klicka på "Edit" och sedan "New". Kommer ni hit så kan jag hjälpa er och så ska vi se till att allt funkar.

#### Mac

Mac kommer oftast även den förinstallerad med python, men gör den inte det så kan ni ladda ner den genom [denna länk](https://www.python.org/downloads/macos/).

Det borde inte nu vara några problem men i värsta fall kan även ni behöva uppdatera eran path, detta görs i en fill som beoende på terminal görs i en .bashrc eller .zshrc fil. Fastnar ni här säg till så hjälper jag er.

#### Linux

Använder ni linux så antar jag att ni vet vad ni gör eller inte är rädda för att experimentera. Fastnar ni ändå så säg till så hjälper jag er.

## Övning 3: Sätt lite färg på vardagen (Om ni vill och har tid)

### Visual Studio Code

Har ni lyckats installera visual studio code så rekomenderar jag nu att ni provar att göra den lite finare eller att passa era preferenser.

Ni hittar era installerade color themes genom att öppna kommandopanelen (Ctrl/Cmd + Shift + P) och skriva in "color theme" och välja "Preferences: Color Theme". Där kan ni välja bland ett antal olika färger. Prova några och se hur det ändras.

Det temat ni kommer att se i min editor till en början i alla fall är:
sythwave84 (https://marketplace.visualstudio.com/items?itemName=RobbOwen.synthwave-vscode)

men ni kan självklart välja vilket ni vill och jag rekomenderar att googla runt lite på vad som finns.

### Terminalen

På windows så rekomenderar jag att kolla in [oh-my-posh](https://ohmyposh.dev/docs/windows) och [oh-my-posh themes](https://ohmyposh.dev/docs/themes). Det är ett sätt att få en finare terminal. Följ instruktionerna på sidan för att se om ni kan lyckas hitta en terminal som ni vill. Ska funka i både powershell och och windows terminalen.

På mac så finns det lite olika alternativ också. Standard typen av terminal på en mac är bash. Ovan nämnda oh-my-posh ska funka där också, men denna är inspirerad från ett annat shell som heter zsh (vilket jag använder på linux) där det finns ett program som heter [oh-my-zsh](https://ohmyz.sh/). Det finns en hel del teman där också. Om ni vill kan ni prova att installera det och se om ni gillar det.

### Python

Prova att starta python i terminalen och se vad som händer.

Lek runt lite så kommer jag att visa mer om det i nästa lektion.

## Övning 4: Terminalen, mappar och filer

Pröva att med endast terminalen skapa följande:

```
min_mapp/
    min_fil.txt
    min_fil2.txt
    min_andra_mapp/
        min_fil3.txt
        min_fil4.txt
    min_tredje_mapp/
        min_fil5.txt
        min_fil6.txt
```

Flytta sedan alla textfiler att ligga i omvänd ordning. Så att min_fil6.txt ligger i min_mapp och min_fil.txt ligger i min_tredje_mapp osv.
Ta sedan bort min_tredje_mapp och filerna i den.
Döp om min_andra_mapp till min_speciella_mapp. med hjälp av mv / move kommandot.
Skapa en ny mapp som heter min_nya_mapp och flytta alla filer dit.
Ta bort min mapp
Ta bort min_nya_mapp

Lite hattigt men kommandona kommer att sitta efter detta.

## Övning 5: Git

1. Skapa ett konto på github
2. Skapa ett nytt repository
3. Klona det till din dator
4. Skapa en ny readme
5. Lägg till filen i git
6. Commita filen
7. Pusha filen till github
8. Gå in på github och se att filen finns där
