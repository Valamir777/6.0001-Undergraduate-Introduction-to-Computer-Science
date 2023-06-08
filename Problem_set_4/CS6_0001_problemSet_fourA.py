# Problem Set 4A
# Name: Taylor Schaefer Jackson
# Time Spent: 1:30

def get_permutations(sequence):
    """
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    #>>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    """
    sequence_copy = sequence[:]
    if len(sequence_copy) < 1:
        "This is invalid"
    elif len(sequence_copy) == 1:
        return sequence_copy
    else:
        sequence_new = []
        for i, e in enumerate(sequence_copy):
            sequence_new += [e + x for x in get_permutations(sequence.replace(e, ''))]
        return sequence_new


if __name__ == '__main__':
    #    #EXAMPLE
    #    example_input = 'abc'
    #    print('Input:', example_input)
    #    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    #    print('Actual Output:', get_permutations(example_input))

    #    # Put three example test cases here (for your sanity, limit your inputs
    #    to be three characters or fewer as you will have n! permutations for a
    #    sequence of length n)

    print(f'Input: dog')
    print('Expected Output:', ['dog', 'dgo', 'odg', 'ogd', 'gdo', 'god'])
    print(f"Actual Output: {get_permutations('dog')} ")

    print(f'Input: fat')
    print('Expected Output:', ['fat', 'fta', 'aft', 'atf', 'tfa', 'taf'])
    print(f"Actual Output: {get_permutations('fat')} ")

    print(f'Input: cat')
    print('Expected Output:', ['cat', 'cta', 'act', 'atc', 'tca', 'tac'])
    print(f"Actual Output: {get_permutations('cat')} ")