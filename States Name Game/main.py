import turtle
import pandas

data = pandas.read_csv("50_states.csv")

listed_states = data['state'].to_list()

states_answered = []

marker = turtle.Turtle()

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)


def mark_states(state_name):
    row = data[data['state'] == state_name].iloc[0]
    x, y = row['x'], row['y']
    marker.hideturtle()
    marker.penup()
    marker.goto(x, y)
    marker.write(state_name, align='center')


while len(states_answered) < 50:
    answer_state = screen.textinput(title=f"{len(states_answered)}/50 States Correct",
                                    prompt="What's another state's name?").title()

    if answer_state == "Exit":
        missing_states_list = [state for state in listed_states if state not in states_answered]
        new_data = pandas.DataFrame(missing_states_list)
        new_data.to_csv("States_to_learn.csv")
        break
    if answer_state in listed_states:
        if answer_state not in states_answered:
            states_answered.append(answer_state)
            mark_states(answer_state)
        else:
            print("You've already typed this state")
    else:
        print("Sorry this is not a U.S. State. Try Again.")

turtle.mainloop()
