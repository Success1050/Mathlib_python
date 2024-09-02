import random

type_number= input("type a number? ")
guesses= 0
correct_guess= 0

if type_number.isdigit():
    type_number = int(type_number)
    if type_number <= 0:
        print("enter a number greater than 0 next time")
        quit()

else:
    print("enter a number not a string")
    quit()

# random_number= random.randint(0, type_number)



while True:
    guesses += 1
    random_number = random.randint(0, type_number)
    try:
        user_input = int(input("Make a guess? "))
        if user_input > type_number:
            print("your guess should not be more than your stated numer")
            quit()
    except ValueError:
        print("please enter a number")
        continue

    if user_input == random_number:
        correct_guess+= 1
        print("you got it right")
        break

    else:
        print("you got it wrong")

    print(f"your guess: {user_input}")
    print(f"computer guess: {random_number}")

print(f"you correctly guessed {str(correct_guess)} out of {str(guesses)}")