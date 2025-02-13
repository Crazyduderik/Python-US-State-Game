import turtle
import pandas



screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

turtle2 = turtle.Turtle()
turtle2.hideturtle()
turtle2.penup()
turtle2.color("black")

# CSV Pandas
data = pandas.read_csv("50_states.csv")
state_list = data["state"].tolist()
# print(state_list)


correct_guessed = 0

# answer_state = screen.textinput(title="Guess the State", prompt="Whats another state's name")
# state_data = data[data.state == answer_state]
# x = state_data.x
# y = state_data.y
# print(f"x = {x}  and y = {y} coordinates")
guesses_left = 50

while guesses_left > 0 and correct_guessed < 50:
    answer_state = screen.textinput(title=f"{correct_guessed}/50 States Correct", prompt="Whats another state's name")
    
    
    if answer_state is None:
        break
    
    if answer_state in state_list:
        correct_guessed += 1
        state_data = data[data.state == answer_state]
        x = int(state_data.x)
        y = int(state_data.y)
        turtle2.goto(x, y)
        turtle2.write(answer_state, align="center", font=("Arial", 8, "normal"))
        state_list.remove(answer_state)
        
    else:
        guesses_left -= 1

if correct_guessed == 50:
    turtle2.goto(0, 0)
    turtle2.write("Congratulations! You've guessed all 50 States!", align="center", font=("Arial", 20, "bold"))
else:
    turtle2.goto(0, 0)
    turtle2.write(f"Game Over! Nice Try! You guessed {correct_guessed}/50 states.", align="center", font=("Arial", 20, "bold"))


# def get_mouse_click_coor(x, y):
#     print(x, y)
    
# turtle.onscreenclick(get_mouse_click_coor)

turtle.done()



