import random

number_to_guess = random.randint(1,100)
playing = True

while (playing):
    try:
        user_input = int(input("Guess the number between 1 and 100: "))

        if (user_input < number_to_guess):
            print("Too low")
        if (user_input > number_to_guess):
            print("Too high")
        elif (user_input == number_to_guess):
            print("\nCongratulations, you found the number (" + str(number_to_guess) + ")")
            playing = False
    except ValueError:
        print("Please enter a valid number")
