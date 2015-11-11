__author__ = 'Jabari Dash'


'''
Write a program that prompts a user for their age.
(Only accept numeric values for the age), notify the
user if they enter anything other than a numeric value.
Based off of the user's answer, give them facts about
whether or not they can just drive a car, drive and drink,
and facts about where they should be in their academic/
profession path. After giving the facts, prompt the user to
play again, if they answer "n" for no, exit, otherwise start
the game over. Only accept "y", or "n" as the first letter of
their answer, notify the user if they enter anything else and
prompt them to answer "y" or "n" again.

Cannot drive:       age < 16
Drive, no drink:    16 <= age < 21
Drink and drive:    a >= 21

Has not graduate college:   1 <= age < 18
Currently in college:       18 < age <= 21
Currently in grad school:   21 < age <= 30
Should be in career:        30 < age <= 60
Should be retired:          60 < age <= 100
unrealistic age:            age < 1 or age > 100
'''


def main():

    # age is initially of type string to start the following loop
    age = ""

    # answer is initially of type int to start the final loop (end of main)
    answer = 0

    # Keep asking until user enters a number
    while type(age) is not int:

        try:

            # Prompt user to enter age
            age = int (input("Enter your age: "))

            # Skip line
            print("")

        # Only except numeric answers
        except ValueError:
            print("Please enter a numeric age")

    # If user is 16 or older, and less than 21
    if age >= 16 and age < 21:
        print("You are old enough to drive a car")

    # If user is older than 21
    elif age >= 21:
        print("You are old enough to drive and drink, but not together")

    # If user is anything else (less than 16)
    else:
        print("You are not old enough to drive")

    # If user is older than 0, and up to and including 18
    if (age >= 1 and age <= 18):
        print("You are probably have not graduated college yet")

    # If user is older than 18, and up to and including 21
    elif (age > 18 and age <= 21):
        print("You are probably in college")

    # If user is older than 21, and up to and including 30
    elif (age > 21 and age <= 30):
        print("You are probably in graduate school")

    # If user is older than 30, and up to and including 60
    elif (age > 30 and age <= 60):
        print("You should be in your career by now")

    # If user is older than 60, and up to and including 100
    elif (age > 60 and age <= 115):
        print("You should be retired")

    # If user is NOT within the acceptable range
    elif not(age > 0 and age < 100):
        print("You entered an unrealistic age")

    # Skip line
    print("")

    # Ask user to play again
    # While answer is not 'y' or 'n', keep asking for an answer
    while type(answer is not str or (answer[0] is not "y" or answer[0] is not "n")):

        try:
            # Prompt user to enter 'y' or 'n'
            answer = input("Would you like to play again? y/n ")

            # If 'y', call main over again
            if answer[0] == "y":
                main()

            # If 'n', exit the program
            if answer[0] == "n":
                print("Thanks, good bye!")
                print("Written by:", __author__)

                # Exits the program entirely
                exit(0)

            # If answer cannot be understood (not 'y' or 'n'), notify user
            else:
                print("Please type \"y\" or \"n\"\n")

        # If the user enters wrong value type (Numeric)
        except ValueError:
            print("Please type \"y\" or \"n\"\n")

# Call main to start the program
main()

