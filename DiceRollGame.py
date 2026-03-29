import random

while True:
    yesOrNo = input("Enter yes or no > (y/n) ").lower()
    if yesOrNo =="y":
        dise1 = random.randint(1,6)
        dise2 = random.randint(1,6)
        print(f"({dise1} , {dise2})")
    elif yesOrNo == "n" :
        print("thank you for playing > ")
        break
    else:
        print("Try again")