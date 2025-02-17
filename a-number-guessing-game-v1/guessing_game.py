import random 
import statistics
import sys

# Create the start_game function.
# Write your code inside this function.

def game_instructions():
    print("""The game will randomly select a number between 1 to 10. 
Your goal is to guess the number with the fewest attempts.
After each guess, you will receive feedback:
    - 'Too low!' if your guess is smaller than the number.
    - 'Too high!' if your guess is greater than the number.
    - 'Correct!' if you guessed the right number!
You can quit anytime by typing 'QUIT'.
""")
# starts the game
def play_game():
    random_number = random.randint(1, 10)
    attempt = []

    while True:
        try:
            user_guess = int(input("Guess a number between 1 and 10:   "))
            if user_guess > random_number:
                print("Too high!")

            elif user_guess < random_number:
                print("Too low!")
            else: 
                print("Correct!")
                break
        except ValueError:
            print("Please enter a valid number.") 

# kicks off the app with a menu
def start_game():
    print("""\N{PARTY POPPER} Welcome to the Number Guessing Game! \N{PARTY POPPER}
Type 'INSTRUCTIONS' to learn how to play.
Type 'START' to play the game.
Type 'QUIT' to exit the game.
""")

    while True:
        user_input = input("> ")

        if user_input.upper() == 'INSTRUCTIONS':
            game_instructions()
        elif user_input.upper() == 'START':
            play_game()
        elif user_input.upper() == "QUIT":
            print("Thanks for playing! \N{WAVING HAND SIGN}")
            break
        else:
            print("Invalid choice. Type 'INSTRUCTIONS', 'START' or 'QUIT'")




#   When the program starts, we want to:
#   ------------------------------------
#   1. Display an intro/welcome message to the player.
#   2. Store a random number as the answer/solution.
#   3. Continuously prompt the player for a guess.
#     a. If the guess is greater than the solution, display to the player "It's lower".
#     b. If the guess is less than the solution, display to the player "It's higher".

#   4. Once the guess is correct, stop looping, inform the user they "Got it" and store the number of guesses it took in a list.
#   5. Display the following data to the player
#     a. How many attempts it took them to get the correct number in this game
#     b. The mean of the saved attempts list
#     c. The median of the saved attempts list
#     d. The mode of the saved attempts list
#   6. Prompt the player to play again
#     a. If they decide to play again, start the game loop over.
#     b. If they decide to quit, show them a goodbye message.

# ( You can add more features/enhancements if you'd like to. )


# Kick off the program by calling the start_game function.
start_game()