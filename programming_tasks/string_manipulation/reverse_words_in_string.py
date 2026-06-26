#!/usr/bin/python3
# Reverse Words in String.
# "we are here" -> "here are we"
# * Words are separate by one or more spaces.
# * Words can contain special characters, punc, etc.
# * You're not allowed to use any built-in split/reverse funcs.
# * You're allowed to use join()

# Time O(N)
# Space O(N)
def reverse_words_in_string(string):
    words = []
    start_of_word = 0
    for i in range(len(string)):
        char = string[i]
        if char == ' ':
            words.append(string[start_of_word:i])
            start_of_word = i
        elif string[start_of_word] == ' ':
            words.append(' ')
            start_of_word = i

    # to add the last word
    words.append(string[start_of_word:])
    reverse_list(words)
    return ''.join(words)


def reverse_list(mylist):
    start = 0
    end = len(mylist) - 1
    while start < end:
        # Swap the values
        mylist[start], mylist[end] = mylist[end], mylist[start]
        start += 1
        end -= 1


print(reverse_words_in_string("we are here"))


# Time O(N)
# Space O(N)
def reverse_words(string):
    output = []

    i, j = 0, 0

    while j < len(string):

        if string[j] == " ":
            output.append(string[i:j])
            i = j
        elif string[i] == " ":
            output.append(" ")
            i = j

        j += 1

    # append last word
    output.append(string[i:])

    # swap elements
    left = 0
    right = len(output) - 1
    while left < right:
        output[left], output[right] = output[right], output[left]
        left += 1
        right -= 1

    return ''.join(output)


print(reverse_words("hello world"))
