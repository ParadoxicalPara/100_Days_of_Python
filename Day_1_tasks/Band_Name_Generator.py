""" A program that generates a possible Band Name from the city's name and
pet name entered """
def main():
    print("\t>> Welcome to Band Name Generator:) <<\n")
    
    # Requesting for Name of City and pet's name
    city = input("Kindly enter the name of the city you grew up in: ")
    pet = input("\nFinally, whats's your pet's name: ")
    
    print("\nYour brand name could be: {0} {1}".format(city.title(), pet.title()))
main()
