#!/usr/bin/env python3
import random

listofthings = ['Rock', 'Paper', 'Scissors']

def rockpaperscissors():
    askuser = input("Choose your destiny Rock, Paper or Scissors: ")
    randomvalue = random.randint(0, 2)
    while True:
        if askuser.lower() not in ('rock', 'r', 'paper', 'p', 'scissors', 's'):
            print("Wrong input, try again") 
            askuser = input("Choose your destiny Rock, Paper or Scissors: ")
            continue
        elif listofthings[randomvalue][:1].lower() == askuser[:1].lower():
            print("Tie")
            break
        elif askuser == "rock".lower() or askuser == "r".lower():
            if randomvalue == 1:
                print("You lose,", "computer chose:", listofthings[1], "which covers", listofthings[0]) 
            else:
                print("You win,", "you chose:", listofthings[0], "which destroys", listofthings[randomvalue])
            break
        elif askuser == "paper".lower() or askuser == "p".lower():
            if randomvalue == 2:
                print("You lose,", "computer chose:", listofthings[2], "which cut", listofthings[1]) 
            else:
                print("You win,", "you chose:", listofthings[1], "which covers", listofthings[randomvalue])
            break
        elif askuser == "scissors".lower() or askuser == "s".lower():
            if randomvalue == 0:
                print("You lose,", "computer chose:", listofthings[0], "which destroys", listofthings[2]) 
            else:
                print("You win,", "you chose:", listofthings[2], "which cuts", listofthings[randomvalue])
            break
        else:
            print("Something went terribly wrong")
            break

while True:
    rockpaperscissors()
    askcont = input("Wanna play again Y/N: ")
    if askcont.lower() not in ('yes', 'y', 'no', 'n'):
        print("Wrong input, try again")
        while True:
            askcont = input("Wanna play again Y/N: ")
            if askcont.lower() not in ('yes', 'y', 'no', 'n'):
                print("Wrong input, try again")
                continue
            elif askcont.lower() in ("yes", "y"):
                rockpaperscissors()
                continue
            elif askcont.lower() in ("no", "n"):
                print("Exiting...")
                break
            else:
                print("zulul")
                break
        break
    elif askcont.lower() in ("yes", "y"):
        continue
    elif askcont.lower() in ("no", "n"):
        print("Exiting...")
        break
    else:
        print("lul")
        break

