#!/usr/bin/env python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Additional basic string exercises

# D. verbing
# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.


def verbing(s):
    """adding ing (and ly) because >= 3 is greedy for letters"""
    if len(s) >= 3:
        if s.endswith("ing"):
            return s + "ly"
        return s + "ing"
    return s


# E. not_bad
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!
def not_bad(s):
    """losing not and bad because optimism is in style"""
    not_index = s.find("not")
    bad_index = s.find("bad")
    not_bad_substring = s[not_index:bad_index + 3]
    if bad_index > not_index:
        s = s.replace(not_bad_substring, "good")  # needs substring, not nums
    return s  # could also do else: return s
    # if not_index != -1 and bad_index != -1 and bad_index > not_index:
    #     s = s[:not_index] + "good" + s[bad_index+3]


# F. front_back
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back
def front_back(a, b):
    """halfing/mixing because frankenstein's monster was just the beginning"""
    a_len = len(a)
    b_len = len(b)
    if a_len % 2 == 0:
        a_half = a_len / 2
    else:
        a_half = a_len / 2 + 1
    if b_len % 2 == 0:
        b_half = b_len / 2
    else:
        b_half = b_len / 2 + 1
    a_front = a[:a_half]
    a_back = a[a_half:]
    b_front = b[:b_half]
    b_back = b[b_half:]
    return a_front + b_front + a_back + b_back

    # a_mid = len(a) / 2
    # b_mid = len(b) / 2
    # if len(a) % 2 == 1:
    #     # add 1 if lenght is odd
    #     a_mid += 1
    # if len(b) % 2 == 1:
    #     b_mid += 1
    # return a[:a_mid] + b[:b_mid] + a[a_mid:] + b[b_mid:]

    # ???
    # def split_half(s):
    #     return (len(s) + 1) / 2
    # return a[:split_half(a)] + b[:split_half(b)] + a[split_half(a):] + b[split_half(b):]

    # # ???
    # def split_half(s):
    #     return (len(s) - len(s)) // 2
    # return a[:split_half(a)] + b[:split_half(b)] + a[split_half(a):] + b[split_half(b):]


# Provided simple test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
    """Your code goes here.  Edit this docstring."""
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


# main() calls the above functions with interesting inputs,
# using the above test() to check if the result is correct or not.
def main():
    """Your code goes here.  Edit this docstring."""
    print('verbing')
    test(verbing('hail'), 'hailing')
    test(verbing('swiming'), 'swimingly')
    test(verbing('do'), 'do')

    print()
    print('not_bad')
    test(not_bad('This movie is not so bad'), 'This movie is good')
    test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
    test(not_bad('This tea is not hot'), 'This tea is not hot')
    test(not_bad("It's bad yet not"), "It's bad yet not")

    print()
    print('front_back')
    test(front_back('abcd', 'xy'), 'abxcdy')
    test(front_back('abcde', 'xyz'), 'abcxydez')
    test(front_back('Kitten', 'Donut'), 'KitDontenut')


# Standard boilerplate (python idiom) to call the main() function.
if __name__ == '__main__':
    main()
