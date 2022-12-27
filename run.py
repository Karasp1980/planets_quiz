"""
Import required modules
"""

import gspread

from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('planets-quiz')

# Get data from google spread sheet 
questions = SHEET.worksheet('questions')
question_data = questions.get_all_values()


answers_a = SHEET.worksheet('answers_a')
answer_a_data = answers_a.get_all_values()

answers_b = SHEET.worksheet('answers_b')
answer_b_data = answers_b.get_all_values()

answers_c = SHEET.worksheet('answers_c')
answer_c_data = answers_c.get_all_values()



def start_game():
    """
    Allow player to enter name and start quiz.
    """
    print("⭐⭐⭐⭐⭐ Welcome to Our Planets quiz! ⭐⭐⭐⭐⭐")
  
    player_name = input("Please enter your username: \n")

    while player_name == "":
        print("A username is required to start the quiz, please try again.")
        player_name = input("Please enter your username: \n")

    # Capitalizes the first letter in the name in case
    # user enteres only lowercase letters
    player_name = player_name.capitalize()
    start = input(f"Hi {player_name} and welcome! Would you like to start the game? (y/n) \n")
    start = start.lower()

    # Check that the input value is valid (y or n)
    while start != 'y' and start != 'n':
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

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in planet_questions:
        print("* * * * * * * * * * * * * * * * * * * * * * * * *")
        print(key)
        
        while True:
        
            valid_inputs = ["a", "b", "c"]

            for i in options[question_num-1]:
                print(i)
            guess = input("Enter (a, b or c): ")
            guess = guess.lower()
                
            if guess in valid_inputs:
                guesses.append(guess)

                correct_guesses += check_answer(planet_questions.get(key), guess)
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
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
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
    print("Answers: ", end="")
    for i in planet_questions:
        print(planet_questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    # Prints out a number of stars according to number of scores
    stars = []
    j = 0
    while j < correct_guesses:
        stars.append("⭐")
        j += 1   
  
    print(f"Good job, you scored: {correct_guesses} out of {len(planet_questions)} {''.join(stars)}")

def play_again():
    """
    Allows the player to chose to play again or quit the game.
    """

    response = input("Do you want to play again? (y/n): \n")
    response = response.lower()

    while response != 'y' and response != 'n':
            response = input("Invalid input! Do you want to play again? (y/n): \n")
            response = response.lower()

    if response == "y":
        return True
    elif response == "n":
        print("Thanks for playing!")
        return False 


planet_questions = {
    question_data[0][0]: "a",
    question_data[1][0]: "b",
    question_data[2][0]: "c",
    question_data[3][0]: "a",
    question_data[4][0]: "b",
    question_data[5][0]: "b",
    question_data[6][0]: "c",
    question_data[7][0]: "b",
}

# Create lists with embedded lists of possible answers from worksheet
options = [
    [answer_a_data[0][0], answer_b_data[1][0], answer_c_data[1][0]],
    [answer_a_data[1][0], answer_b_data[1][0], answer_c_data[1][0]],
    [answer_a_data[2][0], answer_b_data[2][0], answer_c_data[2][0]],
    [answer_a_data[3][0], answer_b_data[3][0], answer_c_data[3][0]],
    [answer_a_data[4][0], answer_b_data[4][0], answer_c_data[4][0]],
    [answer_a_data[5][0], answer_b_data[5][0], answer_c_data[5][0]],
    [answer_a_data[6][0], answer_b_data[6][0], answer_c_data[6][0]],
    [answer_a_data[7][0], answer_b_data[7][0], answer_c_data[7][0]]
]


start_game()


