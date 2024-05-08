import math
import random


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

To begin, choose the amount of rounds you'd like to play,
Press <enter> for Infinite mode.

Then choose the number of rounds and either
customise the game parameters or go with the default game
(where the secret number is between 0 - 10).

Your goal is to guess the secret number 
without running out of guesses.

Good Luck, Player!
    ''')


# Check for an integer with optional upper /
# lower limits and an optional exit code for infinite mode
# / quitting the game
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
end_game = "no"
feedback = ""

game_history = []
all_scores = []

print('''
⬆️⬆️⬆️ Welcome to the Higher Lower Game⬇️⬇️⬇️
''')

want_instructions = yes_no("Do you want to read the instructions? (Y/N)= ")

# Checks users enter yes (y) and no (n)
if want_instructions == "yes":
    instructions()

# Ask user for number of rounds
num_rounds = int_check("How many rounds would you like? Press <enter> to play Infinite Mode: ", low=1, exit_code="")

if num_rounds == "":
    mode = "infinite"
    num_rounds = 5

# ask user if they want to customise the number range
default_params = yes_no("Do you want the normal game parameters? ")
if default_params == "yes":
    low_num = 0
    high_num = 10

# allow user to choose high / low numbers
else:
    low_num = int_check("Low Number? ")
    high_num = int_check("High Number? ", low=low_num + 1)

# calculate the maximum number of guesses based on the lowest and highest numbers
guesses_allowed = calc_guesses(low_num, high_num)

# Game loop starts here
while rounds_played < num_rounds:

    if end_game == "yes":
        break

    # Rounds Headings
    if mode == "infinite":
        rounds_heading = f"\n⬆️⬇️ Round {rounds_played + 1} (INFINITE MODE)⬆️⬇️"
    else:
        rounds_heading = f"\n⬆️⬇️ Round {rounds_played + 1} of {num_rounds} ⬆️⬇️"

    print(rounds_heading)

    # Round starts here
    # Set Guesses used to zero at the start of the round
    guesses_used = 0
    already_guessed = []

    # choose a secret number between the low and high number
    secret = random.randint(low_num, high_num)

    guess = ""
    while guess != secret and guesses_used < guesses_allowed:

        # ask the user to guess a number
        guess = int_check("Guess: ", low_num, high_num, "xxx")

        # check that they don't want to quit
        if guess == "xxx":
            # set end_game to use so that outer loop can be broken
            end_game = "yes"
            break

        # check that guess is not a duplicate
        if guess in already_guessed:
            print(f"You have already guessed {guess}. You've *still* used {guesses_used} / {guesses_allowed} guesses")
            continue

        # if guess is not duplicate then add it to the already guessed list
        else:
            already_guessed.append(guess)

        # add 1 to the number of guesses used
        guesses_used += 1

        # compare the user's guess with the secret number set up feedback statement

        # if we have guesses left...
        if guess < secret and guesses_used < guesses_allowed:
            feedback = (f"Too Low, please try a higher number "
                        f"You've used {guesses_used} / {guesses_allowed} guesses")
        elif guess > secret and guesses_used < guesses_allowed:
            feedback = (f"Too High, please try a lower number "
                        f"You've used {guesses_used} / {guesses_allowed} guesses")

        # when the number is guessed, use 1 of three feedback lines
        elif guess == secret:

            if guesses_used == 1:
                feedback = "🍀Lucky! You got it on the First Guess!🍀"
            elif guesses_used == guesses_allowed:
                feedback = f"Phew! you got it in {guesses_used} guesses. That was your last guess!"
            else:
                feedback = f"Well Done! You guessed the secret number in {guesses_used} guesses"

        # if there are no guesses left
        else:
            feedback = ("you ran out of guesses and you haven't guessed the secret number so... You Lose this round! "
                        f"the number was... {secret}")
            guesses_used += 1

        # print feedback to user
        print(feedback)

        # additional feedback to warn user that they have almost run out
        if guesses_used == guesses_allowed - 1:
            feedback = "\n💣💣💣 Careful You Have 1 Guess Left! 💣💣💣"


    print()
    print("End of this round")

    rounds_played += 1

    # add guesses used to all scores to calculate stats
    all_scores.append(guesses_used)

    # add result to game_history list
    history_item = f"Round: {rounds_played} | Guesses: ({guesses_used} / {guesses_allowed}) {feedback}"
    game_history.append(history_item)

    # if users are in infinite mode, increase number of rounds
    if mode == "infinite":
        num_rounds += 1

# Game loop ends here

# Game history / Statistics area

if rounds_played > 0:
    # Game history / statistics

    # Calculate Statistics
    all_scores.sort()
    best_score = all_scores[0]
    worst_score = all_scores[-1]
    average_score = sum(all_scores) / len(all_scores)

    # output the statistics
    print("\n📈📊📉 Statistics 📈📊📉")
    print(f"Best: {best_score} | Worst: {worst_score} | Average: {average_score:.2f}")
    print()

    # display game history on request.
    see_history = yes_no("Do you want to see your game history? ")
    if see_history == "yes":
        for item in game_history:
            print(item)

        print()
        print("Thanks for playing!")

else:
    print("🐔🐔🐔 No Results As You Chickened Out! 🐔🐔🐔")

