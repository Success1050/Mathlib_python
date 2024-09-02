# import os
# import shutil
# import docs
# from docs import hello,bye 
# import random
# hello()
# bye()
# help("modules")

# sourse= "text.txt"
# destination= "C:\\Users\\Success Emmanuel\\3D Objects\\success.txt"

# try:
#     if os.path.exists(destination):
#         print("file already exists")
#     else: os.replace(sourse, destination)
# except FileNotFoundError: print("file not found")

# try: 
#     if os.path.exists("text.txt"):
#         # shutil.rmtree("folder")
#         # os.rmdir('folder')
#         os.remove('text.txt')
#     else: print("file has been removed already")
# except PermissionError: print("you dont have permission")
# except OSError: print("it needs to be an empty folder")

# computerScore = 0
# playerScore = 0
# while True:
#     choice= ["rock", "paper", "scissors"]
#     computer= random.choice(choice)
#     player= None

#     while player not in choice:
#        player= input("rock, paper, scissors? ").lower()
#        if player == computer:
#            print(f"computer: {computer}")
#            print(f"player: {player}")
#            print("tie")
#            computerScore += 1
#            playerScore += 1
#        elif player== "rock":
#             if computer== "scissors":
#                 print(f"computer: {computer}")
#                 print(f"player: {player}")
#                 print("you win")
#                 playerScore+= 1
#             if computer== "paper":
#                 print(f"computer: {computer}")
#                 print(f"player: {player}")
#                 print("you win")
#             playerScore+= 1
#        elif player== "paper":
#            if computer== "scissors":
#                 print(f"computer: {computer}")
#                 print(f"player: {player}")
#                 print("you lose")
#                 computerScore+= 1
#            if computer== "rock":
#                 print(f"computer: {computer}")
#                 print(f"player: {player}")
#                 print("you lose")
#                 computerScore+= 1
#        elif player== "scissors":
#            if computer== "rock":
#                 print(f"computer: {computer}")
#                 print(f"player: {player}")
#                 print("you lose")
#                 computerScore+= 1
#            if computer== "paper":
#                 print(f"computer: {computer}")
#                 print(f"player: {player}")
#                 print("you win")
#                 playerScore+= 1

#     print(f"computer score: {computerScore}")
#     print(f"player score: {playerScore}")
#     text= input("Do you want to continue YES/NO?: ").lower()
#     if text != "yes":
#         break

