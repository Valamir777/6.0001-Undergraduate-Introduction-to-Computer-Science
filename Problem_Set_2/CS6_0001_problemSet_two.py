import random

# Problem Set 2, hangman.py
# Name: Taylor jackson
# Collaborators: Deez
# Time spent: 5hrs

# Hangman Game
# Match with gaps does not work correctly

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


def is_word_guessed(secret_word, letters_guessed):
    """
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    """

    for char in secret_word:
        if char not in letters_guessed:
            return False
            # returning False if a character from secret_word is not in letters_guessed

    return True  # returning true otherwise


def get_guessed_word(secret_word, letters_guessed):
    """
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    """
    guessed = ''
    for char in secret_word:
        if char in letters_guessed:
            guessed += f"{char} "
        else:
            guessed += "_"
    return guessed


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    alphabet = list(map(chr, range(ord('a'), ord('z') + 1)))
    for char in alphabet:
        if char in letters_guessed:
            alphabet.remove(char)

    return alphabet


def hangman(secret_word):
    """
    secret_word: string, the secret word to guess.
    Starts up an interactive game of Hangman.
    """
    global guessed_letter
    letters_guessed = ["", ]
    guess = 6
    print("let's play a game")
    print(f"I'm thinking of a word that is {int(len(secret_word))} letters long;)")
    print(f"You will have {guess} guesses until you are terminated...")

    while not is_word_guessed(secret_word, letters_guessed):
        gameRound = True

        while gameRound:
            print(f"you have {guess} guesses left!")
            print(get_available_letters(letters_guessed))
            guessed_letter = input("Please enter an alphabetic character ").lower()
            if guessed_letter in list(map(chr, range(97, 123))):
                if guessed_letter not in letters_guessed:
                    letters_guessed += guessed_letter
                    letters_guessed.sort()
                    gameRound = False
                else:
                    print("You have already guessed this letter")
            else:
                print("This is an invalid Entry try again")
        for char in secret_word:
            if guessed_letter == char:
                print(f"The letter {guessed_letter} is in the secret word")
                guess -= 1
                break
            else:
                print(f"The letter {guessed_letter} is not in the secret word")
                guess -= 1
                break
        print(get_guessed_word(secret_word, letters_guessed))
        if guess == 0:
            print("you are out of guesses")
            break
    if is_word_guessed(secret_word, letters_guessed):
        print(f"you guessed that {secret_word} was the secret word")


# -----------------------------------


def match_with_gaps(my_word, other_word):
    """
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    """
    if len(my_word) != len(other_word):
        return False
    for i, char in enumerate(my_word):
        if char != '_' or other_word[i]:
            return False

    return True


def show_possible_matches(my_word):
    """
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.
    """
    f = 0
    for other_word in load_words():
        if match_with_gaps(my_word, other_word):
            f = 1
            print(other_word)

    if f == 0:
        print("No matches found")


def hangman_with_hints(secret_word):
    """
    secret_word: string, the secret word to guess.
    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word.

    Follows the other limitations detailed in the problem write-up.
    """
    global guessed_letter
    letters_guessed = ["", " ", "_"]
    guess = 6
    entry_error = 3
    print("let's play a game")
    print(f"I'm thinking of a word that is {int(len(secret_word))} letters long;)")
    print(f"You will have {guess} guesses until you are terminated...")

    while not is_word_guessed(secret_word, letters_guessed):
        gameRound = True

        while gameRound:
            print(f"you have {guess} guesses left!")
            print(get_available_letters(letters_guessed))
            guessed_letter = input("Please enter an alphabetic character ").lower()

            if guessed_letter == '*':
                show_possible_matches(get_guessed_word(secret_word, letters_guessed))
                break

            elif guessed_letter not in list(map(chr, range(ord('a'), ord('z') + 1))):
                if entry_error >= 1:
                    entry_error -= 1
                    print('That is not a valid input. You have ' +
                          str(entry_error) + ' warnings left: ' + get_guessed_word(secret_word, letters_guessed))
                    break

            if guessed_letter not in letters_guessed:
                letters_guessed += guessed_letter
                letters_guessed.sort()
                gameRound = False
            else:
                print("You have already guessed this letter")

            for char in secret_word:
                if guessed_letter == char:
                    print(f"The letter {guessed_letter} is in the secret word")
                    guess -= 1
                    break
                else:
                    print(f"The letter {guessed_letter} is not in the secret word")
                    guess -= 1
                    break
        print(get_guessed_word(secret_word, letters_guessed))
        if guess == 0:
            print("you are out of guesses")
            break
    if is_word_guessed(secret_word, letters_guessed):
        print(f"you guessed that {str(secret_word)} was the secret word")


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.
###############

class hangman_game:
    # secret_word = choose_word(load_words())
    secret_word = "ad"
    # hangman(secret_word)
    hangman_with_hints(secret_word)