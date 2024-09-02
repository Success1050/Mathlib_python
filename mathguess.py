import time
import random

def generate_question():
    MIN_VALUE= 2
    MAX_VALUE= 10
    OPERATORS= ["+", "-", "*"]
    LEFT= random.randint(MIN_VALUE, MAX_VALUE)
    RIGHT= random.randint(MIN_VALUE, MAX_VALUE)
    OPERATIONS= random.choice(OPERATORS)
    expr= str(LEFT) + OPERATIONS + str(RIGHT)
    answer = eval(expr)
    return expr, answer

wrong= 0
right= 0
num_of_trials= 10
input("Press enter to get started? " )

start_time= time.time()

for trial in range(num_of_trials):
    expr, answer= generate_question()
    while True:
        user_value= input(f"problem #{str(trial + 1)}, {expr} Enter your answer? ")
        if str(answer) == user_value:
            right += 1
            break
           
        else:
            wrong += 1
            break
    end_time= time.time()
    total_time=  round(end_time - start_time, 2)

print(f"Nice job. you finished in {total_time} with {right} right answers and {wrong} wrong answer. overall you scored and average of {(right/num_of_trials) * 100}%")