# Pipenv

Pipenv är ett verktyg för att hantera paket i Python. Det är en kombination av pip och virtualenv. Det är ett verktyg som är utvecklat av Kenneth Reitz, skaparen av Requests.

## Installation

### Installera med pip

Det enklaste sättet är att installera pipenv med pip.

```bash
pip install pipenv
```

### Kontrollera Path

Det kan vara så att pipenv inte är tillgängligt i terminalen. Det kan bero på att pipenv inte är tillagd i PATH. Det kan du kontrollera genom att skriva:

```bash
pipenv --version
```

Funkar det inte, prova att stänga alla terminaler och sen starta en igen och köra kommandot. Funkar inte det prova att skriva:

```bash
python -m pipenv --version
```

för att se att det faktiskt är installerat.

Du kan också prova att avinstallera pipenv och installera det igen.

```bash
pip uninstall pipenv
pip install pipenv
```

funkar det inte fortfarande så är det dags att lägga till pipenv till PATH. Kommer du till detta så hör av dig till mig eller google för ditt operativsystem.

## Skapa en miljö

Pipenv skapar automatiskt en miljö där du först använder det för att installera ett paket.Det går också att skapa en miljö genom att skriva:

```bash
pipenv shell
```

## Installera paket

Att installer paket är enklast att göra genom pipenv install kommandot. Det kommer att installera paketet i den miljö som skapades när du skapade miljön eller i den miljö som skapades när du installerade paketet.

```bash
pipenv install <package>
```

Är du i en aktiverad miljö, dvs att du kört pipenv shell, så kommer pipenv install att installera paketet i den aktiva miljön men även pip install kommer att funka.

### pipfile / pipfile.lock

Pipenv genererar en pipfile och en pipfile.lock. Pipfile är en fil som innehåller information om vilka paket som är installerade i miljön. Pipfile.lock är en fil som innehåller information om vilka paket som är installerade i miljön och vilka versioner av dessa paket som är installerade. Dessa genereras automatiskt och du behöver oftast inte tänka på dem.

Dessa är inspirerade från andra pakethanterare som npm och yarn i javascriptvärlden.

## Kommandon

För att aktivera din skapade miljö skriver du:

```bash
pipenv shell
```

För att lämna miljön skriver du:

```bash
exit
```

För att installera ett paket skriver du:

```bash
pipenv install <package>
```

För att installera alla paket som är listade i pipfile.lock skriver du:

```bash
pipenv install
```

För att se vilka paket som är installerade skriver du:

```bash
pipenv graph
```

För att aktivera en specifik miljö skriver du:

```bash
pipenv shell --three
```

För att ta bort en specifik miljö skriver du:

```bash
pipenv --rm
```

För att ta bort alla miljöer skriver du:

```bash
pipenv --rm --all
```

För att se vilka miljöer som finns skriver du:

```bash
pipenv --venv
```

För att se vilken python som används skriver du:

```bash
pipenv --py
```

För att se vilken pip som används skriver du:

```bash
pipenv --pip
```

För att se vilken pipenv som används skriver du:

```bash
pipenv --pipenv
```

För att starta en miljö med en specifik pythonversion skriver du exempelvis:

```bash
pipenv --python 3.6
```

Men detta kräver att du har den versionen av python installerad på din maskin.
