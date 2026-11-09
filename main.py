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
    print("")
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


def create_deck(decks):
    print()
    print("===CREATE A DECK===")
    print("")
    print("Creating a deck takes about 1 minute.")
    print("Your decks are stored in this computer only.")
    print("No account or personal information needed.")
    print("")
    print("Type B to go back without creating a deck.")

    while True:
        name = input("Enter a name for your new deck: ").strip()
        if name.upper() == "B":
            return
        if name == "":
            print("Deck name cannot be empty. Please try again.")
        elif name in decks:
            print(f'A deck named "{name}" already exists. Please choose another name.')
        else:
            decks[name] = []
            save_decks(decks)
            print(f'Deck "{name}" created!')
            return


def find_deck(decks, choice):
    if choice.isdigit():
        number = int(choice)
        if 1 <= number <= len(decks):
            return list(decks)[number - 1]

    for name in decks:
        if name.lower() == choice.lower():
            return name

    return None


def deck_screen(decks, deck_name):
    while True:
        print()
        print(f'==={deck_name.upper()}===')
        print(f'This deck has {len(decks[deck_name])} cards.')
        print("")
        print("[A] Add a card")
        print("[S] Study this deck")
        print("[B] Back to Home")
        choice = input("Enter your choice: ").strip().upper()
        if choice == "B":
            return
        elif choice == "A":
            add_card(decks, deck_name)
        elif choice == "S":
            print("Study coming soon.")
        else:
            print("Invalid choice. Please try again.")


def ask_text(prompt):
    while True:
        text = input(prompt).strip()
        if text.upper() == "B":
            return None
        if text:
            return text
        print("This cannot be empty. Please try again.")


def add_card(decks, deck_name):
    while True:
        print()
        print(f'===ADD CARD: {deck_name.upper()}===')
        print()
        print("You can type B at any prompt to go back without saving.")
        print()
        print("Step 1 of 3: Enter the question")
        print("Step 2 of 3: Enter the answer")
        print("Step 3 of 3: Review and save")
        question = ask_text("Question: ")
        if question is None:
            return
        answer = ask_text('Answer: ')
        if answer is None:
            return

        print()
        print("===REVIEW YOUR CARD===")
        print("Step 3 of 3: Review and save")
        print()
        print(f"Question: {question}")
        print(f"Answer: {answer}")
        print()
        print("Please check your card for typos before saving.")
        print("Save this card?")
        print("[Y] Yes, save it")
        print("[E] Edit (go back and retype)")
        print("[B] Back to deck without saving")

        while True:
            confirm = input("Enter your choice: ").strip().upper()
            if confirm == "Y":
                decks[deck_name].append({"question": question, "answer": answer})
                save_decks(decks)
                print("Card saved!")
                return
            elif confirm == "E":
                break
            elif confirm == "B":
                return
            else:
                print("Invalid choice. Please try again.")


def main():
    decks = load_decks()
    while True:
        show_home(decks)
        choice = input("Enter your choice: ").strip()
        if choice.upper() == "Q":
            print("Goodbye! Your decks are saved.")
            break
        elif choice.upper() == "C":
            create_deck(decks)
        else:
            deck_name = find_deck(decks, choice)
            if deck_name:
                deck_screen(decks, deck_name)
            else:
                print("Invalid choice. Please try again.")



if __name__ == "__main__":
    main()