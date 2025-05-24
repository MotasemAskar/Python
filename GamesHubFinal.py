import random
import sys
import os

# Clear screen function
def clear_screen():
    """Clear the terminal screen on Windows or Linux/Mac"""
    os.system('cls' if os.name == 'nt' else 'clear')

# ─── Guess the Number Game ────────────────────────────────────────────────────
def guess_the_number():
    clear_screen()
    print("=== Guess the Number ===")
    while True:
        try:
            max_n = int(input("Enter the maximum number for the range (>=2): "))
            if max_n >= 2:
                break
            print("Number must be at least 2.")
        except ValueError:
            print("Please enter a valid integer.")
    secret = random.randint(1, max_n)
    attempts = 0
    while True:
        try:
            guess = int(input(f"Guess a number between 1 and {max_n}: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue
        attempts += 1
        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")
        else:
            print(f"✅ Correct! You took {attempts} attempts.")
            break
    input("\nPress Enter to return to menu...")

# ─── Rock Paper Scissors Game ─────────────────────────────────────────────────
def rock_paper_scissors():
    clear_screen()
    print("=== Rock, Paper, Scissors ===")
    choices = ['rock', 'paper', 'scissors']
    while True:
        mode = input("Choose mode: 1=Player vs Computer, 2=Player vs Player: ")
        if mode in ('1', '2'):
            break
        print("Invalid choice.")
    if mode == '1':
        while True:
            user = input("Enter 'rock', 'paper', or 'scissors': ").lower()
            if user in choices:
                break
            print("Invalid choice, please try again.")
        comp = random.choice(choices)
        print(f"Computer chose: {comp}")
        if user == comp:
            print("It's a tie!")
        elif (user == 'rock' and comp == 'scissors') or \
             (user == 'paper' and comp == 'rock') or \
             (user == 'scissors' and comp == 'paper'):
            print("🎉 You win!")
        else:
            print("😞 You lose!")
    else:
        print("Player 1 turn:")
        while True:
            p1 = input("Enter 'rock', 'paper', or 'scissors': ").lower()
            if p1 in choices:
                break
            print("Invalid choice.")
        print("Player 2 turn:")
        while True:
            p2 = input("Enter 'rock', 'paper', or 'scissors': ").lower()
            if p2 in choices:
                break
            print("Invalid choice.")
        print(f"Player 1 chose: {p1}")
        print(f"Player 2 chose: {p2}")
        if p1 == p2:
            print("It's a tie!")
        elif (p1 == 'rock' and p2 == 'scissors') or \
             (p1 == 'paper' and p2 == 'rock') or \
             (p1 == 'scissors' and p2 == 'paper'):
            print("🎉 Player 1 wins!")
        else:
            print("🎉 Player 2 wins!")
    input("\nPress Enter to return to menu...")

# ─── Hangman Game as Class ────────────────────────────────────────────────────
class Hangman:
    def __init__(self):
        self.word_categories = {
            'food':      ['pizza', 'burger', 'sushi', 'taco', 'pasta'],
            'colors':    ['red', 'blue', 'green', 'yellow', 'purple'],
            'countries': ['jordan', 'france', 'brazil', 'japan', 'egypt'],
            'animals':   ['lion', 'tiger', 'elephant', 'giraffe', 'zebra']
        }
        self.attempts_left = 6
        self.guessed_letters = set()

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def play(self):
        self.clear()
        print("=== Hangman ===")
        categories = list(self.word_categories.keys())
        print("Available categories:", ', '.join(categories))

        choice = input("Pick one: ").strip().lower()
        if choice not in self.word_categories:
            choice = random.choice(categories)
            print("Invalid category—randomly selecting:", choice)
        else:
            print("You chose:", choice)

        word = random.choice(self.word_categories[choice])
        self.attempts_left = 6
        self.guessed_letters.clear()

        print("Attempts left:", self.attempts_left)
        print(' '.join('_' for _ in word))

        while self.attempts_left > 0:
            guess = input("Guess a letter: ").strip().lower()
            if len(guess) != 1 or not guess.isalpha():
                print("Enter a single letter.")
                continue
            if guess in self.guessed_letters:
                print("Already guessed:", ' '.join(sorted(self.guessed_letters)))
                continue

            self.guessed_letters.add(guess)
            if guess not in word:
                self.attempts_left -= 1
                print("Wrong! Attempts left:", self.attempts_left)
            else:
                print("Nice!")

            display = ' '.join(letter if letter in self.guessed_letters else '_' for letter in word)
            print(display)

            if '_' not in display:
                print("🎉 Congratulations! You guessed it.")
                break

        if self.attempts_left == 0:
            print(f"😞 Game over. The word was: {word}")

        input("\nPress Enter to return to menu...")

# ─── Word Scramble Game ────────────────────────────────────────────────────────
def word_scramble():
    clear_screen()
    print("=== Word Scramble ===")
    words = [
        'banana', 'computer', 'python', 'jumble', 'awesome',
        'hangman', 'turtle', 'dolphin', 'mountain', 'parachute',
        'galaxy', 'butterfly', 'sunflower', 'notebook', 'pyramid',
        'oxygen', 'volcano', 'clockwork', 'rainbow', 'zeppelin'
    ]
    word = random.choice(words)
    scrambled = list(word) 
    random.shuffle(scrambled) 
    scrambled_word = ''.join(scrambled)
    print(f"Scrambled word: {scrambled_word}")
    guess = input("Rearrange the letters to form a word: ").lower()
    if guess == word:
        print("✅ Correct!")
    else:
        print(f"❌ Sorry, the correct word was: {word}")
    input("\nPress Enter to return to menu...")

# ─── 21 Count-Up w/ Auto-Risk (1–5) ───────────────────────────────────────────
def count_up_21():
    clear_screen()
    print("=== 21 Count-Up w/ Auto-Risk ===")
    total = 0
    player = 1

    while True:
        print(f"\nCurrent total: {total}")
        print(f"Player {player}'s turn.")
        while True:
            try:
                pick = int(input("Add 1–3: "))
                if pick in (1, 2, 3):
                    break
            except ValueError:
                pass
            print("Invalid. You must enter 1, 2, or 3.")

        total += pick
        print(f"Player {player} adds {pick}, total → {total}.")

        if total == 21:
            print(f"\n🎉 Player {player} hits 21 and wins!")
            break
        if total > 21:
            other = 2 if player == 1 else 1
            print(f"\n💥 Bust! Player {player} went over 21.")
            print(f"🏆 Player {other} wins by default.")
            break

        again = input("Risk it? (y/n): ").strip().lower()
        if again == 'y':
            risk_add = random.randint(1, 5)
            total += risk_add
            print(f"⚠️ Risk adds {risk_add}, total → {total}.")

            if total == 21:
                print(f"\n🎉 Player {player} hits 21 and wins!")
                break
            if total > 21:
                other = 2 if player == 1 else 1
                print(f"\n💥 Bust on risk! Player {player} went over 21.")
                print(f"🏆 Player {other} wins by default.")
                break

        player = 2 if player == 1 else 1

    input("\nPress Enter to return to menu...")

# ─── Dice Roll Game ──────────────────────────────────────────────────────────
def dice_roll():
    clear_screen()
    print("=== Dice Roll ===")
    for p in ("Player 1", "Player 2"):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        total = die1 + die2
        print(f"{p} rolled: {die1} and {die2} (Total: {total})")
        if p == "Player 1":
            score1 = total
        else:
            score2 = total
    if score1 > score2:
        print("🎉 Player 1 wins!")
    elif score2 > score1:
        print("🎉 Player 2 wins!")
    else:
        print("It's a tie!")
    input("\nPress Enter to return to menu...")

# ─── Math Quiz Game ─────────────────────────────────────────────────────────
def math_quiz():
    clear_screen()
    print("=== Math Quiz ===")
    while True:
        try:
            max_n = int(input("Enter the maximum number for quiz questions (>=2): "))
            if max_n >= 2:
                break
            print("Please enter at least 2.")
        except ValueError:
            print("Enter a valid integer.")
    score = 0
    rounds = 3
    print(f"Answer the following {rounds} questions:")
    for i in range(1, rounds + 1):
        a = random.randint(1, max_n)
        b = random.randint(1, max_n)
        op = random.choice(['+', '-', '*', '/'])
        expr = f"{a} {op} {b}"
        ans = eval(expr)
        try:
            resp = int(input(f"Q{i}. {expr} = "))
            if resp == ans:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong. The answer was {ans}.")
        except ValueError:
            print(f"Invalid input. The answer was {ans}.")
    print(f"\nYour score: {score}/{rounds}")
    input("\nPress Enter to return to menu...")

# ─── Main Menu ────────────────────────────────────────────────────────────────
def main():
    while True:
        clear_screen()
        print("=== Welcome to Games Hub")
        print("1. Guess the Number")
        print("2. Rock, Paper, Scissors")
        print("3. Hangman")
        print("4. Word Scramble")
        print("5. 21 Count-Up")
        print("6. Dice Roll")
        print("7. Math Quiz")
        print("0. Exit")
        choice = input("Select a game by number: ")

        if choice == '1':
            guess_the_number()
        elif choice == '2':
            rock_paper_scissors()
        elif choice == '3':
            Hangman().play()
        elif choice == '4':
            word_scramble()
        elif choice == '5':
            count_up_21()
        elif choice == '6':
            dice_roll()
        elif choice == '7':
            math_quiz()
        elif choice == '0':
            print("Goodbye!")
            sys.exit()
        else:
            print("Invalid selection, please try again.")
            input("Press Enter to try again...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExecution interrupted by user. Bye!")
    except SystemExit:
        pass
