# Exercise 6-3.


"""

A palindrome is a word that is spelled the same backward and forward, like “noon” and “redivider”. 
Recursively, a word is a palindrome if the first and last letters are the same and the middle is a palindrome.

Write a function called is_palindrome that takes a string argument and returns True if it is a palindrome and False otherwise. 
Remember that you can use the built-in function len to check the length of a string.
"""


def is_palindrome(arg:str):
    return arg == arg[::-1]