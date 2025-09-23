#!/usr/bin/python3
# Valid IP Addresses.
# * You're given a string of length 12 or smaller.
# * It contains only digits.
# * Write a func that returns all possible IP addresses,
#   that can be created by inserting 3 periods in the string.
# * Each individual integer is within the range 0-255, inclusinve.
# * An IP address isn't valid if any of the individual ints
#   contains leading 0 or any of the ints are greater than 255.
# * If there are no valide IP addresses, the func returns [].

string = "1921680"
# output = ["1.9.216.80", "1.92.16.80", "1.92.168.0", "19.2.16.80", ...]

# The algorithm to solve this is essentially a methodical way of
# trying all possibilities, aka brute-force search.

# Time O(1): as we can only generate 0-255 numbers
#   for each integer which is around 4 billion max.
# Space O(1): because of the same property ^.
def valid_ip_addrs(string):
    ip_addrs = []

    # As we can put the first period only
    # after the first char, we begin with idx 1.
    # min(len(string), 4) is needed to avoid index errors
    # I.e. try first to place the period after 1st digit,
    # then after 2nd, then after 3rd
    for i in range(1, min(len(string), 4)):
        # This loop is for the first period
        ip_parts = ['', '', '', '']

        ip_parts[0] = string[:i]
        # Check validity of the first part
        if not is_valid_part(ip_parts[0]):
            continue

        for j in range(i + 1, i + min(len(string) - i, 4)):
            # This loop is for the second period
            ip_parts[1] = string[i:j]

            # Check validity of the second part
            if not is_valid_part(ip_parts[1]):
                continue

            for k in range(j + 1, j + min(len(string) - j, 4)):
                # This loop is for the third period
                ip_parts[2] = string[j:k]
                ip_parts[3] = string[k:]
                # Check validity of the third and forth parts
                if is_valid_part(ip_parts[2]) and is_valid_part(ip_parts[3]):
                    ip_addrs.append('.'.join(ip_parts))

    return ip_addrs


def is_valid_part(string):
    str_as_int = int(string)
    # Cannot be bigger than 255
    if str_as_int > 255:
        return False

    # Leading 0 check
    if len(string) != len(str(str_as_int)):
        return False

    return True


print(valid_ip_addrs(string))
print(valid_ip_addrs("192168028"))
