import turtle
import pandas



screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# CSV Pandas
data = pandas.read_csv("50_states.csv")
state_list = data["state"].tolist()
print(state_list)


answer_state = screen.textinput(title="Guess the State", prompt="Whats another state's name")

is_guessing = True




def get_mouse_click_coor(x, y):
    print(x, y)
    
turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop()



