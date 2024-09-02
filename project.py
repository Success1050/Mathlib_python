import random

def roll():
    max_num= 4
    min_num= 1
    roll= random.randint(min_num, max_num)
    return roll

while True:
    player= input("Enter the number of player for the game. (2-4): ")
    if player.isdigit():
        player= int(player)
        if 2 <= player <= 4:
            break
        else:
            print("must be between 2-4")
    else:
        print("invalid! enter a valid number")


max_score= 50
player_score= [0 for i in range(player)]
print(player_score)

while max(player_score) < max_score:   
    for player_index in range(player):
        print(F"your total score is {player_score[player_index]}")
        print(f"Player {player_index + 1} your turn has started")
        current_score= 0 
        while True:
            should_play= input("do you want to play?(y): ")
            if should_play.lower() != "y":
                break

            value = roll()
            if value == 1:
                print("you rolled a 1. your turn is over")
                current_score = 0
                break
            else:
                current_score += value 
                print("you rolled:", value)
                
            print("your score is:", current_score)
        
        player_score[player_index] += current_score
        print(f"your total score is: {player_score[player_index]}")
        

max_number= max(player_score)
winning_player= player_score.index(max_number)

print(f"the winner is {player_score[player_index]} with a score of {max_number}")




