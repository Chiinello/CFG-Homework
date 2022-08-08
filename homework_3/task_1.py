from collections import Counter

"""
Create required phrase.
----------------------
You are given a string of available characters and a string representing a word or a phrase that you need to generate.
Write a function that checks if you can generate required word/phrase using the characters provided.
If you can, then please return True, otherwise return False.
NOTES:
    You can only generate the phrase if the frequency of unique characters in the characters string is equal or greater
    than frequency in the document string.
FOR EXAMPLE:
    characters = "cbacba"
    phrase = "aabbccc"
    In this case you CANNOT create required phrase, because you are 1 character short!
IMPORTANT:
    The phrase you need to create can contain any characters including special characters, capital letter, numbers
    and spaces.
    You can always generate an empty string.
"""


def generate_phrase(characters, phrase):

    count_chr = Counter(characters)
    count_phr = Counter(phrase)

    if count_chr == count_phr:
        return True
    elif count_chr != count_phr:
        return "Not enough characters"
    else:
        return False


print(generate_phrase("cbacba", "aabbcc"))
print(generate_phrase("lieda87 @£n", "daniel"))


