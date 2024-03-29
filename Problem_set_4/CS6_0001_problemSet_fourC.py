# Problem Set 4C
# Name: Taylor B. Schaefer-Jackson
# Time Spent: 2:30::00

from ps4a import get_permutations
import string


### HELPER CODE ###
def load_words(file_name):
    """
    file_name (string): the name of the file containing
    the list of words to load

    Returns: a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """

    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    return wordlist


def is_word(word_list, word):
    """
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.

    Returns: True if word is in word_list, False otherwise

    Example:
    #>>> is_word(word_list, 'bat') returns
    True
    #>>> is_word(word_list, 'asdf') returns
    False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list


### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

# you may find these constants helpful
VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'


class SubMessage(object):
    def __init__(self, text):
        """
        Initializes a SubMessage object

        text (string): the message's text

        A SubMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        """
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    def get_message_text(self):
        """
        Used to safely access self.message_text outside the class

        Returns: self.message_text
        """
        return self.message_text

    def get_valid_words(self):
        """
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.

        Returns: a COPY of self.valid_words
        """
        return self.valid_words[:]

    def build_transpose_dict(self, vowels_permutation):
        """
        vowels_permutation (string): a string containing a permutation of vowels (a, e, i, o, u)

        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to an
        uppercase and lowercase letter, respectively. Vowels are shuffled
        according to vowels_permutation. The first letter in vowels_permutation
        corresponds to a, the second to e, and so on in the order a, e, i, o, u.
        The consonants remain the same. The dictionary should have 52
        keys of all the uppercase letters and all the lowercase letters.

        Example: When input "eaiuo":
        Mapping is a->e, e->a, i->i, o->u, u->o
        and "Hello World!" maps to "Hallu Wurld!"

        Returns: a dictionary mapping a letter (string) to
                 another letter (string).
        """
        dict_map = {}

        for x in range(52):
            for char in CONSONANTS_LOWER:
                dict_map[char] = char
            for char in CONSONANTS_UPPER:
                dict_map[char] = char
            x = 0
            for char in VOWELS_LOWER:
                dict_map[char] = vowels_permutation[x]
                x += 1
            vowels_permutation_upper = vowels_permutation.upper()
            x = 0
            for char in VOWELS_UPPER:
                dict_map[char] = vowels_permutation_upper[x]
                x += 1
        return dict_map

    def apply_transpose(self, transpose_dict):
        """
        transpose_dict (dict): a transpose dictionary

        Returns: an encrypted version of the message text, based
        on the dictionary
        """
        text = self.message_text
        encrypted_text = text[:]
        for x in range(len(text)):
            if text[x] in VOWELS_LOWER or text[x] in VOWELS_UPPER:
                encrypted_text = encrypted_text[:x] + transpose_dict[text[x]] + encrypted_text[x+1:]
        return encrypted_text


class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
        """
        Initializes an EncryptedSubMessage object

        text (string): the encrypted message text

        An EncryptedSubMessage object inherits from SubMessage and has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        """
        SubMessage.__init__(self, text)

    def decrypt_message(self):
        """
        Attempt to decrypt the encrypted message

        Idea is to go through each permutation of the vowels and test it
        on the encrypted message. For each permutation, check how many
        words in the decrypted text are valid English words, and return
        the decrypted message with the most English words.

        If no good permutations are found (i.e. no permutations result in
        at least 1 valid word), return the original string. If there are
        multiple permutations that yield the maximum number of words, return any
        one of them.

        Returns: the best decrypted message

        Hint: use your function from Part 4A
        """
        vowel_perm_lower = get_permutations(VOWELS_LOWER)
        number_of_real_words = 0
        max_number_of_real_words = 0
        decrypted_message = ''
        for Permutation in vowel_perm_lower:
            decrypted_dict = self.apply_transpose(self.build_transpose_dict(Permutation))
            for word in decrypted_dict.split():
                if is_word(self.get_valid_words(), word):
                    number_of_real_words += 1
            if number_of_real_words > max_number_of_real_words:
                decrypted_message = decrypted_dict
                max_number_of_real_words = number_of_real_words

        if max_number_of_real_words == 0:
            return self.message_text

        else:
            return decrypted_message


if __name__ == '__main__':
    # Example test case
    message = SubMessage("Hello World!")
    permutation = "eaiuo"
    enc_dict = message.build_transpose_dict(permutation)
    print("Original message:", message.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "Hallu Wurld!")
    print("Actual encryption:", message.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print("Decrypted message:", enc_message.decrypt_message())
    print()

    # TODO: WRITE YOUR TEST CASES HERE

    message = SubMessage("Dogs are great!")
    permutation = "eaiuo"
    enc_dict = message.build_transpose_dict(permutation)
    print("Original message:", message.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "Dugs era graet!")
    print("Actual encryption:", message.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print("Decrypted message:", enc_message.decrypt_message())
    print()

    message = SubMessage("Slava Russia!")
    permutation = "eaiuo"
    enc_dict = message.build_transpose_dict(permutation)
    print("Original message:", message.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "Sleve Rossie!")
    print("Actual encryption:", message.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print("Decrypted message:", enc_message.decrypt_message())
