import random

def guessing_game():
    print("Welcome to the Guessing Game!")
    print("I've chosen a number between 1 and 100. Try to guess it!")

    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too low! Try guessing a higher number.")
        elif guess > secret_number:
            print("Too high! Try guessing a lower number.")
        else:
            print(f"Congratulations! You guessed the number {secret_number} correctly!")
            print(f"It took you {attempts} attempts.")
            break

def main():
    while True:
        guessing_game()
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()