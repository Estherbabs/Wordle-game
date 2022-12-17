import random
lives = 3


# create a list of secret words which the user needs to guess
words = ['happy', 'gracious', 'javascript',
         'python', 'wealth', 'command',
         'consult', 'fulfil', 'computer',
         'unlock', 'career', 'hope']


# The random module choice function is used here
# This will enable users to randomly pick a word
secret_word = random.choice(words)


# Another list has been created here to store the clues
clue = list('?????')
heart_symbol = u'\u2764'

guessed_word_correctly = False


# This defines the beginning of the game which includes
# the game name, instructions and introduction
# the website below is an ASCII website to design the name of
# the game and also the word 'Game over'
class game:
    def start_game():
        """
         https://patorjk.com/software/taag/#p=display&f=Graceful&t=Wordle%20game
        """
        print("""
        _  _   __  ____  ____  __    ____     ___   __   _  _  ____
       / )( \ /  \(  _ \(    \(  )  (  __)   / __) / _\ ( \/ )(  __)
       \ /\ /(  O ))   / ) D (/ (_/\ ) _)   ( (_ \/    \/ \/ \ ) _)
       (_/\_) \__/(__\_)(____/\____/(____)   \___/\_/\_/\_)(_/(____)

       To play this game, player needs to guess the secret word or letter
       and if guessed correctly user wins, if word or letter is guessed wrongly
       user loses. Please see instruction below. Enjoy!

      Instruction:
      1. Wordle is a single player game.
      2. Please note you have 3 lives.
      3. Please input your username and it must be more than 3 characters.
      """)

    print(f"Welcome to Wordle game!!!")

    start_game()

# This function is to make the user enter name and also validate it
# if name is less than 3 words, it wouldnt make the user go further
# until the name is more than 3 words


def get_player_name():
    print()

    while True:
        global PlayerName
        PlayerName = input('Please enter your name: ')

        if len(PlayerName) > 3:
            break
        print("Your name is too short! :c")

    print()
    return PlayerName


get_player_name()


# a function has been created here for the clue list to be updated
def update_clue(guessed_letter, secret_word, clue):
    index = 0
    while index < len(secret_word):
        if guessed_letter == secret_word[index]:
            clue[index] = guessed_letter
        index += 1


def validate_word(word):
    print()
    while len(word) < 1:
        words = input('invalid word: Please enter a word: ')
        print()
    return True
# The function as for user to input the guessed letter or word


while lives > 0:
    print(clue)
    print('You have ' + str(heart_symbol * lives) + ' lives remaining')
    guess = input('Guess a letter or the whole word: ')
    validate_word(guess)
    if guess == secret_word:
        guessed_word_correctly = True
        break
    if guess in secret_word:
        update_clue(guess, secret_word, clue)
    else:
        print('Sorry,' + PlayerName + ' ' + ' that letter in not in the word. You lost a life')
        lives -= 1

# check if the player has won or lost

if guessed_word_correctly:
    print(PlayerName + ' You guessed the word! You win! ➕ ' + secret_word)
else:
    print('Sorry, you lost  ❌. The word was ' + secret_word)


# This function indicates the end of the wordle game
# after the user's lives are exhausted
# This function also gives the users
# the option to play again or exit the game

if lives == 0:
    print("""
      _______  _______  _______  _______    _______           _______  _______
     (  ____ \(  ___  )(       )(  ____ \  (  ___  )|\     /|(  ____ \(  ____ )
     | (    \/| (   ) || () () || (    \/  | (   ) || )   ( || (    \/| (    )|
     | |      | (___) || || || || (__      | |   | || |   | || (__    | (____)|
     | | ____ |  ___  || |(_)| ||  __)     | |   | |( (   ) )|  __)   |     __)
     | | \_  )| (   ) || |   | || (        | |   | | \ \_/ / | (      | (\ (
     | (___) || )   ( || )   ( || (____/\  | (___) |  \   /  | (____/\| ) \ \__
     (_______)|/     \||/     \|(_______/  (_______)   \_/   (_______/|/   \__/


""")

