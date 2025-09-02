import turtle
import time
import random

WIDTH, HEIGTH = 500, 500
COLORS = ["red", "blue", "orange", "yellow", "purple", "black", "cyan"]


def get_number_of_turtles():
    racers = 0
    while True:
        racers = input("Enter the racer_Turtles (2-10): ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Input is not numeric.. Try again")
            continue
        if racers < 2 or racers > 10:
            print(f"Number not in range... Try again ")
        else:
            return racers


def race(colors):
    turtles = create_turtle(colors)

    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)

        x, y = racer.pos()
        if y >= HEIGTH // 2 - 10:
            return colors[turtles.index(racer)]


def create_turtle(colors):
    turtles = []
    spacingx = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape("turtle")
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH // 2 + (i + 1) * spacingx, -HEIGTH // 2 + 20)
        racer.pendown()
        turtles.append(racer)

    return turtles


def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGTH)
    screen.title("Turtle Racing!")


racers = get_number_of_turtles()
init_turtle()

random.shuffle(COLORS)
colors = COLORS[:racers]

winner = race(colors)
print("The winner is the turtle with color:", winner)
time.sleep(5)

""" 
racer = turtle.Turtle()
racer.speed(1)
racer.penup()
racer.shape("turtle")
racer.color("Red")
racer.forward(100)
racer.left(90)
racer.pendown()
racer.forward(100)
racer.right(90)
racer.backward(100)
time.sleep(5)

racer2 = turtle.Turtle()
racer2.speed(1)
racer2.penup()
racer2.shape("turtle")
racer2.color("cyan")
racer2.forward(150)
racer2.left(90)
racer2.pendown()
racer2.forward(150)
racer2.right(90)
racer2.backward(100)
time.sleep(5)
 """
