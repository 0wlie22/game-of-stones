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
# or run in DEBUG mode, to see the hidden logs
python --log=DEBUG
```


## Darba uzdevumi:

- spēles koka vai tā daļas ģenerēšana
- heiristiskā novērtējuma funkcijas izstrāde
- Minimaksa algorima izstrāde
- Alfa-beta algoritma izstrāde
- 10 eksperimenti ar katru no algoritmiem, fiksējot datora un cilvēka uzvaru skaitu, datora apmeklēto virsotņu skaitu, datora vidējo laiku gājiena izpildei
- GUI izveide
- atskaites noformēšana
