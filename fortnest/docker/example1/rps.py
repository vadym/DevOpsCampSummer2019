#!/usr/bin/env python3
"""
ROCK PAPER SCISSORS

Program should ask the user for the input either (ROCK, PAPER, SCISSORS)
and compare it to computer generated (ROCK, PAPER, SCISSORS), print out the output

For that I need a random generated number, list of things that I'm gonna associate with random numbers.
User input
Comparing logic
Failing cases
Make it continuous

"""
import random

listofthings = ['Rock', 'Paper', 'Scissors']
#answerlist = ['yes', 'no', 'y', 'n']
#alreadyplayed = 0

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


#while True:
#    alreadyplayed += 1
#    rockpaperscissors()
#    askcont = input("Wanna play again Y/N: ")
#    if askcont.lower() not in ('yes', 'y', 'no', 'n'):
#        #checku()
#        if askcont.lower() == "no" or askcont.lower() == "n":
#            print("Exiting...")
#            break
#        elif askcont.lower() == "yes" or askcont.lower() == "y":
#            rockpaperscissors()
#            continue
#        else:
#            print("zulul")
#            break
#    elif askcont.lower() == "yes" or askcont.lower() == "y":
#        continue
#    elif askcont.lower() == "no" or askcont.lower() == "n":
#        break
#    else:
#        print("lul")
#        break

#def checku():
#    while True:
#        askcont = input("Wrong input, try again, Y/N: ")
#        if askcont.lower() == "no" or askcont.lower() == "n":
#            print("Exiting...")
#            break
#        elif askcont.lower() == "yes" or askcont.lower() == "y":
#            rockpaperscissors()
#            break
#        else:
#            print("zulul")
#            break

#def contin(askcont):
#   if askcont.lower() == "yes" or askcont.lower() == "y":
#       rockpaperscissors()
#   elif askcont.lower() == "no" or askcont.lower() == "n":
#       print("Exiting...")
#   else:
#       print("Something went terribly wrong")


#while True:
#    rockpaperscissors()
#    askcont = input("Wanna play again Y/N: ")
#    if askcont.lower() in ('yes', 'y', 'no', 'n'):
#        checku()
#        continue
#    elif askcont.lower() == "yes" or askcont.lower() == "y":
#        rockpaperscissors()
#    elif askcont.lower() == "no" or askcont.lower() == "n":
#        break
#    else:
#        print("Something went terribly wrong")
#        break
         

