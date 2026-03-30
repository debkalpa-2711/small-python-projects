import random

choice = ('r','p','s')
emoji = {
    'r' : '🪨' ,
    'p' : '📃' ,
    's' : '✂️'
}

while True:
    userChoice = input("Enter Rock or Paper or Scissors (r/p/s) > ").lower()
    if userChoice not in choice:
        print("Invalid Input ")
        continue

    computerChoice = random.choice(choice)

    print(f" You choose > {emoji[userChoice]} ")
    print(f" Computer Choose > {emoji[computerChoice]}")

    if userChoice == 'r' and computerChoice == 's' or userChoice == 'p' and computerChoice == 'r' or userChoice == 's' and computerChoice == 'p' :
        print("The user wins")
        
    elif userChoice == computerChoice :
        print("Its a tie ")
    else :
        print("Computer Won ")