
![Planets Quiz game](/assets/images/solar-system.jpg)

# Welcome to Planets Quiz game!
#### This game is designed in order to play a quiz game about the Planets in our solar system! 

#### [Deployed site]()
------

# Table of Contents
+ [Responsove](#responsive)
+ [Flowchart](#flowchart)
+ [Style/design](#style-design)
+ [Features](#features)
  + [](#)
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

## Responsive

#### The 
----


## Flowchart

#### Wireframes were made by using [Lucidchart](https://lucid.app/)




------
## Style/design





----

## Features


### **Tim



-------
## Testing

#### I tested that the site worked in different browsers: Google Chrome, Firefox, Edge

#### I confirmed that this projectfunctions on all standard screen sizes using the devtools device toolbar. The site has been tested on different physical devices: desktop, laptop, tablet and mobile.

#### I confirmed that the game is readable and easy to understand and all the game functions are working.

### Testing during development
* Tested that the data was gotten as expected from the google sheet "planets-quiz" by printing out data from the spreadsheet and also adding data from run.py to the spreadsheet. The data was added as expected.S

![Test getting data from google sheets](/assets/images/test-print-add-data.png)
![Test getting data from google sheets](/assets/images/test-print-add-data-google-sheets.png)

* Tested that the input is valid for all the inputs, otherwise ask the user to enter a valid input.
![First input](/assets/images/validInput1.png)
![Second input](/assets/images/validInput2.png)
![Third input](/assets/images/validInput3.png)
![Fourth input](/assets/images/validInput4.png)


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

     - The live version of the app can be found here [Deployed site]()


-----

## Credits

#### The 
#### Inspiration and help has also come from the Code Institute projects [Love Sandwiches](https://github.com/Karasp1980/love_sandwiches).

#### The following sites has also been helpful:
* [W3Schools](https://www.w3schools.com/) 
* [Bro Code](https://www.youtube.com/watch?v=yriw5Zh406s) 
* [Wikipedia](https://www.wikipedia.org) 
*
* 
