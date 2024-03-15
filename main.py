import pandas
import turtle
from turtle import Turtle, Screen

screen = Screen()
screen.title("USA States Game")
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

# Read file
states = pandas.read_csv('50_states.csv')
all_states = list(states['state'])

score = 0
guessed_states = []

while len(guessed_states) < 50:
    screen.delay(2)
    state_guess = screen.textinput(f"{score}/50 States Correct", "Input a state name:")
    user_state = state_guess.title()

    if user_state == 'Exit':
        # Write missing states to a file
        missing_states = [state for state in all_states if state not in guessed_states]
        # Creating a DataFrame and writing to CSV
        pandas.DataFrame(missing_states, columns=['Missing States']).to_csv('states_to_learn.csv', index=False)
        break
    if user_state in all_states and user_state not in guessed_states:
        # Create a turtle and write the State to the corresponding position
        turtle = Turtle()
        turtle.penup()
        turtle.hideturtle()
        score += 1
        guessed_states.append(user_state)
        # Get the row information of the state that the user correctly guessed, then access the x,y coordinates
        coordinates = states[states.state == user_state]
        turtle.goto(int(coordinates['x']), int(coordinates['y']))
        turtle.write(user_state, font=('Courier', 8, 'normal'))
