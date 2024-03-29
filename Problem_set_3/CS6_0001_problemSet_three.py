# 6.0001 Problem Set 3
#
# Name          : Taylor Jackson
# Collaborators : Palash Sharma, James Black
# Time spent    : 7

import math
import random

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7


def SCRABBLE_LETTER_VALUES(letter):
    values = {
        'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1,
        'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10, '*': 1
    }
    return values[letter]


# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

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
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.
    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x, 0) + 1
    return freq


# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    You may assume that the input word is always either a string of letters,
    or the empty string "". You may not assume that the string will only contain
    lowercase letters, so you will have to handle uppercase and mixed case strings
    appropriately.
	The score for a word is the product of two components:
	The first component is the sum of the points for letters in the word.
	The second component is the largest of:
    1, or
    7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
    and n is the hand length when the word was played
	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.
    word: string
    n: int >= 0
    returns: int >= 0
    """
    A, B = 0, 0
    for char in word.lower():
        if char != "":
            A += SCRABBLE_LETTER_VALUES(char)
    B = (7 * len(word)) - (3 * (n - len(word)))
    if 0 < B < 1:
        B = 1
    elif B < 0:
        B = 0
    return A + B


#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    string = ""
    for letter in hand.keys():
        for j in range(hand[letter]):
            string += f"{letter} "
    return string


#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3) - 1 to account for the wild card.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """

    hand = {'*': 1}
    num_vowels = int(math.ceil(n / 3))

    for i in range(num_vowels - 1):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1

    for i in range(num_vowels, n):
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1

    return hand


#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Does NOT assume that hand contains every char in word at least as
    many times as the char appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the char from the
    dictionary, depending on how your code is structured).

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)
    returns: dictionary (string -> int)
    """
    hand_copy = hand.copy()
    char_dict = get_frequency_dict(word.lower())

    for char in hand_copy:
        if char in char_dict:
            hand_copy[char] -= char_dict[char]

    hand_copy_b = hand_copy.copy()
    for char in hand_copy_b:
        if hand_copy_b[char] <= 0:
            del hand_copy[char]

    return hand_copy


#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, wordList):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.

    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """
    char_dict = get_frequency_dict(word.lower())
    list_word = list(word)

    if word.lower() in wordList:
        # Valid Entree Procedure
        for char in word.lower():
            if char not in hand:
                return False
            else:
                if char_dict[char] > hand[char]:
                    return False
        return True

    else:
        # Check for Wildcard use
        i = 0
        for char in word:
            if char == '*':
                for v in VOWELS:
                    list_word[i] = v
                    word = ''.join(list_word)
                    if word.lower() in wordList:
                        return True
            i += 1
        return False


#
# Problem #5: Playing a hand
#
def calculate_handlen(hand):
    """
    Returns the length (number of letters) in the current hand.

    hand: dictionary (string-> int)
    returns: integer
    """
    return sum(char for char in hand.values())


def play_hand(hand, wordList):
    """
    Allows the user to play the given hand, as follows:
    * The hand is displayed.
    * The user may input a word.
    * When any word is entered (valid or invalid), it uses up letters
      from the hand.
    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand

    """
    # Keep track of the total score
    score = 0
    word = ""
    Run_game = True
    while Run_game:

        # Ask user for input
        # If the input is two exclamation points:
        # End the game (break out of the loop)
        word = input("Please enter a word ")
        if word == "!!":
            Run_game = False
            break
        # Otherwise (the input is not two exclamation points):
        else:
            # If the word is valid:
            # Tell the user how many points the word earned,
            # and the updated total score
            if is_valid_word(word, hand, wordList):
                print(f"This word got a score of {get_word_score(word, calculate_handlen(hand))} congrats!")
                score += get_word_score(word, calculate_handlen(hand))
                return score
            # Otherwise (the word is not valid):
            # Reject invalid word (print a message)
            else:
                print(f"!Rejected Invalid Word! \\ Please pick another word")

        # update the user's hand by removing the letters of their inputted word
        update_hand(hand, word)

    # Game is over (user entered '!!' or ran out of letters),
    # so tell user the total score
    # Return the total score as result of function
    if word == "!!":
        print(f"You got a Total Score of {score} congrats")
        return score
    elif calculate_handlen(hand) <= 0:
        print(f"You ran out of letters! Total Score: {score}")
        return score


#
# Problem #6: Playing a game
#


#
# procedure you will use to substitute a letter in a hand
#

def substitute_hand(hand, letter):
    """
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.

    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """

    hand_copy = hand.copy()
    change = ''
    choice = random.choice('vc')
    if choice == 'v':
        change = random.choice(VOWELS)
        while change in hand:
            change = random.choice(VOWELS)
    else:
        change = random.choice(CONSONANTS)
        while change in hand:
            change = random.choice(CONSONANTS)

    val = hand[letter]
    del (hand_copy[letter])
    hand_copy[change] = val

    return hand_copy


def play_game(wordList):
    """
    Allow the user to play a series of hands
    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the
      entire series

    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep
      the better of the two scores for that hand.  This can only be done once
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.

    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """
    # Bound Variables
    hand_num = int(input("How many hand do you want to play? "))
    Sub = True
    a, b, score, score1 = 0, 0, 0, 0
    total_score = [0]
    # Start of Function
    while hand_num > 0:
        hand = deal_hand(HAND_SIZE)
        print("Current Hand: ")
        print(display_hand(hand))

        if a == 0 and b != 1:
            # One time chance to substitute
            sub = input("Would you like to substitute a letter? Yes or No: ").lower()
            if sub == 'yes':
                hand = substitute_hand(hand, input("Which letter would you like to replace: "))
                a += 1
        print(hand)
        score = play_hand(hand, wordList)

        # procedure for matching scores if hand is replayed
        if b == 1:
            if score > score1:
                total_score += [score]
            else:
                total_score += score1
            b = 2
            hand_num -= 1

        # checking if user wants to replay
        if b == 0:
            replay = input("Would you like to replay the hand? ")
            replay = replay.lower()
            if replay == 'yes':
                score1 = [score]
                b = 1
            else:
                hand_num -= 1
                total_score += [score]
                b += 1

        if b == 2:
            hand_num += 1
    print(f"Total score over all hands is: {sum(x for x in total_score)}")


if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)