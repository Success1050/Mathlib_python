
name= input("What is your name? ")
print("you are welcome", name, "to the game")

answer= input(f"{name}, you are welcome to the game. You are left with two options left/ right").strip().lower()
if answer == "left":
    answer = input("you have come across a river and a rock, should you swim or climb? ").strip().lower()
    if answer == "swim":
        print("you swam and got eaten by a shark")
    elif answer == "climb":
        print("you climbed the rock and fell down")
    else:
        print("invalid option only choose swim or climb")

elif answer == "right":
    answer = input("you have come across a valley filled with gold, should you pick or skip it yes/no ").strip().lower()
    if answer == "yes":
        print("you picked the gold and won")
    elif answer == "no":
        print("you didn't pick the gold and you loose")
    else: print("invalid option only choose swim or climb")

else:
    print("invalid option")

