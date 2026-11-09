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


def show_home(decks):
    print("===FLASHCARD APP===")
    print("Create flashcard decks for your courses and quiz yourself to prepare for exams.")
    print("")
    print("Your decks:")
    if not decks:
        print("You have no decks yet. Type C to create one.")
    else:
        for number, name in enumerate(decks, start=1):
            print(f"{number}. {name} ({len(decks[name])} cards)")
    print("")
    print("[#] Open a deck by number      [C] Create a new deck")
    print("[Q] Quit")
    print("")
    print("Can't find your deck by number? Type its name.")


def main():
    decks = load_decks()
    show_home(decks)


if __name__ == "__main__":
    main()