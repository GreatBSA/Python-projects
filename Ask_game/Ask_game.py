import random

def Ask_game():
    x = ["AHMED", "BASIL", "ZIYAD", "ABDULLAH", "ABDULRAHMAN", "ALEX", "MAX"]
    person_selected = False  # Flag to track if a person has been selected

    # Randomly select one person to mark with "ASK ===>"
    selected_person = random.choice(x)

    for person in x:
        if person == selected_person and not person_selected:
            print("ASK ===>", person)
            person_selected = True  # Mark that a person has been selected
        else:
            print(person)

# Run the function
Ask_game()