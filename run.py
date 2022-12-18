def start_game():
    """
    Allow player to enter name and start quiz.
    """
    print("⭐⭐⭐⭐⭐ Welcome to the Quiz game! ⭐⭐⭐⭐⭐")
    player_name = input("Please enter your name: \n")
    
    if player_name=="":
        print("A name is required to start the quiz, please try again.")
        start_game()

    else:
        # Capiralizes the first letter in the name in case user enteres only lowercase letters
        player_name = player_name.capitalize()  

        start=input(f"Hi {player_name} and welcome! Would you like to start the game? (y/n) \n")

        if start=="y":
            print("Lets start the game!⭐ \n")
            new_game()



        elif start=="n":
            print("Welcome back next time, bye! \n") 
            return start_game()
        else:
            print("Invalid input! Would you like to start the game? (y/n) \n")     

def new_game():
    """
    Creates a new game and starts the game and starts displaying questions.
    """

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("*****************")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (a, b or c): ")
        guess = guess.lower()

        if guess=="a" or guess=="b" or guess=="c":

            guesses.append(guess)

            correct_guesses += check_answer(questions.get(key), guess)
            question_num += 1
        else: 
            print("Invalid input! Please answer a, b or c")
            start_game()
             

    display_score(correct_guesses, guesses)

# -------------------------
def check_answer(answer, guess):
    """
    Displays correst or wrong answer after every question after the player has answered to let the 
    user see if the anser was correct.
    """

    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0

# -------------------------
def display_score(correct_guesses, guesses):
    """
    When the game is finished and all the question has been answered a display  
    of scores shows in order to let the user see the answers compared to the right
    answers as well as the total score contained.
    """
    print("*****************")
    print("Your results:")
   

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    #score = int((correct_guesses/len(questions))*100)
    #print("Your score is: "+str(score)+"%")
    print(f"Good job, you scored: {correct_guesses} out of {len(questions)}")

# -------------------------
def play_again():
    """
    Allows the player to chose to play again or quit the game.
    """

    response = input("Do you want to play again? (y/n): ")
    response = response.lower()

    if response == "y":
        return True
    else:
        return False
# -------------------------


questions = {
 "⭐ Who created Python?: ": "a",
 "⭐ What year was Python created?: ": "b",
 "⭐ Python is tributed to which comedy group?: ": "c",
 "⭐ Is the Earth round?: ": "a",
 "⭐ What is the capital of Sweden: ": "a",
 "⭐ What year was the moon land: ": "b",
 "⭐ What creature is said to sit in a stream and suduce people to drown with his violon playing?: ": "c",
 "⭐ What is the capital of Finland?: ": "a"
}

options = [
          ["a. Guido van Rossum", "b. Elon Musk", "c. Bill Gates"],
          ["a. 1989", "b. 1991", "c. 2000"],
          ["a. Lonely Island", "b. Smosh", "c. Monty Python"],
          ["a. True","b. False", "c. sometimes"],
          ["a. Stockholm", "b. Kopenhagen", "c. Helsinki"],
          ["a. 1989", "b. 1969", "c. 1949", "d. 1972"],
          ["a. Santa", "b. Elf", "c. The neck"],
          ["a. Helsinki", "b. Reykjavik", "c. Lund"]
          ]

start_game()

while play_again():
    new_game()

print("Thanks for playing!")