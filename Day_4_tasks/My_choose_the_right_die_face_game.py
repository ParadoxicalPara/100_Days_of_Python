# Author: ParadoxicaL
""" This is a program that generates a random die and ask you to guess what the
die is. If you guess the generated die right, you win, else, you lose. Enjoy
the dice ascii art I created myself to make it fun:)"""
from random import randint

class die:
    """This class creates a die with 6 faces.
The draw(face) method prints the face of the die to the screen.
The face() method returns an integer value indicating the current number of
faces the die has."""
    def __init__(self):
        """Creates a die"""
        self.die1 = '''
.-------.
|       |
|   O   |
|       |
'-------'
'''
        self.die2 = '''
.-------.
| O     |
|       |
|     O |
'-------'
'''
        self.die3 = '''
.-------.
| O     |
|   O   |
|     O |
'-------'
'''
        self.die4 = '''
.-------.
| O   O |
|       |
| O   O |
'-------'
'''
        self.die5 = '''
.-------.
| O   O |
|   O   |
| O   O |
'-------'
'''
        self.die6 = '''
.-------.
| O   O |
| O   O |
| O   O |
'-------'
'''
        self.dice = [self.die1, self.die2, self.die3, self.die4, self.die5, \
                     self.die6]
    def draw(self, face):
        """Prints out die with faces \"face\""""
        try:
            self.__face = int(face)
            print(self.dice[int(face)-1])
        except: 
            print("\nNo such number of face")
    def face(self):
        """Returns an integer indicating the latest number of faces the die has
"""
        return self.__face

# The function that executes the main program.
def main():
    # Creating a die for the user and for the computer
    usrDie = die()
    compDie = die()
    
    # Asking user to enter the number of faces and generating a random face for the computer
    print("\nHello:) Can you try to guess the right face \
the die stored in the computer has?")
    usrFace = input("\nEnter your guessed face (from 1-6): ")
    compFace = randint(1,6)

    # Printing the results
    print("\nThe face you guessed is: ")
    usrDie.draw(usrFace)
    print("\nThe acutal face of the die in the computer is: ")
    compDie.draw(compFace)
    if usrDie.face()==compDie.face():
        print("\nYou won!")
    else:
        print("\nSorry, you guessed it wrong:{")
main()
    
