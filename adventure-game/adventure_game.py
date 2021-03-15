import time
import random


def print_with_pause(str):
    print(str)
    time.sleep(3)


def intro():
    print_with_pause("You, Queen of the Elves, are taking a casual stroll\n"
                     "through your royal garden when you come across a\n"
                     "large, old, tree.\n")
    print_with_pause("This is your garden, and you've spent many years here,\n"
                     "yet you've never seen this tree before.\n")
    print_with_pause("The tree has a large, dark, opening that seems to lead\n"
                     "somewhere.\n")


def getUserInput(prompt):
    while True:
        try:
            response = int(input(prompt))
        except ValueError:
            print_with_pause("Sorry, that is not a valid input, try again.\n")
            continue
        else:
            return response
            break


def first_choice():
    flags = []

    response = getUserInput("Enter 1 if you'd like to go into the"
                            " tree.\n"
                            "Enter 2 if you'd like to call for the royal"
                            " gaurd.\n"
                            "What would you like to do?\n")

    if response == 1:
        no_gaurd(flags)
    elif response == 2:
        gaurds(flags)
    else:
        print_with_pause("Sorry, that is not a valid input, try again.\n")
        first_choice()


def no_gaurd(flags):
    if "waitForLight" in flags:
        print_with_pause("The tunnel does not get any brighter.\n")
    else:
        print_with_pause("You enter the tree to find it leads to a dark\n"
                         "underground tunnel.\n")
        print_with_pause("You feel around but cannot see anything so you\n"
                         "must call your gaurds for a torch.\n")

    response = getUserInput("Enter 1 if you'd like to call for the royal"
                            " gaurd.\n"
                            "Enter 2 if you'd like to wait and see if the"
                            " tunnel gets brighter.\n"
                            "What would you like to do?\n")

    if response == 1:
        flags.append("askedForTorch")
        gaurds(flags)
    elif response == 2:
        if "waitForLight" not in flags:
            flags.append("waitForLight")
        no_gaurd(flags)
    else:
        print_with_pause("Sorry, that is not a valid input, try again.\n")
        no_gaurd(flags)


def gaurds(flags):
    print_with_pause("Your gaurds arrive and enter the tree with you.\n")

    if "askedForTorch" in flags:
        print_with_pause("They light their torches and you all"
                         " enter the cave.\n")
    else:
        print_with_pause("The tree leads to a dark underground tunnel.\n")
        print_with_pause("It is hard to see but the gaurds have torches"
                         " that they light.\n")

    print_with_pause("You walk deeper and deeper into the tunnel.\n")
    print_with_pause("Soon, you reach the end where you find a large alter"
                     " that blocks a doorway.\n")
    print_with_pause("The alter has spot in the center that can be lit with"
                     " the torch.\n")

    response = getUserInput("Enter 1 if you'd like to light the alter.\n"
                            "Enter 2 if you'd like to ask the gaurds to try"
                            " and move the alter.\n"
                            "What would you like to do?\n")

    if response == 1:
        lightAlter(flags)
    elif response == 2:
        moveAlter(flags)
    else:
        print_with_pause("Sorry, that is not a valid input, try again.\n")
        gaurds(flags)


def moveAlter(flags):
    if "movedAlter" in flags:
        print_with_pause("The gaurds keep trying to move the alter but it"
                         " appears to be too heavy.\n")
    else:
        print_with_pause("The gaurds all try and move the alter but it appears"
                         " to be too heavy.\n")

    print_with_pause("The door is still blocked and the alter still unlit.\n")

    response = getUserInput("Enter 1 if you'd like to light the alter.\n"
                            "Enter 2 if you'd like to keep trying to move"
                            " the alter.\n"
                            "What would you like to do?\n")

    if int(response) == 1:
        lightAlter(flags)
    elif int(response) == 2:
        if "movedAlter" not in flags:
            flags.append("movedAlter")
        moveAlter(flags)
    else:
        print_with_pause("Sorry, that is not a valid input, try again.\n")
        moveAlter(flags)


def lightAlter(flags):
    print_with_pause("You light the alter with a torch.\n")
    print_with_pause("For a moment, nothing happens.\n")
    print_with_pause("The alter starts to make a loud noise and the door"
                     " behind it begins to turn.\n")
    print_with_pause("An ancient and large snake appears and begins"
                     " to attack!!\n")

    response = getUserInput("Enter 1 if you'd like to run.\n"
                            "Enter 2 if you'd like to stay and fight.\n"
                            "What would you like to do?\n")

    if response == 1:
        run(flags)
    elif response == 2:
        fight(flags)
    else:
        print_with_pause("Sorry, that is not a valid input, try again.\n")
        lightAlter(flags)


def run(flags):
    print_with_pause("Your gaurds and you begin to run down the tunnel"
                     " but the snake is too fast.\n")
    print_with_pause("It attacks your gaurds then comes for you.\n")
    print_with_pause("You keep running but are not fast enough and the"
                     " snake gets you before you can escape the tunnel.\n")

    response = getUserInput("Enter 1 if you'd like to play again.\n"
                            "Enter 2 if you'd like to quit.\n"
                            "What would you like to do?\n")

    if response == 1:
        print_with_pause("Restarting game. Good Luck!\n")
        gamePlay()
    elif response == 2:
        print_with_pause("Thank you for playing. Try again next time.\n")
    else:
        print_with_pause("Sorry, that is not a valid input, try again.\n")
        run(flags)


def fight(flags):
    print_with_pause("You lead your gaurds into an epic fight with"
                     " the snake monster.\n"
                     "Its an incredible battle for the ages that goes on"
                     " for many hours.\n")

    fightResult = random.randint(1, 2)

    if fightResult == 1:
        print_with_pause("Your gaurds are tired and you see that you're\n"
                         "about to lose, but then you find the will and"
                         " slay the beast.\n")
        print_with_pause("You walk out of their victorious knowing your\n"
                         "kingdom is safe for another day.\n")
    elif fightResult == 2:
        print_with_pause("You fight bravely but your gaurds are tired and\n"
                         "the battle is not going well.\n")
        print_with_pause("The beast is too strong and ends up demolishing you"
                         " and your gaurds.\n"
                         "The kingdom has fallen.\n")
        print_with_pause("Game Over.\n")

    response = getUserInput("Enter 1 if you'd like to play again.\n"
                            "Enter 2 if you'd like to quit.\n"
                            "What would you like to do?\n")

    if response == 1:
        print_with_pause("Restarting game. Good Luck!\n")
        gamePlay()
    elif response == 2:
        print_with_pause("Thank you for playing. Try again next time.\n")
    else:
        print_with_pause("Sorry, that is not a valid input, try again.\n")
        run(flags)


def gamePlay():
    intro()
    first_choice()


gamePlay()
