import time
import random
enemy = random.choice(["dragon", "troll", "lion", "tiger", "pirat"])
vapon = [""]


def play():
    vapon.clear()
    intro()
    dir()


def print_pause(message, delay=1):
    print(message)
    time.sleep(delay)


def lb():
    print_pause("\n")


def intro():
    print_pause("\n\n\nGAME LOADING...\n\n\n")
    print_pause("You find yourself standing in an open field,")
    print_pause("filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that a " + enemy +
                " is somewhere around here,")
    print_pause("and has been terrifying the nearby village.")
    lb()


def house():
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens"
                "and out steps a " + enemy + ".")
    print_pause("Eep! This is the " + enemy + "'s house!")
    print_pause("The "+enemy+" attacks you!")
    lb()
    if "sword" in vapon:
        action()
    else:
        print_pause("You feel a bit under-prepared for this,"
                    "what with only having a tiny dagger.")
        action()


def play_again():
    while True:
        choice = input("Would you like to play again (y/n)?\n")
        lb()
        if choice == "y":
            print_pause("Warning! This game seem to be to scary for you.. "
                        "but here you go")
            lb()
            play()
            break
        elif choice == "n":
            print_pause("Thanks for playing! See you next time")
            lb()
            break
        else:
            print_pause("Please enter 1 or 2.")


def cave():
    print_pause("You peer cautiously into the cave.")
    if "sword" in vapon:
        print_pause("You have been here before"
                    "and gotten all the good stuff.")
        print_pause("It's just an empty cave now.")
    else:
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly old dagger"
                    "and take the sword with you.")
        vapon.append("sword")
    lb()
    print_pause("You walk back out to the field.")
    lb()
    dir()


def fight():
    if "sword" in vapon:
        print_pause("As the "+enemy+" moves to attack,"
                    "you unsheath your new sword.")
        print_pause("The sword of Ogoroth shines brightly in your hand"
                    "as you brace yourself for the attack.")
        print_pause("But the "+enemy+" takes one look at your shiny new toy"
                    "and runs away!")
        print_pause("You have rid the town of the "+enemy+"."
                    "You are victorious!")
        lb()
        play_again()
    else:
        print_pause("You do your best...")
        print_pause("but your dagger is no match for the "+enemy)
        print_pause("You have been defeated!")
        lb()
        play_again()


def run():
    print_pause("You run back into the field. Luckily,"
                "you don't seem to have been followed.")
    lb()
    dir()


def action():
    choice = input("Would you like to fight (1) or to run (2) ?\n")
    lb()
    if choice == "1":
        fight()
    elif choice == "2":
        run()
    else:
        print_pause("Please enter 1 or 2.")
        lb()
        action()


def dir():
    print_pause("In front of you is a house")
    print_pause("To right is a dark cave.")
    lb()
    choice = input("What would you like to do?\n"
                   "Enter 1 to knock on the door of the house.\n"
                   "Enter 2 to peer into the cave\n")
    lb()
    if choice == "1":
        house()
    elif choice == "2":
        cave()
    else:
        print_pause("Please enter 1 or 2.")
        lb()
        dir()


play()
