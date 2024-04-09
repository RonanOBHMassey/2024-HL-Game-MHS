# Checks users enter yes (y) and no (n)
def yes_no(question):
    while True:
        response = input(question).lower()

        # Checks users response, question
        # Repeats if users don't enter yes / no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes / no")


def instructions():
    print('''
**** INSTRUCTIONS ****

To begin, Choose the number of rounds and either
customize the game parameters or go with the default game
(where the secret number is between 1 - 100).

Then choose the number of rounds you'd like to play,
Press <enter> for Infinite mode.

Your goal is to guess the secret number 
without running out of guesses.

Good Luck, Player!
    ''')


# Main Routine
print('''
⬆️⬆️⬆️ Welcome to the Higher Lower Game⬇️⬇️⬇️
''')


# Loop for testing purposes.


want_instructions = yes_no("Do you want to read the instructions? (Y/N)= ")

# Checks users enter yes (y) and no (n)
if want_instructions == "yes" or want_instructions == "y":
    instructions()

print("program continuing")
