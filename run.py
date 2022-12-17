def start_game():
    """
    Allow player to enter name and start quiz.
    """
    print("⭐⭐⭐⭐⭐ Welcome to Nordic Mythology Quiz! ⭐⭐⭐⭐⭐")
    player = input("Please enter your name: \n")
    player = player.capitalize()

    start=input(f"Hi {player} and welcome! Would you like to start the game? (y/n) \n")
    if start=="y":

        print("Lets start the game!⭐ \n")

    elif start=="n":
        print("Thanks for playing, welcome back next time! \n") 
        return start_game()
    else:
        print("Invalid input! Would you like to start the game? (y/n) \n")     

start_game() 