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


# Guessing loop

# Replace number below with random number between high / low values
secret = 7

# parameters which exist in the base game
low_num = 0
high_num = 10
guesses_allowed = 5

# Set guesses used to zero at the start of each round
guesses_used = 0
already_guessed = []

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
        feedback = "Uh Oh! you ran out of guesses and you haven't guessed the secret number so... You Lose this round!"

    # print feedback to user
    print(feedback)

    # additional feedback to warn user that they have almost run out
    if guesses_used == guesses_allowed - 1:
        feedback = "\n💣💣💣 Careful You Have 1 Guess Left! 💣💣💣"

print()
print("End of this round")