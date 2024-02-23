import turtle

def draw_flower(name, message):
    t = turtle.Turtle()
    s = turtle.Screen()
    s.bgcolor("black")
    t.pensize(2)
    colors = ["purple", "blue", "green", "yellow", "orange"]

    t.speed(0)
    for i in range(150):
        t.pencolor(colors[i % len(colors)])
        t.circle(190 - i, 90)
        t.lt(90)
        t.circle(190 - i, 90)
        t.lt(18)

    t.penup()
    t.goto(0, 300)
    t.pendown()
    t.write(f"Dear {name},", align="center", font=("Script MT Bold", 40, "italic"))
    t.penup()
    t.goto(0, 250)
    t.write(f"{message}", align="center", font=("Script MT Bold", 40, "italic"))

    turtle.done()

person_name = input("Enter the name of the person: ")
person_message = input("Enter the message for them: ")
draw_flower(person_name, person_message)