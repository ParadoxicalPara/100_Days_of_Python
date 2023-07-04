"""This program helps in calculating the amount of tips each person should pay
by taking the Total Bill, the Number of People to split the bill and the
percentage of tips to be given"""
def main():
    print("\t>> Welcome to the tip calculator <<\n")
    
    # Getting total bill, number of people to split the bill and percentage tip 
    tot_bill = float(input("What was the total bill? $"))
    people = int(input("\nHow many people to split the bill? "))
    perc_tip = float(input("\nWhat percentage tip would you like to give? \
10, 12 or 15? "))

    # Calculating the amount each person should pay
    bill_to_shr = tot_bill*(1+0.01*perc_tip)
    amt_to_pay = round(bill_to_shr/people, 2)

    # Output
    print(f"\nOkay, each person should pay: ${amt_to_pay}\n")
main()
