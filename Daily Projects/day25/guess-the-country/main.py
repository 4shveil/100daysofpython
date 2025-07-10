import turtle as tt
import pandas as pd

screen = tt.Screen()
screen.title("U.S. States Game")
image = "/Users/Dell/Documents/python-stuff/day 25/guess-the-country/blank_states_img.gif"
screen.addshape(image)
tt.shape(image)
screen.setup(800, 800)

tim = tt.Turtle()
tim.penup()
tim.speed(-1)
tim.ht()

data = pd.read_csv("/Users/Dell/Documents/python-stuff/day 25/guess-the-country/50_states.csv")
states = data.state.to_list()

game_is_on = True

while game_is_on:
    if not states:
        game_is_on = False
        break
    
    answer_state = screen.textinput("Guess the state", "What's another state's name?").title()

    if answer_state in states:
        x = data[data.state == answer_state]["x"]
        y = data[data.state == answer_state]["y"]
        tim.goto(int(x), int(y))
        tim.write(arg=answer_state)
        ans_state_index = states.index(answer_state)
        states.pop(ans_state_index)
    else:
        print("You either already guessed that one or it doesn't exist")

tt.mainloop()
