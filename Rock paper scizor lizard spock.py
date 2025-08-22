import random

# Opciones del juego
options = {
    1: ("✊", "Rock"),
    2: ("✋", "Paper"),
    3: ("✌️", "Scissors"),
    4: ("🦎", "Lizard"),
    5: ("🖖", "Spock")
}

# Reglas del juego
# Cada clave vence a los valores en la lista
win_conditions = {
    "Rock": ["Scissors", "Lizard"],
    "Paper": ["Rock", "Spock"],
    "Scissors": ["Paper", "Lizard"],
    "Lizard": ["Spock", "Paper"],
    "Spock": ["Scissors", "Rock"]
}

# Frases para cada victoria
action_phrases = {
    ("Scissors", "Paper"): "cuts",
    ("Paper", "Rock"): "covers",
    ("Rock", "Lizard"): "crushes",
    ("Lizard", "Spock"): "poisons",
    ("Spock", "Scissors"): "smashes",
    ("Scissors", "Lizard"): "decapitates",
    ("Lizard", "Paper"): "eats",
    ("Paper", "Spock"): "disproves",
    ("Spock", "Rock"): "vaporizes",
    ("Rock", "Scissors"): "crushes"
}


def get_choice_text(choice):
    emoji, name = options[choice]
    return f"{emoji} {name}"


def main():
    print("=" * 31)
    print("Rock Paper Scissors Lizard Spock")
    print("=" * 31)

    for number, (emoji, name) in options.items():
        print(f"{number}) {emoji} {name}")

    try:
        user_input = int(input("Pick a number: "))
        if user_input not in options:
            print("Invalid choice. Please pick a number between 1 and 5.")
            return
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    user_choice = options[user_input][1]
    user_display = get_choice_text(user_input)

    cpu_input = random.randint(1, 5)
    cpu_choice = options[cpu_input][1]
    cpu_display = get_choice_text(cpu_input)

    print(f"\nYou chose: {user_display}")
    print(f"CPU chose: {cpu_display}")

    if user_choice == cpu_choice:
        print("It's a tie!")
    elif cpu_choice in win_conditions[user_choice]:
        verb = action_phrases.get((user_choice, cpu_choice), "defeats")
        print(f"{options[user_input][0]} {verb} {options[cpu_input][0]}")
        print("The player won!")
    else:
        verb = action_phrases.get((cpu_choice, user_choice), "defeats")
        print(f"{options[cpu_input][0]} {verb} {options[user_input][0]}")
        print("CPU won!")


if __name__ == "__main__":
    main()

