import turtle
import time
import random

WIDTH, HEIGHT = 500, 500
COLORS= ["red", "brown", "green", "orange", "blue", "cyan", "pink", "purple", "black", "gray"]

def num_of_racers():
    racers= 0
    while True:
        racers= input("Enter the number of racers (2 - 10): ")
        if racers.isdigit():
            racers= int(racers)
        else:
            print("input is invalid, enter a valid number")
            continue

        if 2 <= racers <= 10:
            return racers
        else:
            print("Enter number between 2 - 10")


def race(colors):
    turtles = create_turtles(colors)
    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)

            x, y = racer.pos()
            if y >= HEIGHT // 2  - 10:
                return colors[turtles.index(racer)]


def create_turtles(color):
    turtles = []
    spacingx= WIDTH // (len(colors) + 1)
    for i, color in enumerate(color):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape("turtle")
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 + (i + 1) * spacingx, -HEIGHT//2 + 20)
        racer.pendown()
        turtles.append(racer)

    return turtles

def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle race")

racers = num_of_racers()
init_turtle()

random.shuffle(COLORS)
colors= COLORS[:racers]
winning = race(colors)
print(f"the winner of the race is the {winning} turtle")


# for racer in range(racers):
#     racer = turtle.Turtle()
#     racer.speed(1)
#     racer.shape("turtle")
#     racer.color("red")
#     racer.penup()
#     racer.forward(100)
#     racer.left(90)
#     racer.forward(100)
#     racer.right(90)
#     racer.backward(100)

