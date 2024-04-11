from turtle import Turtle, Screen
import random




def play():
    screen = Screen()
    screen.setup(width=1400, height=700)
    screen.bgpic("трасса.png")


    colors = ["red", "orange", "yellow", "green", "blue", "purple"]

    is_race_on = False
    user_choice = ""
    while True:
        user_choice += screen.textinput(title="What is your choice?", prompt="Which turtle will win the race? Enter you color: ").lower()
        if user_choice in colors:
            break
        else:
            continue
    y_position = + 152

    all_turtles = []
    for turtle_index in range(0, 6):
        new_turtle = Turtle(shape="turtle")
        new_turtle.speed(20)
        new_turtle.penup()
        new_turtle.color(colors[turtle_index])
        new_turtle.goto(x=-650, y=y_position)
        y_position -= 60
        all_turtles.append(new_turtle)
    if user_choice in colors:
        is_race_on = True

    while is_race_on:
        for turtle in all_turtles:
            if turtle.xcor() > 650:
                is_race_on = False
                winning_color = turtle.pencolor()
                massage = ""
                if winning_color == user_choice:
                    massage += f"You've win! The {winning_color} turtle is the winner!"
                else:
                    massage += f"You've lose! The {winning_color} turtle is the winner!"
                play_again = screen.textinput(title=f"{massage}", prompt="Do you want to play again? yes/no").lower()
                if play_again == "yes":
                    screen.clear()
                    play()
                else:
                    exit()
            rand_distance = random.randint(0, 20)
            turtle.forward(rand_distance)



    screen.exitonclick()



play()

