import pandas
from turtle import Turtle, Screen


def score_print(score, x, y):
    turtle = Turtle()
    screen = Screen()
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(int(x), int(y))
    turtle.write(score, align="left", font=("Arial", 15, "normal"))
    screen.tracer(0)



def read_data(user_name):
    user_csv = pandas.read_csv(f"user_files/{user_name}.csv")

    for i, row in user_csv.iterrows():
        user_home_score = row["Home Score"]
        user_home_x = row["Home X"]
        user_home_y = row["Home Y"]
        user_away_score = row["Away Score"]
        user_away_x = row["Away X"]
        user_away_y = row["Away Y"]

        score_print(user_home_score, user_home_x, user_home_y)
        score_print(user_away_score, user_away_x, user_away_y)
