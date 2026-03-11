#!/usr/bin/python3
# Run-length encoding.

string = "aaaaabbbccd"


# Time O(N)
# Space O(N)
def run_length_encoding(string):
    encoded = []
    length = 1
    for i in range(1, len(string)):
        curr = string[i]
        prev = string[i-1]

        if curr != prev or len == 9:
            encoded.append(str(length))
            encoded.append(prev)
            length = 0

        length += 1

    # handle the last element
    encoded.append(str(length))
    encoded.append(string[-1])

    return "".join(encoded)


print(run_length_encoding(string))


# Time O(N)
# Space O(N)
def run_len_encoding(string):
    encoded = []

    cnt = 1
    for i in range(len(string)):
        if i == len(string) - 1:
            encoded.append(str(cnt) + string[i])

        elif string[i] == string[i + 1]:
            if cnt == 9:
                encoded.append(str(cnt) + string[i])
                cnt = 1
                continue

            cnt += 1
        else:
            encoded.append(str(cnt) + string[i])
            cnt = 1

    return ''.join(encoded)


print(run_len_encoding(string))
