#Question three solution
""" Reverse the order of words given a string."""
def reverse(word):
    word = word.strip()
    print(word) #strip trailing or leading spaces in the string of words
    word = word.split(" ") # split at the white space and make a list of the strings
    print(word)
    word = word[::-1]# reverse the order of list and print out the reversed string
    print(word)
    n = len(word)
    i = 0
    while i<n:
        print(word[i])
        i = i+1


reverse(" my name is gladwell")