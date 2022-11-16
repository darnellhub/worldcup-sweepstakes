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
home_x_cor = []
away_x_cor = []
home_y_cor = []
away_y_cor = []
home_team_csv = []
away_team_csv = []
team_group_csv = []


def get_coor(x, y):
    pyperclip.copy(" ")
    x_cor.append(x)
    y_cor.append(y)
    pyperclip.copy(str(x) + " " + str(y))
    print(x, y)

"""Initial questions"""

user_mode = screen.textinput(title="World Cup Sweepstakes",
                             prompt="Do you want to input scores or read previous scores? Input/Read").lower()

user_name = screen.textinput(title="World Cup Sweepstakes",
                             prompt="What is your name?").lower()

if user_mode == "input":
    while score_input:
        """Input Dialog Boxes"""
        home_country_name = screen.textinput(title="World Cup Sweepstakes",
                                             prompt="Which Home Team you want to input score? ").title()
        away_country_name = screen.textinput(title="World Cup Sweepstakes",
                                             prompt="Which Team would they be playing? ").title()
        home_score = screen.textinput(title="World Cup Sweepstakes",
                                      prompt=f"What would be {home_country_name}'s score against {away_country_name}?")
        away_score = screen.textinput(title="World Cup Sweepstakes",
                                      prompt=f"What would be {away_country_name}'s score against {home_country_name}?")

        """Locate Match and map coordinates in CSV"""
        if home_country_name in home_country and away_country_name in away_country:
            locate_row = data.loc[(data["Home Team"] == home_country_name) & (data["Away Team"] == away_country_name)]
            home_locate_x = locate_row["Home X"].astype(int)
            home_locate_y = locate_row["Home Y"].astype(int)
            away_locate_x = locate_row["Away X"].astype(int)
            away_locate_y = locate_row["Away Y"].astype(int)
            group_locate = locate_row["Group"].apply(str)

            """Print Score to map via coordinates"""
            # print(locate_row["Away Y"])
            score_print(home_score, home_locate_x, home_locate_y)
            score_print(away_score, away_locate_x, away_locate_y)

            """Collating Data to put in lists"""
            home_x_cor.append(int(home_locate_x))
            home_y_cor.append(int(home_locate_y))
            away_x_cor.append(int(away_locate_x))
            away_y_cor.append(int(away_locate_y))
            home_team_csv.append(home_country_name)
            away_team_csv.append(away_country_name)
            home_score_csv_info.append(int(home_score))
            away_score_csv_info.append(int(away_score))
            team_group_csv.append(str(group_locate))
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
                    "Home Score": home_score_csv_info,
                    "Home X": home_x_cor,
                    "Home Y": home_y_cor,
                    "Away Team": away_team_csv,
                    "Away Score": away_score_csv_info,
                    "Away X": away_x_cor,
                    "Away Y": away_y_cor,
                    "Group": team_group_csv
                }
                saved_user = pandas.DataFrame(saved_user_data)
                # print(saved_user)
                saved_user.to_csv(f"user_files/{user_name}.csv", index=False)
        else:
            score_input = False
            print("Wrong Spelling")
elif user_mode == "read":
    user_csv = pandas.read_csv(f"user_files/{user_name}.csv")
    user_dict = user_csv.to_dict()

    print(user_dict)


    saved_user_home_team = user_csv["Home Team"]
    saved_user_home_score = user_csv["Home Score"]
    saved_user_away_team = user_csv["Away Team"]
    saved_user_away_score = user_csv["Away Score"]
    saved_user_home_x = user_csv["Home X"]
    saved_user_home_y = user_csv["Home Y"]
    saved_user_away_x = user_csv["Away X"]
    saved_user_away_y = user_csv["Away Y"]




    for val in saved_user_away_score:
        user_away_score = val

    for val in saved_user_away_y:
        user_away_y = val

    for val in saved_user_away_x:
        used_away_x = val

    for val in saved_user_home_score:
        user_home_score = val

    for val in saved_user_home_x:
        user_home_x = val

    for val in saved_user_away_y:
        user_home_y = val



    score_print(user_home_score, user_home_x, user_home_y)
    score_print(user_away_score, used_away_x, user_away_y)


    # print(int(saved_user_home_score))

    # saved_user_home_score = 1
    # saved_user_home_x = -374
    # saved_user_home_y = 235
    # saved_user_away_score = 2
    # saved_user_away_x = -354
    # saved_user_away_y = 235




    # print(saved_user_home_score,saved_user_away_score)
    #

screen.mainloop()
