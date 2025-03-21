def main():
    name = input("Welcome player to Challenging Days! What do you wish to be called? ")
    print("You will traverse your days, interacting with different people in your life. However, you seem to have woken up on the"
    "wrong side of the bed. Good luck going through, your challenging days! ;)")

    reputation = 100

    scenerio_one(reputation, name)
    scenerio_two(reputation, name)
    scenerio_three(reputation, name)
    scenerio_four(reputation, name)
    scenerio_five(reputation, name)
    scenerio_six(reputation, name)
    scenerio_seven(reputation, name)
    scenerio_eight(reputation, name)
    scenerio_nine(reputation, name)
    scenerio_ten(reputation, name)

def scenerio_one(reputation, name):
    print("You wake up and tap your phone to check the time. Your phone is dead."
    " You get up to check the time on your laptop and realize you're super late!"
    " On the way out, you tell your mom that your charger must be broken because your "
    "phone didn't charge.\n"
    "Your mom admits she unplugged your phone at night because she needed a charger "
    "and forgot to plug your phone back in.\n"
    "What do you respond with, " + str(name) + "?\n"
    "a) What the hell is your problem Mom?\n"
    "b) I'm late and its all your fault!\n"
    "c) Of course you would do something like that. *scoffs at her*")

    option = input("Choose an option by writing a, b, or c: ").strip().lower()

    if option == "a":
        good_option(reputation)

    if option == "b":
        decent_option(reputation)
    
    if option == "c":
        bad_option(reputation)

    while option not in ["a", "b", "c"]:
        option = input("Invalid choice. Choose between options a, b, or c: ").strip().lower()

def scenerio_two(reputation, name):
    print("Premise, premise, premise")

def scenerio_three(reputation, name):
    print("Premise, premise, premise")

def scenerio_four(reputation, name):
    print("Premise, premise, premise")

def scenerio_five(reputation, name):
    print("Premise, premise, premise")

def scenerio_six(reputation, name):
    print("Premise, premise, premise")

def scenerio_seven(reputation, name):
    print("Premise, premise, premise")

def scenerio_eight(reputation, name):
    print("Premise, premise, premise")

def scenerio_nine(reputation, name):
    print("Premise, premise, premise")

def scenerio_ten(reputation, name):
    print("Premise, premise, premise")


def good_option(reputation):
    print("Make sure to update reputation dependant on this choice")

def bad_option(reputation):
    print("Make sure to update reputation dependant on this choice")

def decent_option(reputation):
    print("Make sure to update reputation dependant on this choice")

main()
