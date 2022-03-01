from tkinter import *
import random

win = Tk()
win.title('PythonGuides')
#win.geometry('600x400')
win.config(bg='#5671A6')

random_num = random.randint(0, 20)
chance = 5
var = IntVar()
display = StringVar()

def check_guess():
    global random_num
    global chance
    usr_input = var.get()
    if chance > 0:
        if usr_input == random_num:
            msg = f'You won! {random_num} is the right answer.'
        elif usr_input > random_num:
            chance -= 1
            msg = f'{usr_input} is greater. You have {chance} attempt left.'
        elif usr_input < random_num:
            chance -= 1
            msg = f'{usr_input} is smaller. You have {chance} attempt left.'
        else:
            msg = 'Something went wrong!'
    else:
        msg = f'You Lost! you have {chance} attempt left.'

    display.set(msg)


Label(
    win,
    text='Number Guessing Game',
    font=('sans-serif', 20),
    relief=SOLID,
    padx=10,
    pady=10,
    bg='#F27D16'
).pack(pady=(10, 0))

Entry(
    win,
    textvariable=var,
    font=('sans-serif', 18)
).pack(pady=(50, 10))

Button(
    win,
    text='Submit Guess',
    font=('sans-serif', 18),
    command=check_guess
).pack()

Label(
    win,
    textvariable=display,
    bg='#5671A6',
    font=('sans-serif', 14)
).pack(pady=(20,0))


win.mainloop()