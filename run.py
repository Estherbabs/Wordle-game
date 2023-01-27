import random
# This defines the beginning of the game which includes
# the game name, instructions and introduction
# the website below is an ASCII website to design the name of
# the game and also the word 'Game over'


class game(object):
    def __init__(self):
        self.lives = 3

        # create a list of secret words which the user needs to guess

        self.words = ['happy', 'gracious', 'javascript',
                      'python', 'wealth', 'command',
                      'consult', 'fulfil', 'computer',
                      'unlock', 'career', 'hope']

        # The random module choice function is used here
        # This will enable users to randomly pick a word

        self.secret_word = random.choice(self.words)

        # Another list has been created here to store the clues

        self.clue = list('?????')
        self.heart_symbol = u'\u2764'
        self.guessed_word_correctly = False
        self.PlayerName = None

    def start_game(self):
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
        self.set_player_name()
        self.play()

    # This function is to make the user enter name and also validate it
    # if name is less than 3 words, it wouldnt make the user go further
    # until the name is more than 3 words

    def set_player_name(self):
        print()
        while True:
            self.PlayerName = input('Please enter your name: ')
            if len(self.PlayerName) > 3:
                break
            print("Your name is too short! :c")

    # a function has been created here for the clue list to be updated

    def update_clue(self, guessed_letter, secret_word):
        index = 0
        while index < len(secret_word):
            if guessed_letter == secret_word[index]:
                self.clue[index] = guessed_letter
            index += 1

    def validate_word(self, word):
        print()
        while len(word) < 1:
            word = input('invalid word: Please enter a word: ')
            print()
        return word

# The function as for user to input the guessed letter or word

    def play(self):
        while self.lives > 0:
            print(self.clue)
            print(" You have " + str(self.heart_symbol * self.lives) + " lives remaining")
            guess = input('Guess a letter or the whole word: ')
            if guess in ["*", ".", ",", "!", "?", "@", "(", ")", ";", ":", " "]:
                print("Please input a valid letter or word")
                continue
            guess = self.validate_word(guess)
            if guess == self.secret_word:
                self.guessed_word_correctly = True
                break
            if guess in self.secret_word:
                self.update_clue(guess, self.secret_word)
            else:
                print('Sorry,' + self.PlayerName + ' ' + ' that letter is in not in the word. You lost a life')
                self.lives -= 1

        # check if the player has won or lost

        if self.guessed_word_correctly:
            print(self.PlayerName + ' You guessed the word! You win! ➕ ' + self.secret_word)
        else:
            print('Sorry, you lost  ❌. The word was ' + self.secret_word)

        # This function indicates the end of the wordle game
        # after the user's lives are exhausted
        # This function also gives the users
        # the option to play again or exit the game

        if self.lives == 0:
            print("""
               ___   __   _  _ ____     __  _  _ ____ ____ 
              / __) / _\ ( \/ |  __)   /  \/ )( (  __|  __/
             ( (_ \/    \/ \/ \) _)   (  O ) \/ /) _) )   /
              \___/\_/\_/\_)(_(____)   \__/ \__/(____|__\_)
 
              """)


if __name__ == '__main__':
    while True:

        g = game()
        g.start_game()
        while True:
            answer = str(input('Run again?(y/n)')).strip()
            if answer in ("y", "n"):
                break
            print("invalid input")
        if answer == "n":
            print("Goodbye")
            # break
            exit(0)