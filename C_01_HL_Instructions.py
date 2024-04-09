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

To begin, decide on a score goal
(eg: the first one to reach a score of 50 wins).

For each round of the game, you win points by rolling dice.
The winner of the round is the one who gets 13 (or slightly less)

If you win the round, then your score will increase by the number of points you earned.
If your first roll of two dice is a double (eg: both dice are the same number) 
then your score will be DOUBLE the number of points

If you lose the round, say goodbye to those potential points!

If you and the computer tie, (eg: you both get a score of 11) 
then you will get the points and the computer will not.

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
