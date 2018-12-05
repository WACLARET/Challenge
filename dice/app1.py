# question 1:
# Dice Rolling Simulator
# context: Like the title suggests, this project involves writing a program that simulates rolling dice.
# Task:When the program runs, it will randomly choose a number between 1 and 6. (Or whatever other integer you prefer — the number of sides on the die is up to you.) The program will print what that number is. It should then ask you if you’d like to roll again.

 
import random

def roll(sides = 6):
    num_rolled = random.randint(1,sides)
    return num_rolled
def main():
    sides = 6
    rolling = True
    while rolling:    
        user_roll = input("Do you want to roll the dice? y/n: ")
        if user_roll.lower() == "y":
            num_rolled = roll(sides)
            print("you rolled a", num_rolled)
        elif user_roll.lower() == "n":
            rolling = False
            print("Thanks for playing")
        else:
            rolling = False
            print("You entered a wrong choice!!")

main()
