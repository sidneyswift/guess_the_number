import random

def number_guessing_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    
    print("Welcome to the Number Guessing Game!")
    print("I have chosen a number between 1 and 100.")
    print("Can you guess what it is?")
    
    while True:
        guess = input("Enter your guess: ")
        
        # Ensure the input is a valid number
        if not guess.isdigit():
            print("Please enter a valid number.")
            continue
        
        guess = int(guess)
        attempts += 1
        
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number in {attempts} attempts.")
            break

if __name__ == "__main__":
    number_guessing_game()
