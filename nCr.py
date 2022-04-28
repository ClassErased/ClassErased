import math
import time
import sys

#Welcome message
print("Program to perform nCr calculation for combinations")

#Define selection pool
n = int(input("What is the number of possible selections?: "))

#Define selection limit
r = int(input("How many can you choose?: "))

#This method ignores repeats as it is assumed users will not repeat words
print("Calculating...")

#Perform nCr calculation then print amount of possiblities.
#Exit the program after 10 seconds
print (math.comb(n, r)) 
time.sleep(10)
print("Exiting program...")
sys.exit()
