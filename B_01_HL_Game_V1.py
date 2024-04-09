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


# Check that users have entered a valid option based on a list
def int_check(question):
    while True:
        error = "Please enter an integer more than 1 or with out a decimal point."

        to_check = input(question)

        # check for infinite mode
        if to_check == "":
            return "infinite"

        try:
            response = int(to_check)

            # checks that the number is more than / equal to 13
            if response < 1:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# Main routine starts here

# Initialize game variables
mode = "regular"
rounds_played = 0

print('''
⬆️⬆️⬆️ Welcome to the Higher Lower Game⬇️⬇️⬇️
''')

want_instructions = yes_no("Do you want to read the instructions? (Y/N)= ")

# Checks users enter yes (y) and no (n)
if want_instructions == "yes" or want_instructions == "y":
    instructions()

# Ask user for number of rounds
num_rounds = int_check("How many rounds would you like? Press <enter> to play Infinite Mode: ")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5

# Game loop starts here
while rounds_played < num_rounds:

    # Rounds Headings
    if mode == "infinite":
        rounds_heading = f"\n⬆️⬇️ Round {rounds_played + 1} (INFINITE MODE)⬆️⬇️"
    else:
        rounds_heading = f"\n⬆️⬇️✂️ Round {rounds_played + 1} of {num_rounds} ⬆️⬇️"

    print(rounds_heading)
    print()

    user_choice = input("Choose: ")

    # if user enters exit code, game ends.
    if user_choice == "xxx":
        break

    rounds_played += 1

    # if users are in infinite mode, increase number of rounds
    if mode == "infinite":
        num_rounds += 1

# Game loop ends here

# Game history / Statistics area
