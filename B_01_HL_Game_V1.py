import math


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
customise the game parameters or go with the default game
(where the secret number is between 1 - 100).

Then choose the amount of rounds you'd like to play,
Press <enter> for Infinite mode.

Your goal is to guess the secret number 
without running out of guesses.

Good Luck, Player!
    ''')


# Check that users have entered a valid option
def int_check(question, low=None, high=None, exit_code=None):

    # if any integer is allowed...
    if low is None and high is None:
        error = "Please enter an integer"

    # if the number needs to be higher than an integer
    # (ie: rounds / high number)
    elif low is not None and high is None:
        error = f"Please enter an integer more than / equal to {low}"

    # if the number needs to be between low and high
    else:
        error = f"Please enter an integer that is between {low} and {high} (inclusive)"

    while True:
        response = input(question).lower()

        # check for infinite mode / exit code
        if response == exit_code:
            return response

        try:
            response = int(response)

            # check if the integer not too low.
            if low is not None and response < low:
                print(error)

            # check response is more than the low number
            elif high is not None and response > high:
                print(error)

            # if response is valid, return it
            else:
                return response

        except ValueError:
            print(error)


# calculate the number of guesses allowed
def calc_guesses(low, high):
    num_amount = high - low + 1
    max_raw = math.log2(num_amount)
    max_upped = math.ceil(max_raw)
    max_guesses = max_upped + 1
    return max_guesses


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
num_rounds = int_check("How many rounds would you like? Press <enter> to play Infinite Mode: ", low=1, exit_code="")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5

# Get Game parameters
low_num = int_check("Low Number? ")
high_num = int_check("High Number? ", low=low_num+1)
guesses_allowed = calc_guesses(low_num, high_num)

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
