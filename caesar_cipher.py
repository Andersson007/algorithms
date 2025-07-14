#!/usr/bin/python3
# Caesar Cipher Encryption.
# Given a non-empty string of lowercase letters
# and a non-negative integer representing a key,
# write a function that returns a new string obtained
# by shifting every letter in the input string by k
# positions in the alphabet, where k is the key.
# Note that letter should "wrap" around the alphabet, i.e.
# the letter "z" shifted by one returns the letter "a".

# We'll use unicode codes + the modulo operator.
# The modulo operator is used to compute the remainder
# of a division operator. In case of key % 26, it will
# keep the key var within 26 in case its bigger than
# the number of letter in the English alphabet.

# The ord() function returns a digital representation of
# a single character.

# Unicode a = 97, z = 122

string = "xyz"
key = 2


def caesar_cipher(string, key):
    new_letters = []

    for char in string:
        # ord(char) - 97 where 97 is a digital
        # representation of the character "a"
        # converts the character to a 0-25 index.
        # Then we add the shift and wrap around
        # with % 26.
        shifted = (ord(char) - 97 + key) % 26
        # Then we convert it back with chr(97 + shifted)
        new_letters.append(chr(97 + shifted))

    return "".join(new_letters)


print(caesar_cipher(string, key))
