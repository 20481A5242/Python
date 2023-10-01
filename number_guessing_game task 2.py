import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)
attempts = 0
max_attempts = 10

while attempts < max_attempts:
    # Get the player's guess
    guess = int(input("Guess the number: "))

    # Increment the attempts counter
    attempts += 1

    # Check if the guess is correct
    if guess == secret_number:
        print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
        break
    elif guess < secret_number:
        print("Try a higher number.")
    else:
        print("Try a lower number")

# Check if the player has exhausted all attempts
if attempts == max_attempts:
    print(f"Sorry, you've run out of attempts. The secret number was {secret_number}.")
