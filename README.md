# WORDLE GAME
Wordle game is a python terminal and a single player game which runs on Heroku.
Players can guess the letter or secret word. If guessed corrently the user wins if guessed
wrongly the user loses.

See my deployed wordle game in Heroku below:

![Screenshot 2022-12-17 at 06 25 42](https://user-images.githubusercontent.com/108898698/208228728-50ecf19c-13aa-43ad-bcd8-0591ed3a8b0e.png)

***

## HOW TO PLAY
Wordle is a web based game, created and developed by Josh Wardle, See [Wikipedia] (https://en.m.wikipedia.org/wiki/Wordle)
In this version, the player enters their name and the game is randomly generated.
The player can guess the letter or the secret word, if the player guesses right, they win. If
the player guesses wrong they lose and the guessed word is prompted on the screen.

***
## FEATURES
***
### EXISTING FEATURES
- __User login__
- The user is prompted to input name to start game.
- The name must be more than 3 words.

![Screenshot 2022-12-17 at 06 50 30](https://user-images.githubusercontent.com/108898698/208229608-a5862680-63bf-44ab-946f-c1de52a12c5b.png)

- __Accepts User-input__
- __Shows amount of lives__

![Screenshot 2022-12-17 at 06 56 29](https://user-images.githubusercontent.com/108898698/208229812-abee9ffd-3b15-4fd4-9851-80820b22cae4.png)

- __Shows win or lose__

![Screenshot 2022-12-17 at 07 08 58](https://user-images.githubusercontent.com/108898698/208230295-a1f27c84-c8e9-44dd-9ae1-5960c83a5d26.png)

***

### FUTURE FEATURES
- Show clues of letter in the secret word.
 
***

## DATA MODEL
I decided to use a game class as my model. The game class stores the name of the game,
how to play the game, instruction and user name input.
The class has method to help play the game such print method to print out the current board, 
***

## TESTING
***
I have manually tested this project by doing the following:

- Passed the code through a PEP8 linter and confirmed there are no significant problems
- Tested severally in my local terminal and also Heroku terminal.

***
## BUGS
- At first I struggled with invalid syntax because I put one = instead of double == I was able to
figure it out eventually.
- My code was giving some errors when I try to add the restart code, but eventually fixed it by wraping my code with the game class.

### Remaining Bugs
- No bugs remaining
***

### Validator testing
- PEP8
- No significant error was returned, except invalid escape sequence which is as a result
of ASCII in my code.

***
## Deployment

This project was deployed using Heroku.

- Steps for deployment
- Fork or clone this repository
- Create a new Heroku app
- Set the buildbacks to python and NodeJS in that order
- click on Deploy

***
## Credits
- Code Institute for Readme Sample
- ACSII design for the name of the game (Wordle game and Game over) [patorjk] (https://patorjk.com/software/taag/#p=display&f=Graceful&t=Wordle%20game)
