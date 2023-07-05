# Author: ParadoxicaL
""" This is a program that challenges you travel to FUTA Westgate from FUTA Northgate """

# This fuction will make  sure the user enters a valid option. It tells the user to re-enter if an invalid option is entered
def getInput(label, *args):
    options = args
    inp = input(label)
    while True:
        if inp.lower() in options:
            return inp.lower()
            break
        print("You entered an invalid option. Read carefully to enter a valid option.\n")
        inp = input(label)
        
# The function that executes the main program
def main():
    # Introductory texts
    print("\t\t>> Welcome to FUTA <<\n")
    print("\tYour goal is to travel from FUTA Northgate to FUTA Westgate\n")

    # Getting directions from users
    first_dir = getInput("You are at FUTA Northgate. Type \"forward\" to move forward to the roundabout: ", "forward")

    # Getting second direction provided the the first direction entered is "forward".
    second_dir = getInput("\nYou are at the roundabout. Type \"left\" to go left, \"right\" to go right and \"forward\" to \
go forward: ", "left", "right", "forward")
    if second_dir == "left":
        print("\nSorry, you lost because the leftward direction leads to southgate :(.")
    elif second_dir == "forward":
        print("\nSorry, you lost because the forward direction leads to SUB Building :(.")
    else:
        print("\nGood Job so far!\nYou are at the second roundabout where the newly installed traffic light is, backing T.I. Francis.")

        # Getting Third direction provided that the second direction entered is "right".
        third_dir = getInput("Type \"right\" to go right and \"forward\" to go forward: ", "right", "forward")
        if third_dir == "right":
            print("\nSorry, you lost because the rightward direction leads to School of Computing :(.")
        else:
            print("\nCongratulations :). You won because the forward direction leads to FUTA Westgate and you are there at the moment:)\n")
main()
