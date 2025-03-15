import random

inp = input("Roll the dice? (y/n): ")
roll = inp.lower()
yes = "Y"
no = "N"

playing = True

while playing:
    if(not(roll == no.lower()) and not(roll == yes.lower())):
        print("Invalid choice!")
        inp = input("\nRoll the dice? (y/n): ")
        roll = inp.lower()
    if roll == yes.lower():
        number1 = random.randint(1,6)
        number2 = random.randint(1,6)
        print("(" + str(number1) + "," + str(number2) + ")")
        inp = input("\nRoll the dice? (y/n): ")
        roll = inp.lower()
    elif roll == no.lower():
        print("Thanks for playing")
        playing = False