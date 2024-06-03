import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Games")

#show the image in turtle graphics
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("50_states.csv")
all_state = data.state.to_list()
#game_is_on =True
# while game_is_on:
#     answer_state = screen.textinput(title="Guess the state", prompt="what is the another state name?").capitalize()
#     csv_data = data[data.state == answer_state]
#     if csv_data.shape[0] > 0:
#         text = turtle.Turtle()
#         text.hideturtle()
#         text.penup()
#         text.goto(int(csv_data['x']), int(csv_data['y']))
#         text.write(answer_state, font=("Arial", 12, "normal"))

guessed_state = []

while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 state correct", prompt="what is the another state name?").capitalize()

    if answer_state == "Exit":
        missing_state = []
        for state in all_state:
            if state not in guessed_state:
                missing_state.append(state)
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("state_to_learn.csv")
        break
    if answer_state in all_state:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

#state to learn csv

