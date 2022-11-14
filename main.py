import pandas
import pyperclip
from turtle import Turtle, Screen
from background import Background

turtle = Turtle()
turtle.hideturtle()
background = Background()
screen = Screen()

"""Printing Score to Image"""


def score_print(score, x, y):
    turtle.penup()
    turtle.goto(int(x), int(y))
    turtle.write(score, align="left", font=("Arial", 15, "normal"))



"""Reading CSV Data"""
data = pandas.read_csv("data/world_cup_fixtures.csv")

home_country = data["Home Team"].tolist()
away_country = data["Away Team"].tolist()
country_group = data["Group"].tolist()

score_input = True

"""Add X,Y Coordinates to Data File"""

x_cor = []
y_cor = []

home_score_csv_info = []
away_score_csv_info = []
home_team_csv = []
away_team_csv = []
team_group_csv = []

def get_coor(x, y):
    pyperclip.copy(" ")
    x_cor.append(x)
    y_cor.append(y)
    pyperclip.copy(str(x) + " " + str(y))
    print(x, y)

# user_mode = screen.textinput(title="World Cup Sweepstakes",
                                 prompt="Are you ready to join the World Cup Fantasy League?")

user_name = screen.textinput(title="World Cup Sweepstakes",
                             prompt="What is your name?")

while score_input:

    home_country_name = screen.textinput(title="World Cup Sweepstakes",
                                         prompt="Which Home Team you want to input score? ").title()
    away_country_name = screen.textinput(title="World Cup Sweepstakes", prompt="Which Team would they be playing? ").title()
    home_score = screen.textinput(title="World Cup Sweepstakes",
                                  prompt=f"What would be {home_country_name}'s score against {away_country_name}?")
    away_score = screen.textinput(title="World Cup Sweepstakes",
                                  prompt=f"What would be {away_country_name}'s score against {home_country_name}?")

    """Locate Match and map coordinates in CSV"""

    locate_row = data.loc[(data["Home Team"] == home_country_name) & (data["Away Team"] == away_country_name)]
    home_locate_x = locate_row["Home X"].astype(int)
    home_locate_y = locate_row["Home Y"].astype(int)
    away_locate_x = locate_row["Away X"].astype(int)
    away_locate_y = locate_row["Away Y"].astype(int)
    group_locate = locate_row["Group"]

    """Print Score to map via coordinates"""

    score_print(home_score, home_locate_x, home_locate_y)
    score_print(away_score, away_locate_x, away_locate_y)

    """Collating Data to put in lists"""

    home_team_csv.append(home_country_name)
    away_team_csv.append(away_country_name)
    home_score_csv_info.append(home_score)
    away_score_csv_info.append(away_score)
    team_group_csv.append(group_locate)
    continue_input = screen.textinput(title="World Cup Sweepstakes",
                                      prompt="Do you want to continue?").lower()
    """Continue"""
    if continue_input == "yes":
        score_input = True
    else:
        score_input = False

"""Save Data to User Name CSV"""
saved_user_data = {
                "Home Team": home_team_csv,
                "Home Team Score": home_score_csv_info,
                "Away Team": away_team_csv,
                "Away Team Score": away_score_csv_info,
                "Group": team_group_csv
                }
saved_user = pandas.DataFrame(saved_user_data)
saved_user.to_csv(f"user_files/{user_name}.csv")

# screen.mainloop()
