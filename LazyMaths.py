import math
import sys

#Code is chunky as hell, im still learning more efficent ways of programming, however I am not a programmer.
#f-strings weren't taught when I first learnt python but now I am aware I will start to use them, they rock!

#standard form is simple as formatting an integer (input, 10.2E/5.2e)
#will add this next, then will attempt a loop that allows user to naviagate
#back to welcome message
#add option to exit program which breaks that loop

#Print Welcome message and available options
print("Multi-Function maths program by ClassErased, more features added as I require them. Along with better code. \n")
print("[1] nCr program \n[2] Subnet calculator \n")
#Create variable for users choice and perform basic input validation
choice = int(input("Select a program number from the list above: "))
if choice >= 3 or choice <= 0:
    print("\nInvalid input, terminating!\n")
    sys.exit()

#Begin while loop for the number of the program requested.    
while choice == 1:
    print("\nProgram to perform nCr calculation for combinations")
    #User inputs the n and r variables of nCr equation which must be an integer
    n = int(input("What is the number of possible selections?: "))
    r = int(input("How many can you choose?: "))
    #Performs nCr calculation and prints the result, asks user what to do next.
    answer = (math.comb(n, r))
    print("\nThe amount of possible combinations is", answer) 
    choice2 = input("\nWould you like to perform another calculation? [Y/N]: ")
    
    #Checks user decision and takes correct action
    if choice2 == "Y" or choice2 == "y":
        continue
    
    elif choice2 == "N" or choice2 == "n":
        break

    else:
        #Catches invalid input
        print("\nInvalid input, terminating!\n")
        sys.exit()

#Program yet to be built, looks more complicated than I thought but there has to be a simpler way!
while choice == 2:
    inet = input("What is the default gateway address?: ")
    range = input("How many subnets do you need?: ")
    range2 = input("How many hosts in a subnet do you need?: ")
    print("\nSubnet calculator not available at this time, exiting program\n")
    break

print("\nThank you for using the tool, goodbye.\n")
