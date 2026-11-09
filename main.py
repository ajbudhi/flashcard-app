import json
import os

DATA_FILE = 'decks.json'

def load_decks():
    if not os.path.exists(DATA_FILE):
        return {}

    with open(DATA_FILE, "r") as file:
         data = json.load(file)
         return data


def save_decks(decks):
    with open(DATA_FILE, "w") as file:
        json.dump(decks, file, indent=2)


def main():
    print("===FLASHCARD APP===")


if __name__ == "__main__":
    main()