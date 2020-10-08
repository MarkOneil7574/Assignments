age = str(input("Are you a cigarette addict older than 75 years old?(Yes/No)")).title().strip()
while True:   # these while loop is written to force the user to input just Yes or No
    if age == "Yes":
        age = True 
        break
    elif age == "No":
        age = False
        break
    else:
        age = input("Write only Yes or No please !!! Are you a cigarette addict older than 75 years old?(Yes/No)").title().strip()
chronic = input("Do you have a severe chronic disease? (Yes/No)").title().strip()
while True:    # these while loop is written to force the user to input just Yes or No
    if chronic == "Yes":
        chronic = True 
        break
    elif chronic == "No":
        chronic = False
        break
    else:
        chronic = input("Write only Yes or No please !!! Do you have a severe chronic disease? (Yes/No)?").title().strip()
immune = input("Is your immune system too weak? (Yes/No)").title().strip()
while True:    # these while loop is written to force the user to input just Yes or No
    if immune == "Yes":
        immune = True 
        break
    elif immune == "No":
        immune = False
        break
    else:
        immune = input("Write only Yes or No please !!! Is your immune system too weak? (Yes/No)").title().strip()

risk = age or chronic or immune
if risk: 
    print ("You are in risky group")
else :
    print ("You are not in risky group")