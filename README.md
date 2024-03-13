# Team 40 - Game of Stones

## Development

### Prerequisites:

- python 3.12
- mise 2024.1.12 or later

### Installation

```bash
# create python venv with mise
mise trust

# install required libraries
pip install -r requirements.txt

# install precommit to format files automatically with every commit
pre-commit install

# run the application
python main.py
```

## Spēles apraksts

Pirms spēles sākuma lietotājs izvēlas:

- sākuma akmentiņu skaitu (no 50 līdz 70)
- kurš pirmais uzsāks spēli - lietotājs vai dators
- kuru algoritmu izmantos dators

Uz galda atrodas tik daudz akmentiņu, cik izvēlās cilvēks-spēlētājs (no 50 līdz 70).
Katram spēlētājam spēles sākumā ir 0 akmentiņu un 0 punktu.
Spēlētāji izpilda gājienus pēc kārtas. Spēlētājs savā gājienā drīkst paņemt sev 2 vai 3 akmentiņus.
Ja pēc akmentiņu paņemšanas uz galda ir palicis pāra akmentiņu
skaits, tad pretinieka punktiem tiek pieskaitīti 2 punkti, bet ja nepāra skaits, tad spēlētāja punktu skaitam tiek pieskaitīti 2 punkti.
Spēle beidzas, kad uz galda nepaliek neviens akmentiņš.
Spēlētāju punktu skaitam tiek pieskaitīts spēlētājam esošo akmentiņu skaits.
Ja spēlētāju punktu skaits ir vienāds, tad rezultāts ir neizšķirts.
Pretējā gadījumā uzvar spēlētājs, kam ir vairāk punktu.

## Darba uzdevumi:

- spēles koka vai tā daļas ģenerēšana
- heiristiskā novērtējuma funkcijas izstrāde
- Minimaksa algorima izstrāde
- Alfa-beta algoritma izstrāde
- 10 eksperimenti ar katru no algoritmiem, fiksējot datora un cilvēka uzvaru skaitu, datora apmeklēto virsotņu skaitu, datora vidējo laiku gājiena izpildei
- GUI izveide
- atskaites noformēšana
