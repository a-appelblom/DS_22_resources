# Terminal Kommandon

### Navigering

- `cd` - Change directory (byt mapp). Används för att röra sig runt i filsystemet genom terminalen

  - `cd ..` - Gå tillbaka en mapp
  - `cd min_mapp` - Gå till "min_mapp" om den är en mapp i den "mappen" du är i
    - `cd /mapp/mapp2/` - Gå till mappen som heter "mapp2" som ligger i mappen som heter "mapp"

- `ls` - list files (lista filer). Visar vilka filer som finns i den mappen du är i
  - `ls -a` - Visar även dolda filer
  - `ls -l` - Visar mer information om filerna
  - `ls -la` - Visar mer information om filerna och dolda filer

### Manipulering av filer

- `touch` / `ni` - Skapa en fil
- `rm` - Ta bort en fil
  - `rm -r` - Ta bort en mapp och allt i den
- `mv` - Flytta en fil eller mapp
  - `mv fil.txt mapp/` - Flytta filen "fil.txt" till mappen "mapp"
- `cp` - Kopiera en fil eller mapp
  - `cp fil.txt mapp/` - Kopiera filen "fil.txt" till mappen "mapp"
- `mkdir` - Skapa en mapp

### GIT

- `git init` - Skapa ett nytt git-repo
- `git status` - Visa status för git-repo
- `git add` - Lägg till filer för att commita
- `git commit` - Commita ändringar
  - `git commit -m "meddelande"` - Commita ändringar med ett meddelande
- `git push` - Pusha ändringar till github
- `git pull` - Hämta ändringar från github
- `git clone` - Klona ett repo från github
  - `git clone "repo_url"` - klona repo från github
- `git log` - Visa logg för commits
- `git remote add "namn" "repo_url"` - Lägg till ett remote repo

### python

`python` / `python3` - Starta python
`python fil.py` - Kör filen "fil.py" med python
