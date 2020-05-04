# Game: Place N queens in NxN grid

Test of programming knowledge for BNP, using Python 3.

## Installation

Clone this repository and install dependencies in virtualenv.

```bash
virtualenv -p python3 myenv
source myenv/bin/activate # In Linux
source myenv/script/activate # In Windows
pip install -r requirements.txt
```

## Usage

```bash
python main.py
```

## Commands

Commands:
- Goback. Quit the last movement.
- Color. Switch between display types colored or black/white.
- Resolve. Take the actual state of the grid and resolve it with best-first search algorithm.
- Exit. Finish the game.
