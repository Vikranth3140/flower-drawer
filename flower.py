import turtle

class FlowerDrawer:
    def __init__(self):
        self.t = turtle.Turtle()
        self.s = turtle.Screen()
        self.s.bgcolor("black")
        self.t.pensize(2)
        self.colors = ["purple", "blue", "green", "yellow", "orange"]

    def draw_flower(self, name, message):
        self.t.speed(0)

        # Drawing the flower
        for i in range(150):
            self.t.pencolor(self.colors[i % len(self.colors)])
            self.t.circle(190 - i, 90)
            self.t.lt(90)
            self.t.circle(190 - i, 90)
            self.t.lt(18)

        # Writing the name and the message
        self.t.penup()
        self.t.goto(0, 300)
        self.t.pendown()
        self.t.write(f"Dear {name},", align="center", font=("Script MT Bold", 40, "italic"))
        self.t.penup()
        self.t.goto(0, 250)
        self.t.write(f"{message}", align="center", font=("Script MT Bold", 40, "italic"))

        # Drawing the Heart
        self.t.penup()
        self.t.goto(0, -375)
        self.t.pendown()
        self.t.color("red")
        self.t.begin_fill()
        self.t.left(50)
        self.t.forward(100)
        self.t.circle(25, 200)
        self.t.right(140)
        self.t.circle(25, 200)
        self.t.forward(100)
        self.t.end_fill()

        self.t.hideturtle()

        turtle.done()

# Checking if name and message is not empty
def get_input(prompt):
    while True:
        try:
            user_input = input(prompt)
            if user_input.strip():
                return user_input
            else:
                print("Input cannot be empty. Please try again.")
        except KeyboardInterrupt:
            print("\nProgram terminated by user.")
            exit()

def main():
    print()
    print("Welcome to the Flower Drawer!")
    print()
    person_name = get_input("Enter the name of the person: ")
    person_message = get_input("Enter the message for them: ")

    flower_drawer = FlowerDrawer()
    flower_drawer.draw_flower(person_name, person_message)

if __name__ == "__main__":
    main()