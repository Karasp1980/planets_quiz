
![Planets Quiz game](/assets/images/solar-system.png)

# Welcome to Our Planets Quiz game!
#### This game, made for the Code Institute third project, is designed in order to play a quiz game about the Planets in our solar system! The quiz contains 8 questions with a, b or c answers.

#### [Deployed site](https://planet-quiz-game.herokuapp.com/)
------

# Table of Contents
+ [Responsove](#responsive)
+ [Flowchart](#flowchart)
+ [Style/design](#style-design)
+ [Features](#features)
  + [Welcome section](#welcome-section)
  + [Questions](#questions)
  + [Display results](#display-results)
  + [Printing top 5 scores](#printing-top-scores)
+ [Testing](#testing)
  + [Ufixed bugs](#unfixed-bugs)
+ [Solved issues](#solved-issues) 
+ [Validator testing](#validator-testing)
  + [Python](#python)
+ [Ufixed bugs](#unfixed-bugs)
+ [Solved issues](#solved-issues)  
+ [Deployment](#deployment)  
+ [Media](#media)  
+ [Credits](#credits)  

-----


## Flowchart

#### Wireframes were made by using [Lucidchart](https://lucid.app/)
![Flowchart](/assets/images/flowchart.png)





------
## Style/design

### The game is designed with a simple terminal game design to make the game easy to play. The correct/wrong answers are displayed in green/red color to make that pop to the user. A background image with the planets was added to make the game more visiable appealing and also enhance the theme of the quiz. 
### The background image was taken from [Istockphoto](https://www.istockphoto.com/en/photo/solar-system-gm482954331-13391001?phrase=solar%20system)


----

## Features

### Welcome section
#### When starting the game a welcome section is displayed, and the user is asked to enter their username (the username can not be an empty string, in that case an Invalid input message show and the user is asked to enter username again). When username is entered the user is asked the question "Do you want to start the game?, and must input y (yes) or no (n) (in case any other letter is entered an Invalid input message accure and the user is asked to enter y or n again). If the user enters no (n) the game is closed, but if the input is yes the game starts and the questions start.


### Questions
#### When the game starts the questions are displayed and the user is provided with 3 choices and is asked to answer a, b or c (in case any other letter is entered an Invalid input message accure and the user is asked to enter a, b or c again). When the answer is entered correct or wrong is displayed (in green or red) to let the user see directly if the answer was correct or not. The game contains 8 questions and the questions and ansewer_a, answer_b and answer_c options are stored in a google sheet. So it is easy if you would like to alter the questions.

### Displaying results
#### When all 8 questions are answered the scores are displayed. First a row with the answered alternatives from the user, then a row with the correct alternatives, and finally the total score. Good job, you scored: x out of y (8) followed by number of stars according to the number of correct answers in order to make it more visiable for the user. This score (connected to the username) is then stored in the google sheet in the top_scores file.

### Printing top 5 scores
#### When the scores have been displayed the user is asked if they want to print the top 5 scores. If the user enters no (n) the game is closed and the user is asked if they want to play again, but if the input is yes the top 5 scores are printed in two columns to let the user see if their result is in the top five scores. Unfortunately the row might be altered a bit to the right if the username is too long, but found no better way to print in columns and in most cases the username is not to long to fit. The user is then asked the question if they want to play again or not. If not, a good bye message appear and the game is closed. All inputs are checked for valid input.


-------
## Testing

#### I tested that the site worked in different browsers: Google Chrome, Firefox, Edge

#### I confirmed that this projectfunctions on all standard screen sizes using the devtools device toolbar. The site has been tested on different physical devices: desktop, laptop, tablet and mobile.

#### I confirmed that the game is readable and easy to understand and all the game functions are working.

### Testing during development
* Tested that the data was gotten as expected from the google sheet "planets-quiz" by printing out data from the spreadsheet and also adding data from run.py to the spreadsheet. The data was added as expected.

![Test getting data from google sheets](/assets/images/test-print-add-data.png)
![Test getting data into google sheets](/assets/images/test-print-add-data-google-sheets.png)

* Tested that the input is valid for all the inputs, otherwise ask the user to enter a valid input.
![First input](/assets/images/validInput1.png)
![Second input](/assets/images/validInput2.png)
![Third input](/assets/images/validInput3.png)
![Fourth input](/assets/images/validInput4.png)

* Tested that the correct_guesses together with the username is printed to the spreadsheet when a game is over
![Print to the top_scores google sheet](/assets/images/test-top-scores.png)

------

## Validator testing

### Python:
#### No errors were returned when passed through the Pep8 validator
[Pep8 validator](https://pep8ci.herokuapp.com/)

![W3 validator]()

-----

## Unfixed bugs

#### No unfixed bugs.

## Solved issues
* When a game is over and the player gets the question "Do yo want to play again?" we want the game to restart and keep doing that as long as the player inputs yes (y) when asked the question. Therefore a while loop (with the condition while play_again() is True, call new_game() ) was added to the end of the new_game() function (after the scores have been displayed). But then the user got that question "Do yoy want to play again?" two times if answering no (n) to the question when having played more than one time. In order to fix that an if statement was used instead.
![Bug 1](/assets/images/bug1.png)


-----

## Deployment

#### This project was deployed to [Heroku](https://www.heroku.com/) using Code Institute's mock terminal.

   - Steps

     - Go to Heroku and click on the new button at the top right of the page. Select create new app from the dropdown menu.

     - Enter a name, change region to Europe and click create app.

     - Go to settings and select Config Vars

     - Locate Buildpacks and add Python and NodeJS in that order.

     - Add a new Config Var with a keyword of PORT and a value of 8000

     - Exit settings and click Deploy. Select GitHub from the deploy options.

     - Select your repository and connect it to Heroku.

     - Click Enable Automatic Deploys in the automatic deploys section or make sure main branch is selected and click Deploy Branch in the manual deploy section.

     - The live version of the app can be found here [Deployed site](https://planet-quiz-game.herokuapp.com/)


-----

## Credits

#### The 
#### Inspiration and help has also come from the Code Institute projects [Love Sandwiches](https://github.com/Karasp1980/love_sandwiches).

#### The following sites has also been helpful:
* [W3Schools](https://www.w3schools.com/) 
* [Bro Code](https://www.youtube.com/watch?v=yriw5Zh406s) 
* [Wikipedia](https://www.wikipedia.org) 
* [Stackoverflow](https://stackoverflow.com/questions/13214809/pretty-print-2d-list/50257693#50257693)
* [CI Tom - Pub Quiz](https://github.com/CI-Tom/pub-quiz-challenge)
* [ANSI colors](https://gist.github.com/kamito/704813)
* [If name main](https://realpython.com/if-name-main-python/)