# Venv

Venv är ett verktyg för att skapa isolerade Python-utvecklingsmiljöer. Det är ett verktyg som är inbyggt i Python och som är tillgängligt i alla versioner av Python 3.3 och senare.

## Skapa en venv

För att kunna skapa virtual environments behöver du ha Python 3.3 eller senare installerat på din dator. Det finns inget särskilt sätt att installera venv, det är ett inbyggt verktyg i Python.

Kontrollera att du har tillgång till python genom att öppna en terminal och skriva:

```bash
python --version
```

Funkar kommandot så är du redo att skapa en venv.

Annars prova att använda `python3` istället för `python`.

Funkar inte heller det så är det troligtvis så att du inte har Python installerat på din dator. Ladda ner och installera Python från [python.org](https://www.python.org/downloads/). När du installerar Python så kommer du att få frågan om du vill lägga till Python till PATH. Det är viktigt att du gör det. Det kan ocks vara så att du har python, då kan du välja modify istället och i installationen välja att lägga till python till PATH.

För att skapa en venv skriver du:

```bash
python -m venv <namn på venv>
```

Det kommer nu att skapas en mapp i den mappen där du skrev kommandot. Mappen kommer att heta `<namn på venv>`. I den mappen finns det en mapp som heter `Scripts` och en mapp som heter `Lib`. I `Scripts` finns det en fil som heter `activate`. Det är den filen som vi ska använda för att aktivera venv.

## Aktivera venv

### Windows

För att aktivera venv skriver du:

Om du är i bash på Windows:

```bash
source <namn på venv>\Scripts\activate
```

Om du är i powershell på Windows:

```powershell
<namn på venv>\Scripts\Activate.ps1
```

Alla dessa kommandon är dock beroende på i vilken mapp du befinner dig i. Om du inte är i samma mapp som venv-mappen så måste du skriva hela sökvägen till mappen.

Du ser nu att det står `(venv)` eller något liknande beroende på ditt namn på din venv framför din prompt. Det betyder att venv är aktiverat.

### Mac / Linux

För att aktivera venv skriver du:

```bash
source <namn på venv>/bin/activate
```

Alla dessa kommandon är dock beroende på i vilken mapp du befinner dig i. Om du inte är i samma mapp som venv-mappen så måste du skriva hela sökvägen till mappen.

Du ser nu att det står `(venv)` eller något liknande beroende på ditt namn på din venv framför din prompt. Det betyder att venv är aktiverat.

### Avaktivera venv

För att avaktivera venv skriver du:

```bash
deactivate
```

## Installera paket

### Pip

Pip är en pakethanterare inbyggd i Python. Det är den som används för att installera paket i venv.

För att installera paket skriver du:

```bash
pip install <namn på paket>
```

Se till att du är i rätt mapp och att du har aktiverat venv.
