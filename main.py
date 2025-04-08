'''FUNCTION main(): 
        name = input of the user who is asked what they would like to be called
        print the game premise for the user
        
        sets reputation variable to be 100 at the start
        
        sets reputation equal to FUNCTION scenerio_one with parameters reputation and name
        sets reputation equal to FUNCTION scenerio_two with parameters reputation and name
        sets reputation equal to FUNCTION scenerio_three with parameters reputation and name
        sets reputation equal to FUNCTION scenerio_four with parameters reputation and name
        sets reputation equal to FUNCTION scenerio_five with parameters reputation and name
        sets reputation equal to FUNCTION scenerio_six with parameters reputation and name
        sets reputation equal to FUNCTION scenerio_seven with parameters reputation and name
        sets reputation equal to FUNCTION scenerio_eight with parameters reputation and name
        sets reputation equal to FUNCTION scenerio_nine with parameters reputation and name
        sets reputation equal to FUNCTION scenerio_ten with parameters reputation and name
        
        print final reputation score using variable reputation
        
        If reputation >= 50 then
            print good ending
        Elif reputation >= 30 then
            print decent ending
        Else
            print bad ending
          '''
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
    if reputation >= 50:
        print("\nGood reputation: You successfully earned yourself a good reputation!")
    elif 30 <= reputation < 55:
        print("\nDecent reputation: Not bad, pat yourself on the back and say you made it!")
    else: 
        print("\nBad reputation: Ouch, better luck next time my friend.")

'''FUNCTION scenerio_one(reputation, name): 
        print heading, DAY 1: MORNING DISASTER
        print premise of scenerio and options to respond to
        
        option = input of user in their choice to respond to scenerio (a, b, or c)
        
        while option not in ["a", "b", "c"]:
            option = user input after being told they but an invalid choice
            
            if option = b then
                reputation = to FUNCTION good_option with parameter reputation
            elif option = c then
                reputation = to FUNCTION decent_option with parameter reputation
            else
                reputation = to FUNCTION bad_option with parameter reputation
                
            return variable reputation'''

def scenerio_one(reputation, name):
    print("\n\n\033[1mDAY 1: MORNING DISASTER\033[0m")
    print("\nYou wake up and tap your phone to check the time. Your phone is dead."
    " You get up to check the time on your laptop and realize you're super late!\n"
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

'''FUNCTION scenerio_two(reputation, name):
        follows same format as scenerio_one'''

def scenerio_two(reputation, name):
    print("\n\n\033[1mDAY 1: COLLEGE MISHAP\033[0m")
    print("After your horrible start, you meet up with your friends at a coffee shop to get a drink."
    "\nYou ordered your Venti Iced Pumpkin Spiced Chai Frappachino with 5 shots of expresso, 5 pumps of vanilla, 3 pumps of hazelnut, "
    "2 pumps of carmel syrup, extra caramel, and extra whipcream."
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

'''FUNCTION scenerio_three(reputation, name): 
        print heading, DAY 1: BACK AT HOME
        print premise of scenerio and options to respond to
        
        option = input of user in their choice to respond to scenerio (a, b, or c)
        
        while option not in ["a", "b", "c"]:
            option = user input after being told they but an invalid choice
            
            if option = a then
                reputation = to FUNCTION good_option with parameter reputation
            elif option = c then
                reputation = to FUNCTION decent_option with parameter reputation
            else
                reputation = to FUNCTION bad_option with parameter reputation
                
            return variable reputation'''

def scenerio_three(reputation, name):
    print("\n\n\033[1mDAY 1: BACK AT HOME\033[0m")
    print("You return back to home after a long day of school. As you throw your bookbag on the floor and lay down, your younger sibling goes up to you and asks you to play with them."
    "\nYou say no and that you're tired so they start to cry saying how you never hang out with them. You feel bad and try to say yes but something stops you."
    "\nThe word, yes, won't come out and you realize you're left with only 3 options."
    "\nYou HAVE to say one " + str(name) + "!\n"
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

'''FUNCTION scenerio_four(reputation, name): 
        print heading, DAY 2: TITLE
        print premise of scenerio and options to respond to
        
        option = input of user in their choice to respond to scenerio (a, b, or c)
        
        while option not in ["a", "b", "c"]:
            option = user input after being told they but an invalid choice
            
            if option = a then
                reputation = to FUNCTION good_option with parameter reputation
            elif option = b then
                reputation = to FUNCTION decent_option with parameter reputation
            else
                reputation = to FUNCTION bad_option with parameter reputation
                
            return variable reputation'''

def scenerio_four(reputation, name):
    print("\n\n\033[1mDAY 2: LOUD KIDS\033[0m")
    print("It's spring break! You hop on a plane with your friends to Miami."
    "\nUnfortunately, you are surrounded by misbehaving toddlers who are yelling and crying loud on the plane."
    "\nTheir parents are not bothered by the noise but you can't take it anymore!"
    "\nWhat would you do to make the kids stop from being loud " + str(name) +"?\n"
    "a) Tell the parents to discipline their kids.\n"
    "b) Complain to the flight attendant and demand for an action.\n"
    "c) Yell at the kids and spank to stop them.") 
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

'''FUNCTION scenerio_five(reputation, name):
        follows same format as scenerio_four'''
def scenerio_five(reputation, name):
    print("\n\n\033[1mDAY 2: PROJECT TEAM\033[0m")
    print("It's April 21st and your COMT 170 team is excited to submit the project you all have been working hard for."
    "\nJust before the deadline, one of your teammate accidentaly deletes all the code and it's not possible to recover."
    "\nThere is not enough time to write the code all over again since you only have 1 hour left to submit everything."
    "\nWhat would you do " + str(name) +"?\n"
    "a) Tell them this is why I didn't want you to be on my team.\n"
    "b) Yell at them 'YOU ARE A LOSER'\n"
    "c) Report the student to the professor so he/she can get 0 on the project.")
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

'''FUNCTION scenerio_six(reputation, name):
        follows same format as scenerio_four'''
def scenerio_six(reputation, name):
    print("\n\n\033[1mDAY 2: FRIEND FIGHT\033[0m")
    print("You wake up one morning and find out your 2 friends Kali and Leyla have been fighting in the group chat."
    "\nKali is your best friend and Leyla is not so close with you."
    "\nKnowing Leyla was right in the argument, you still don't want to upset your best friend Kali."
    "\nWhat would you say to Leyla " + str(name) +"?\n"
    "a) I don't know, leave me out of it\n"
    "b) I dont care who is right, Kali is the goat\n"
    "c) It's not that deep, you're such a drama queen, just get over it")
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

'''FUNCTION scenerio_seven(reputation, name):
        follows same format as scenerio_four'''
def scenerio_seven(reputation, name):
    print("\n\n\033[1mDAY 3: TITLE\033[0m")
    print("After your alarm not going off you realize you have 5 minutes to get to school"
    "\nYou race down to your car only to get inside and realize that it wont start!"
    "\nYou have a test first period, you have to get there in time!"
    "\nWhat do you do? " + str(name) +"?\n"
    "a) Steal your moms car \n"
    "b) Walk to school in the pouring rain \n"
    "c) Beg your ex boyfriend  for a ride") 
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

'''FUNCTION scenerio_eight(reputation, name):
        follows same format as scenerio_four'''
def scenerio_eight(reputation, name):
    print("\n\n\033[1mDAY 3: TITLE\033[0m")
    print("Somehow you make it to first period on time"
    "\nYou sit in your chair and start your test, you realize you studied for the wrong one!"
    "\nThis test is worth 30% of your grade you need it to pass!"
    "\nWhat do you do? " + str(name) +"?\n"
    "a) Look off someone elses test \n"
    "b) Answer A for every question and hope its right \n"
    "c) Use chat gpt ")
    option = input("\nChoose an option by writing a, b, or c: ").strip().lower()

    while option not in ["a", "b", "c"]:
        option = input("\nInvalid choice. Choose between options a, b, or c: ").strip().lower()

    if option == "b":
        reputation = good_option(reputation)

    elif option == "c" :
        reputation = decent_option(reputation)

    else:
        reputation = bad_option(reputation)

    return reputation

'''FUNCTION scenerio_nine(reputation, name):
        follows same format as scenerio_four'''
def scenerio_nine(reputation, name):
    print("\n\n\033[1mDAY 4: TITLE\033[0m")
    print("After school you get home and open the fridge to eat your favorite snack (carrots and hummus)."
    "\nYou have been looking foward to this snack all day. "
    "\nYou turn around and see your sister eating the last bite. "
    "\nWhat do you do? " + str(name) +"?\n"
    "a) slap your sister \n"
    "b) start screaming at her and then break the plate over her head \n"
    "c) starve to death ")
    option = input("\nChoose an option by writing a, b, or c: ").strip().lower()
    while option not in ["a", "b", "c"]:
        option = input("\nInvalid choice. Choose between options a, b, or c: ").strip().lower()

    if option == "c" :
        reputation = good_option(reputation)

    elif option == "a":
        reputation = decent_option(reputation)
    
    else:
        reputation = bad_option(reputation)

    return reputation

'''FUNCTION scenerio_ten(reputation, name):
        follows same format as scenerio_four'''
def scenerio_ten(reputation, name):
    print("\n\n\033[1mDAY 5: TITLE\033[0m")
    print("finally it is friday, this terrible week is almost over!"
    "\nAs you are relaxing upstairs you get a call from your friends to come hang out."
    "\nThis is just what you need after this week from hell! "
    "\nYou go down to ask your mom if it is ok for you to hang out with them."
    "\nYour mom laughs at you and says there is no way, and you have to wash the floors with a toothbrush."
    "\nwhat do you do? " + str(name) +"?\n"
    "a) Sneak out anyways and suffer the concequences \n"
    "b) Yell at her and leave anyway \n"
    "c) Use your moms toothbrush to clean the floors")
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

'''FUNCTION good_option(reputation):
        subtract 5 from reputation
        print Honestly, you could've done better... and reputation variable'''

def good_option(reputation):
    reputation -= 5
    print("\nHonestly, you could've done better but not the worst choice! You lost 5 reputation points. \nYour new reputation is: ", reputation, "\n")
    return reputation

''' FUNCTION bad_option(reputation):
        subtract 15 from reputation
        print Uh ohhh... and reputation variable'''

def bad_option(reputation):
    reputation -= 15
    print("\nUh ohhh. Sometimes self reflection is the best option... You lost 15 reputation points. \nYour new reputation is:", reputation, "\n")
    return reputation

''' FUNCTION decent_option(reputation):
        subtract 10 from reputation
        print Well... it is what it is... and reputation variable'''

def decent_option(reputation):
    reputation -= 10
    print("\nWell... it is what it is, could've done better. You lost 10 reputation points. \nYour new reputation is:", reputation, "\n")
    return reputation

main()