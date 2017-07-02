#Made on May 27th, 2017
#Made by SlimxShadyx
#Editted by CaptMcTavish, June 17th, 2017

#Dice Rolling Simulator

import random

def start():
    print "\n\n\nWelcome to dice rolling simulator: \n\nPress any key to proceed\n"
    raw_input("> ")
    result()

def bye():
    print "\nThanks for using the Dice Rolling Simulator! Have a great day!\n"

def result():
    print "\nGreat! Begin by choosing a die! [6] [8] [12]?\n"
    user_dice_chooser = raw_input("> ")
    user_dice_chooser = int(user_dice_chooser)

    if user_dice_chooser == 6:
        dice6()

    elif user_dice_chooser == 8:
        dice8()

    elif user_dice_chooser == 12:
        dice12()

    else:
        print "\nPlease choose one of the applicable options!\n"
        result()

def user_exit_checker():
    user_exit_checker_raw = raw_input("\nIf you want to roll another die, type [roll]. To exit, type [exit].\n\n> ")
    user_exit_checker = (user_exit_checker_raw.lower())
    if user_exit_checker == "roll":
        result()
    else:
        bye()

def dice6():
    dice_6 = random.randint(1, 6)
    print "\r\nYou rolled a " + str(dice_6) + "!"
    user_exit_checker()

def dice8():
    dice_8 = random.randint(1, 8)
    print "\r\nYou rolled a " + str(dice_8) + "!"
    user_exit_checker()

def dice12():
    dice_12 = random.randint(1, 12)
    print "\r\nYou rolled a " + str(dice_12) + "!"
    user_exit_checker()

start()
