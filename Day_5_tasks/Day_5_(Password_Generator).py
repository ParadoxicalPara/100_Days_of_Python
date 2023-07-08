#Author: ParadoxicaL
"""This is a program for generating passwords with specified number of letters,
numbers and symbols"""

from random import shuffle, choice


def main():
    # Initializing a list of numbers, letters and symbols
    nums = [chr(i) for i in range(48,58)]
    ltrs = [chr(i) for i in range(65,91)]+[chr(i) for i in range(97,123)]
    syms = ["\\", "/", ":", "*", "?", "\"", "<", ">", "@", ",", "."]

    # Welcome greeting
    print("\n\t\t>> This is a password generator <<\nEnter the number of letters\
, numbers and symbols you want in your password:)")

    # Getting the number of letters, numbers and symbols
    num_ltrs = int(input("\nHow many letters would you like? "))
    num_nums = int(input("\nHow many numbers would you like? "))
    num_syms = int(input("\nHow many symbols would you like? "))

    # Creating a list of characters in the password
    res = [choice(nums) for i in range(num_nums)]+\
          [choice(ltrs) for i in range(num_ltrs)]+\
          [choice(syms) for i in range(num_syms)]
    # Shuffling the list of result and printing a joined characters in the list as string
    shuffle(res)
    print("\nYour generated password is: {}". format("".join(res)))
main()

