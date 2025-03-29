def main():
    name = input("Welcome player to Challenging Days! What do you wish to be called? ")
    print("\nYou will traverse your days, interacting with different people in your life. However, you seem to have woken up on the"
    " wrong side of the bed. Good luck going through, your challenging days! ;)")

    reputation = 100

    reputation = scenerio_one(reputation, name)
    reputation = scenerio_two(reputation, name)
    reputation = scenerio_three(reputation, name)
    reputation = scenerio_four(reputation, name)
    reputation = scenerio_five(reputation, name)
    reputation = scenerio_six(reputation, name)
    reputation = scenerio_seven(reputation, name)
    reputation = scenerio_eight(reputation, name)
    reputation = scenerio_nine(reputation, name)
    reputation = scenerio_ten(reputation, name)

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

    if option == "b":
        reputation = good_option(reputation)

    elif option == "c":
        reputation = decent_option(reputation)
    
    else:
        reputation = bad_option(reputation )
    
    return reputation

def scenerio_two(reputation, name):
    print("\n\n\033[1mDAY 1: COLLEGE MISHAP\033[0m")
    print("After your horrible start, you meet up with your friends at a coffee shop to get a drink."
    "\n You ordered your Venti Iced Pumpkin Spiced Chai Frappachino with 5 shots of expresso, 5 pumps of vanilla, 3 pumps of hazelnut, "
    "2 pumps of carmel syrup, extra caramel, and extra whipcream. "
    "\nWhen you get your drink, you take a sip and realize it's all wrong!!\n"
    "\nWhat do you do " + str(name) +"?\n"
    "a) Throw drink at barista\n"
    "b) Tell them 'REMAKE IT IMMEDIATELY!'\n"
    "c) Demand a refund and ask to speak to their manager")
    option = input("\nChoose an option by writing a, b, or c: ").strip().lower()

    while option not in ["a", "b", "c"]:
        option = input("\nInvalid choice. Choose between options a, b, or c: ").strip().lower()

    if option == "b":
        reputation = good_option(reputation)

    elif option == "c":
        reputation = decent_option(reputation)
    
    else:
        reputation = bad_option(reputation)

    return reputation

def scenerio_three(reputation, name):
    print("\n\n\033[1mDAY 1: BACK AT HOME\033[0m")
    print("You return back to home after a long day of school. As you throw your bookbag on the floor and lay down, your younger sibling goes up to you and asks you to play with them."
    "\n You say no and that you're tired so they start to cry saying how you never hang out with them. You feel bad and try to say yes but something stops you."
    "\n The word, yes, won't come out and you realize you're left with only 3 options."
    "\n You HAVE to say one " + str(name) + "!\n"
    "\na) You're so annoying!"
    "\nb) I hate you! Get out of my room"
    "\nc) Stop your crying already")
    option = input("\nChoose an option by writing a, b, or c: ").strip().lower()

    while option not in ["a", "b", "c"]:
        option = input("\nInvalid choice. Choose between options a, b, or c: ").strip().lower()

    if option == "a":
        reputation = good_option(reputation)

    elif option == "c":
        reputation = decent_option(reputation)
    
    else:
        reputation = bad_option(reputation )

    return reputation

def scenerio_four(reputation, name):
    print("\n\n\033[1mDAY 2: TITLE\033[0m")
    print("Premise, premise, premise")
    option = input("\nChoose an option by writing a, b, or c: ").strip().lower()

    while option not in ["a", "b", "c"]:
        option = input("\nInvalid choice. Choose between options a, b, or c: ").strip().lower()

    if option == "a":
        reputation = good_option(reputation)

    elif option == "b":
        reputation = decent_option(reputation)
    
    else:
        reputation = bad_option(reputation)

    return reputation

def scenerio_five(reputation, name):
    print("\n\n\033[1mDAY 2: TITLE\033[0m")
    print("Premise, premise, premise")
    option = input("\nChoose an option by writing a, b, or c: ").strip().lower()

    while option not in ["a", "b", "c"]:
        option = input("\nInvalid choice. Choose between options a, b, or c: ").strip().lower()

    if option == "a":
        reputation = good_option(reputation)

    elif option == "b":
        reputation = decent_option(reputation)
    
    else:
        reputation = bad_option(reputation)

    return reputation

def scenerio_six(reputation, name):
    print("\n\n\033[1mDAY 2: TITLE\033[0m")
    print("Premise, premise, premise")
    option = input("\nChoose an option by writing a, b, or c: ").strip().lower()

    while option not in ["a", "b", "c"]:
        option = input("\nInvalid choice. Choose between options a, b, or c: ").strip().lower()

    if option == "a":
        reputation = good_option(reputation)

    elif option == "b":
        reputation = decent_option(reputation)
    
    else:
        reputation = bad_option(reputation)

    return reputation

def scenerio_seven(reputation, name):
    print("\n\n\033[1mDAY 3: TITLE\033[0m")
    print("Premise, premise, premise")
    option = input("\nChoose an option by writing a, b, or c: ").strip().lower()

    while option not in ["a", "b", "c"]:
        option = input("\nInvalid choice. Choose between options a, b, or c: ").strip().lower()

    if option == "a":
        reputation = good_option(reputation)

    elif option == "b":
        reputation = decent_option(reputation)

    else:
        reputation = bad_option(reputation)

    return reputation

def scenerio_eight(reputation, name):
    print("\n\n\033[1mDAY 3: TITLE\033[0m")
    print("Premise, premise, premise")
    option = input("\nChoose an option by writing a, b, or c: ").strip().lower()

    while option not in ["a", "b", "c"]:
        option = input("\nInvalid choice. Choose between options a, b, or c: ").strip().lower()

    if option == "a":
        reputation = good_option(reputation)

    elif option == "b":
        reputation = decent_option(reputation)

    else:
        reputation = bad_option(reputation)

    return reputation

def scenerio_nine(reputation, name):
    print("\n\n\033[1mDAY 4: TITLE\033[0m")
    print("Premise, premise, premise")
    option = input("\nChoose an option by writing a, b, or c: ").strip().lower()
    while option not in ["a", "b", "c"]:
        option = input("\nInvalid choice. Choose between options a, b, or c: ").strip().lower()

    if option == "a":
        reputation = good_option(reputation)

    elif option == "b":
        reputation = decent_option(reputation)
    
    else:
        reputation = bad_option(reputation)

    return reputation

def scenerio_ten(reputation, name):
    print("\n\n\033[1mDAY 5: TITLE\033[0m")
    print("Premise, premise, premise")
    option = input("\nChoose an option by writing a, b, or c: ").strip().lower()
    while option not in ["a", "b", "c"]:
        option = input("\nInvalid choice. Choose between options a, b, or c: ").strip().lower()

    if option == "a":
        reputation = good_option(reputation)

    elif option == "b":
        reputation = decent_option(reputation)
    
    else:
        reputation = bad_option(reputation)

    return reputation


def good_option(reputation):
    reputation -= 5
    print("\nHonestly, you could've done better but not the worst choice! You lost 5 reputation points. \nYour new reputation is: ", reputation, "\n")
    return reputation

def bad_option(reputation):
    reputation -= 15
    print("\nUh ohhh. Sometimes self reflection is the best option... You lost 15 reputation points. \nYour new reputation is:", reputation, "\n")
    return reputation

def decent_option(reputation):
    reputation -= 10
    print("\nWell... it is what it is, could've done better. You lost 10 reputation points. \nYour new reputation is:", reputation, "\n")
    return reputation

main()