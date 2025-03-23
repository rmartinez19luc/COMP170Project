def main():
    name = input("Welcome player to Challenging Days! What do you wish to be called? ")
    print("\nYou will traverse your days, interacting with different people in your life. However, you seem to have woken up on the"
    " wrong side of the bed. Good luck going through, your challenging days! ;)")

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

    print("\nYour final reputation score is: ", reputation)
    if reputation >= 55:
        print("\n Good reputation: You successfully earned yourself a good reputation!")
    elif 30 <= reputation < 55:
        print("\nDecent reputation: Not bad, pat yourself on the back and say you made it!")
    else: 
        print("\nBad reputation: Ouch, better luck next time my friend.")

def scenerio_one(reputation, name):
    print("\n\n\033[1mDAY 1: MORNING DISASTER\033[0m")
    print("\nYou wake up and tap your phone to check the time. Your phone is dead."
    " You get up to check the time on your laptop and realize you're super late!"
    " On the way out, you tell your mom that your charger must be broken because your "
    "phone didn't charge.\n"
    "Your mom admits she unplugged your phone at night because she needed a charger "
    "and forgot to plug your phone back in.\n"
    "\nWhat do you respond with, " + str(name) + "?\n"
    "a) What the hell is your problem Mom?\n"
    "b) I'm late and its all your fault!\n"
    "c) Of course you would do something like that. *scoffs at her*")

    option = input("\nChoose an option by writing a, b, or c: ").strip().lower()

    while option not in ["a", "b", "c"]:
        option = input("\nInvalid choice. Choose between options a, b, or c: ").strip().lower()

    if option == "a":
        reputation = good_option(reputation + 10)
        print("\nGreat choice! you have gained 10 reputation points."
        "Your new reputation is: ", reputation, "\n")

    elif option == "b":
        reputation = decent_option(reputation + 5)
        print("\nCould have done better! You gained 5 reputation points."
        "Your new reputation is:", reputation, "\n")
    
    else:
        reputation = bad_option(reputation - 10)
        print("\nUh ohhh. Sometimes self reflection is the best option... You lost 10 reputation points."
        "Your new reputation is:", reputation, "\n")

    return reputation

def scenerio_two(reputation, name):

    option = input("\nChoose an option by writing a, b, or c: ").strip().lower()

    while option not in ["a", "b", "c"]:
        option = input("\nInvalid choice. Choose between options a, b, or c: ").strip().lower()

    if option == "a":
        reputation = good_option(reputation + 10)
        print("\nGreat choice! you have gained 10 reputation points."
        "Your new reputation is: ", reputation, "\n")

    elif option == "b":
        reputation = decent_option(reputation + 5)
        print("\nCould have done better! You gained 5 reputation points."
        "Your new reputation is:", reputation, "\n")
    
    else:
        reputation = bad_option(reputation - 10)
        print("\nUh ohhh. Sometimes self reflection is the best option... You lost 10 reputation points."
        "Your new reputation is:", reputation, "\n")

    return reputation

def scenerio_three(reputation, name):
    print("Premise, premise, premise")
    option = input("\nChoose an option by writing a, b, or c: ").strip().lower()

    while option not in ["a", "b", "c"]:
        option = input("\nInvalid choice. Choose between options a, b, or c: ").strip().lower()

    if option == "a":
        reputation = good_option(reputation + 10)
        print("\nGreat choice! you have gained 10 reputation points."
        "Your new reputation is: ", reputation, "\n")

    elif option == "b":
        reputation = decent_option(reputation + 5)
        print("\nCould have done better! You gained 5 reputation points."
        "Your new reputation is:", reputation, "\n")
    
    else:
        reputation = bad_option(reputation - 10)
        print("\nUh ohhh. Sometimes self reflection is the best option... You lost 10 reputation points."
        "Your new reputation is:", reputation, "\n")

    return reputation

def scenerio_four(reputation, name):
    print("Premise, premise, premise")
    option = input("\nChoose an option by writing a, b, or c: ").strip().lower()

    while option not in ["a", "b", "c"]:
        option = input("\nInvalid choice. Choose between options a, b, or c: ").strip().lower()

    if option == "a":
        reputation = good_option(reputation + 10)
        print("\nGreat choice! you have gained 10 reputation points."
        "Your new reputation is: ", reputation, "\n")

    elif option == "b":
        reputation = decent_option(reputation + 5)
        print("\nCould have done better! You gained 5 reputation points."
        "Your new reputation is:", reputation, "\n")
    
    else:
        reputation = bad_option(reputation - 10)
        print("\nUh ohhh. Sometimes self reflection is the best option... You lost 10 reputation points."
        "Your new reputation is:", reputation, "\n")

    return reputation

def scenerio_five(reputation, name):
    print("Premise, premise, premise")
    option = input("\nChoose an option by writing a, b, or c: ").strip().lower()

    while option not in ["a", "b", "c"]:
        option = input("\nInvalid choice. Choose between options a, b, or c: ").strip().lower()

    if option == "a":
        reputation = good_option(reputation + 10)
        print("\nGreat choice! you have gained 10 reputation points."
        "Your new reputation is: ", reputation, "\n")

    elif option == "b":
        reputation = decent_option(reputation + 5)
        print("\nCould have done better! You gained 5 reputation points."
        "Your new reputation is:", reputation, "\n")
    
    else:
        reputation = bad_option(reputation - 10)
        print("\nUh ohhh. Sometimes self reflection is the best option... You lost 10 reputation points."
        "Your new reputation is:", reputation, "\n")

    return reputation

def scenerio_six(reputation, name):
    print("Premise, premise, premise")
    option = input("\nChoose an option by writing a, b, or c: ").strip().lower()

    while option not in ["a", "b", "c"]:
        option = input("\nInvalid choice. Choose between options a, b, or c: ").strip().lower()

    if option == "a":
        reputation = good_option(reputation + 10)
        print("\nGreat choice! you have gained 10 reputation points."
        "Your new reputation is: ", reputation, "\n")

    elif option == "b":
        reputation = decent_option(reputation + 5)
        print("\nCould have done better! You gained 5 reputation points."
        "Your new reputation is:", reputation, "\n")
    
    else:
        reputation = bad_option(reputation - 10)
        print("\nUh ohhh. Sometimes self reflection is the best option... You lost 10 reputation points."
        "Your new reputation is:", reputation, "\n")

    return reputation

def scenerio_seven(reputation, name):
    print("Premise, premise, premise")
    option = input("\nChoose an option by writing a, b, or c: ").strip().lower()

    while option not in ["a", "b", "c"]:
        option = input("\nInvalid choice. Choose between options a, b, or c: ").strip().lower()

    if option == "a":
        reputation = good_option(reputation + 10)
        print("\nGreat choice! you have gained 10 reputation points."
        "Your new reputation is: ", reputation, "\n")

    elif option == "b":
        reputation = decent_option(reputation + 5)
        print("\nCould have done better! You gained 5 reputation points."
        "Your new reputation is:", reputation, "\n")
    
    else:
        reputation = bad_option(reputation - 10)
        print("\nUh ohhh. Sometimes self reflection is the best option... You lost 10 reputation points."
        "Your new reputation is:", reputation, "\n")

    return reputation

def scenerio_eight(reputation, name):
    print("Premise, premise, premise")
    option = input("\nChoose an option by writing a, b, or c: ").strip().lower()

    while option not in ["a", "b", "c"]:
        option = input("\nInvalid choice. Choose between options a, b, or c: ").strip().lower()

    if option == "a":
        reputation = good_option(reputation + 10)
        print("\nGreat choice! you have gained 10 reputation points."
        "Your new reputation is: ", reputation, "\n")

    elif option == "b":
        reputation = decent_option(reputation + 5)
        print("\nCould have done better! You gained 5 reputation points."
        "Your new reputation is:", reputation, "\n")
    
    else:
        reputation = bad_option(reputation - 10)
        print("\nUh ohhh. Sometimes self reflection is the best option... You lost 10 reputation points."
        "Your new reputation is:", reputation, "\n")

    return reputation

def scenerio_nine(reputation, name):
    print("Premise, premise, premise")
    while option not in ["a", "b", "c"]:
        option = input("\nInvalid choice. Choose between options a, b, or c: ").strip().lower()

    if option == "a":
        reputation = good_option(reputation + 10)
        print("\nGreat choice! you have gained 10 reputation points."
        "Your new reputation is: ", reputation, "\n")

    elif option == "b":
        reputation = decent_option(reputation + 5)
        print("\nCould have done better! You gained 5 reputation points."
        "Your new reputation is:", reputation, "\n")
    
    else:
        reputation = bad_option(reputation - 10)
        print("\nUh ohhh. Sometimes self reflection is the best option... You lost 10 reputation points."
        "Your new reputation is:", reputation, "\n")

    return reputation

def scenerio_ten(reputation, name):
    print("Premise, premise, premise")
    while option not in ["a", "b", "c"]:
        option = input("\nInvalid choice. Choose between options a, b, or c: ").strip().lower()

    if option == "a":
        reputation = good_option(reputation + 10)
        print("\nGreat choice! you have gained 10 reputation points."
        "Your new reputation is: ", reputation, "\n")

    elif option == "b":
        reputation = decent_option(reputation + 5)
        print("\nCould have done better! You gained 5 reputation points."
        "Your new reputation is:", reputation, "\n")
    
    else:
        reputation = bad_option(reputation - 10)
        print("\nUh ohhh. Sometimes self reflection is the best option... You lost 10 reputation points."
        "Your new reputation is:", reputation, "\n")

    return reputation


def good_option(reputation):
    print("Make sure to update reputation dependant on this choice")
    while option not in ["a", "b", "c"]:
        option = input("\nInvalid choice. Choose between options a, b, or c: ").strip().lower()

    if option == "a":
        reputation = good_option(reputation + 10)
        print("\nGreat choice! you have gained 10 reputation points."
        "Your new reputation is: ", reputation, "\n")

    elif option == "b":
        reputation = decent_option(reputation + 5)
        print("\nCould have done better! You gained 5 reputation points."
        "Your new reputation is:", reputation, "\n")
    
    else:
        reputation = bad_option(reputation - 10)
        print("\nUh ohhh. Sometimes self reflection is the best option... You lost 10 reputation points."
        "Your new reputation is:", reputation, "\n")

    return reputation

def bad_option(reputation):
    print("Make sure to update reputation dependant on this choice")
    while option not in ["a", "b", "c"]:
        option = input("\nInvalid choice. Choose between options a, b, or c: ").strip().lower()

    if option == "a":
        reputation = good_option(reputation + 10)
        print("\nGreat choice! you have gained 10 reputation points."
        "Your new reputation is: ", reputation, "\n")

    elif option == "b":
        reputation = decent_option(reputation + 5)
        print("\nCould have done better! You gained 5 reputation points."
        "Your new reputation is:", reputation, "\n")
    
    else:
        reputation = bad_option(reputation - 10)
        print("\nUh ohhh. Sometimes self reflection is the best option... You lost 10 reputation points."
        "Your new reputation is:", reputation, "\n")

    return reputation

def decent_option(reputation):
    print("Make sure to update reputation dependant on this choice")
    while option not in ["a", "b", "c"]:
        option = input("\nInvalid choice. Choose between options a, b, or c: ").strip().lower()

    if option == "a":
        reputation = good_option(reputation + 10)
        print("\nGreat choice! you have gained 10 reputation points."
        "Your new reputation is: ", reputation, "\n")

    elif option == "b":
        reputation = decent_option(reputation + 5)
        print("\nCould have done better! You gained 5 reputation points."
        "Your new reputation is:", reputation, "\n")
    
    else:
        reputation = bad_option(reputation - 10)
        print("\nUh ohhh. Sometimes self reflection is the best option... You lost 10 reputation points."
        "Your new reputation is:", reputation, "\n")

    return reputation

main()