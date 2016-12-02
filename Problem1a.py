__author__ = 'consultadd'
'''
(i) Write a function which accepts 2 params - a string and a word and computes the following:

A. Count occurrences of the word in the string
B. Remove that word from string
C. Append same word equal to number of occurrences in string.
'''


def checkWord(str, w):
    c = 0
    s = str.split()
    for i in range(0, len(s),1):
        if s[i] == w:
            c += 1
    return c, w, str.replace(w,'').strip(), " ".join((str, c*w))

print checkWord("strings are strings that never ends", 'strings')