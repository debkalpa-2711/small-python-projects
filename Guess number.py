import random

goal_number = random.randint(1,101)

while True :
    try:
        number = int(input("Guess the number between 1 to 100 > "))
        if number > goal_number :
            print("too high")
        elif number< goal_number:
            print("too low")
        elif number == goal_number:
            print("congratulations")
            break
    except ValueError:
        print("invalid")