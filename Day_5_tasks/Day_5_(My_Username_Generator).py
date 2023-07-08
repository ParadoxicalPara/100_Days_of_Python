#Author: ParadoxicaL
"""This is a program for generating a username from one's firstname and
lastname"""
from random import choice

def main():
     # Welcome greeting
    print("\n\t\t>> This is a username generator <<\nEnter firstname\
, lastname and the length you want the username to be one after the\
other:)")

    # Getting firstname and lastname
    f_name = input("\nEnter firstname: ")
    l_name = input("\nEnter lastname: ")
    len_usrname = int(input(\
        "\nEnter the length you want for your username: "))

    # Creating a list of the characters in firstname and lastname
    chInNms = [ch for ch in f_name+l_name]

    # Creating a username and printing it
    usrname = [choice(chInNms) for i in range(len_usrname)]
    print("\nYour generated username is: {}".format("".join(usrname).title()))

    # Confirming whether the user likes the username with an event loop
    while True:
        resp = input("\nDo you want to change the username? Enter [Y] for \
Yes and [N] for No: ")
        if resp[0].lower()!="y": break
        else:
            # Generating another username
            usrname = [choice(chInNms) for i in range(len_usrname)]
            print("\nYour generated username is: {}".format("".join(usrname).title()))

main()    
