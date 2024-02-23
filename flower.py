import turtle

def draw_flower(name, message):
    t = turtle.Turtle()
    s = turtle.Screen()
    s.bgcolor("black")
    t.pensize(2)
    colors = ["purple", "blue", "green", "yellow", "orange"]

    t.speed(0)

    # Drawing the flower
    for i in range(150):
        t.pencolor(colors[i % len(colors)])
        t.circle(190 - i, 90)
        t.lt(90)
        t.circle(190 - i, 90)
        t.lt(18)

    # Writing the name and the message
    t.penup()
    t.goto(0, 300)
    t.pendown()
    t.write(f"Dear {name},", align="center", font=("Script MT Bold", 40, "italic"))
    t.penup()
    t.goto(0, 250)
    t.write(f"{message}", align="center", font=("Script MT Bold", 40, "italic"))

    # Drawing the Heart
    t.penup()
    t.goto(0, -375)
    t.pendown()
    t.color("red")
    t.begin_fill()
    t.left(50)
    t.forward(100)
    t.circle(25, 200)
    t.right(140)
    t.circle(25, 200)
    t.forward(100)
    t.end_fill()

    t.hideturtle()

    turtle.done()

person_name = input("Enter the name of the person: ")
person_message = input("Enter the message for them: ")
draw_flower(person_name, person_message)