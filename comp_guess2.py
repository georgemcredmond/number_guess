"""
Program: comp_guess.py
Project 3-3
Author: George

The computer will try to guess the user's number using the minimum number of attempts.
"""
import random

myNumber = int(input("Enter a number between 1 and 100: "))
print("The secret number is", myNumber)
print("")
count = 0

while True:
	count += 1
	compNumber = random.randint(1, 100)
	print("The computer guess is", compNumber)
	
	if compNumber == myNumber:
		print("MATCH made in", count, "tries!")
		break
	else:
		print("Nope, not the right number")
		print("")
		if count == 5:
			print("GAME OVER: You didn't guess it")
			break
		
