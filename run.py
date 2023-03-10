"""
Import required modules
"""

import gspread

from google.oauth2.service_account import Credentials
import random


def start_game():
    """
    Allow player to enter name and start quiz.
    """
    print("⭐⭐⭐⭐⭐  Welcome to Our Planets quiz! ⭐⭐⭐⭐⭐")

    # Defining variables as global to be able to access it globaly
    global username
    global planet_questions
    global options
    username = input("Please enter your username: \n")

    while username == "":
        print("A username is required to start the quiz, please try again.")
        username = input("Please enter your username: \n")

    # Capitalizes the first letter in the username in case
    # user enteres only lowercase letters
    username = username.capitalize()
    start = input(
        f"Hi {username} and welcome!"
        " Would you like to start the game? (y/n) \n"
    )
    start = start.lower()

    # Check that the input value is valid (y or n)
    while start != "y" and start != "n":
        start = input("Invalid input! Do you want to play? (y/n): \n")
        start = start.lower()

    if start == "y":
        print("Let´s start the game!⭐ \n")
        new_game()

    elif start == "n":
        print("Welcome back next time, bye! \n")


def new_game():
    """
    Creates a new game and starts the game and starts displaying questions.
    """
    global planet_questions
    global options
    guesses = []
    correct_guesses = 0
    question_num = 1
    # zip planet_questions and options
    zipped_questions_options = dict(zip(planet_questions, options))
    # convert to list to be able to use random.shuffle. Help from
    # https://stackoverflow.com/questions/19895028/randomly-shuffling-a-dictionary-in-python
    zipped_list = list(zipped_questions_options.items())
    random.shuffle(zipped_list)
    # Only use 8 questions, so all the questions are not printed every game
    zipped_list = zipped_list[0:8]
    # redirecting to dictionary
    d = dict(zipped_list)
    # printing out the questions with help from
    # https://realpython.com/iterate-through-dictionary-python/#iterating-through-items
    for key, values in d.items():
        print("* * * * * * * * * * * * * * * * * * * * * * * * *")
        print(key)

        while True:

            valid_inputs = ["a", "b", "c"]

            for i in values:
                print(i)
            guess = input("Enter (a, b or c): ")
            guess = guess.lower()

            if guess in valid_inputs:
                guesses.append(guess)

                correct_guesses += check_answer(
                    planet_questions.get(key), guess)
                question_num += 1
                break

            else:
                print("Invalid input, please enter a, b or c \n")

    display_score(correct_guesses, guesses)
    again = play_again()

    # If play_again returns True (player inputs yes when asked
    # "Do you want to play again? in the play_again function)
    # the new_game() function is called

    if again:
        new_game()


def check_answer(answer, guess):
    """
    Displays correst or wrong answer after every question
    (after the player has answered) in order to let the
    user see directly if the anser was correct or not.
    """

    if answer == guess:
        # If answer is correct, print correct in green color in order to make
        # it visable clear for the user
        # with help from https://gist.github.com/kamito/704813
        print("\033[0;32mCORRECT!\033[0m")
        return 1
    else:
        # if the answer is wrong, print wrong in red color
        print("\033[0;31mWRONG!\033[0m")
        return 0


def display_score(correct_guesses, guesses):
    """
    When the game is finished and all the question has
    been answered a display of scores shows in order to
    let the user see the answers compared to the right
    answers as well as the total score contained.
    """
    print("* * * * * * * * * * * * * * * * * * * * * * * * *")
    print("Your results:")
    print("Correct answers: ", end="")
    for i in planet_questions:
        print(planet_questions.get(i), end=" ")
    print()

    print("Your answers:    ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    # Prints out a number of stars according to number of scores
    stars = []
    j = 0
    while j < correct_guesses:
        stars.append("⭐")
        j += 1
    print(
        f"Good job, you scored: {correct_guesses} out of"
        f" 8 {''.join(stars)}"
    )

    check_score(correct_guesses, username)


def play_again():
    """
    Allows the player to chose to play again or quit the game.
    """

    response = input("Do you want to play again? (y/n): \n")
    response = response.lower()

    while response != "y" and response != "n":
        response = input("Invalid input! Do you want to play again? (y/n): \n")
        response = response.lower()

    if response == "y":
        return True
    elif response == "n":
        print("Thanks for playing!")
        return False


def check_score(correct_guesses, username):

    # Get the top_scores from the worksheet
    top_scores = SHEET.worksheet("top_scores")

    # add the username together with the score (correct_guesses)
    # to the spread sheet
    top_scores.append_row([username, correct_guesses])

    # get all values from the spread sheet
    top_scores_data = top_scores.get_all_values()

    # sort the values in the top_scores_data by the second value (=the score)
    # in reverse order
    top_scores_data.sort(key=lambda x: x[1], reverse=True)

    # take only the first 5 top values/highest scores from the sorted
    # top_scores_data
    top_scores_data = top_scores_data[0:5]

    print_top_scores = input(
        "Would you like to see the top 5 scores? (y/n): \n")
    print_top_scores = print_top_scores.lower()

    while print_top_scores != "y" and print_top_scores != "n":
        print_top_scores = input(
            "Invalid input! Would you like to see the top 5 scores? (y/n): \n"
        )
        print_top_scores = print_top_scores.lower()

    if print_top_scores == "y":
        # print the values in the top_scores_data
        # (now only containing the top 5 scores) in two columns
        # with username-score, to be make it easy to read
        # with help from #
        # https://stackoverflow.com/questions/13214809/pretty-print-2d-list/50257693#50257693
        print(
            "\n".join(
                ["\t".join(
                    [str(cell) for cell in row]
                    ) for row in top_scores_data]
                    )
            )

# https://realpython.com/if-name-main-python/


if __name__ == "__main__":
    SCOPE = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive.file",
        "https://www.googleapis.com/auth/drive",
    ]

    CREDS = Credentials.from_service_account_file("creds.json")
    SCOPED_CREDS = CREDS.with_scopes(SCOPE)
    GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
    SHEET = GSPREAD_CLIENT.open("planets-quiz")

    # Get data from google spread sheet
    questions = SHEET.worksheet("questions")
    question_data = questions.get_all_values()

    answers_a = SHEET.worksheet("answers_a")
    answer_a_data = answers_a.get_all_values()

    answers_b = SHEET.worksheet("answers_b")
    answer_b_data = answers_b.get_all_values()

    answers_c = SHEET.worksheet("answers_c")
    answer_c_data = answers_c.get_all_values()
    # Store questions from the spread sheet
    # with help from https://github.com/CI-Tom/pub-quiz-challenge
    planet_questions = {
        question_data[0][0]: "a",
        question_data[1][0]: "b",
        question_data[2][0]: "c",
        question_data[3][0]: "a",
        question_data[4][0]: "b",
        question_data[5][0]: "b",
        question_data[6][0]: "c",
        question_data[7][0]: "b",
        question_data[8][0]: "a",
        question_data[9][0]: "b",
        question_data[10][0]: "b",
        question_data[11][0]: "c",
        question_data[12][0]: "a",
        question_data[13][0]: "b",
    }

    options = [
        [answer_a_data[0][0], answer_b_data[0][0], answer_c_data[0][0]],
        [answer_a_data[1][0], answer_b_data[1][0], answer_c_data[1][0]],
        [answer_a_data[2][0], answer_b_data[2][0], answer_c_data[2][0]],
        [answer_a_data[3][0], answer_b_data[3][0], answer_c_data[3][0]],
        [answer_a_data[4][0], answer_b_data[4][0], answer_c_data[4][0]],
        [answer_a_data[5][0], answer_b_data[5][0], answer_c_data[5][0]],
        [answer_a_data[6][0], answer_b_data[6][0], answer_c_data[6][0]],
        [answer_a_data[7][0], answer_b_data[7][0], answer_c_data[7][0]],
        [answer_a_data[8][0], answer_b_data[8][0], answer_c_data[8][0]],
        [answer_a_data[9][0], answer_b_data[9][0], answer_c_data[9][0]],
        [answer_a_data[10][0], answer_b_data[10][0], answer_c_data[10][0]],
        [answer_a_data[11][0], answer_b_data[11][0], answer_c_data[11][0]],
        [answer_a_data[12][0], answer_b_data[12][0], answer_c_data[12][0]],
        [answer_a_data[13][0], answer_b_data[13][0], answer_c_data[13][0]], ]
    start_game()
