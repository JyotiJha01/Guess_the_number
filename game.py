from tkinter import *
import random
import os

win = Tk()
win.config(bg='#5671A6')
win.geometry('600x400')
win.title("Number Guessing Game")

result = StringVar()
chances = IntVar()
chances1= IntVar()
choice= IntVar()
no=random.randint(1,20)
result.set('Hii, I am thinking of a number between 1 to 20.')
chances.set(5)
chances1.set(chances.get())

def fun():
  chances1.set(chances.get())
  if chances.get()>0:

    if choice.get() > 20 or choice.get()<0:
      result.set("You just lost 1 Chance")
      chances.set(chances.get()-1)
      chances1.set(chances.get())
    
    elif no==choice.get():
      result.set("Congratulation YOU WON!!!")
      chances.set(chances.get()-1)
      chances1.set(chances.get())
      
    elif no > choice.get():
      result.set("Your guess was too low: Guess a number higher ")
      chances.set(chances.get()-1)
      chances1.set(chances.get())
    elif no < choice.get():
      result.set(
          "Your guess was too High: Guess a number Lower ")
      chances.set(chances.get()-1)
      chances1.set(chances.get())
  else:
     result.set(
         "Game Over You Lost")

def restart():
  no=random.randint(1,20)
  result.set("Guess a number between 1 to 20 ")
  chances.set(5)
  chances1.set(chances.get())

ent1=Entry(win, textvariable=choice, width=3,
             font=('sans-serif', 50))
ent1.place(relx=0.5, rely=0.3, anchor=CENTER)

ent2 = Entry(win, textvariable=result, width=50,
             font=('sans-serif', 15))
ent2.place(relx=0.5, rely=0.7, anchor=CENTER)

ent3 = Entry(win, text=chances1, width=2,
             font=('sans-serif', 24), relief=SOLID)
ent3.place(relx=0.61, rely=0.85, anchor=CENTER)

msg = Label(win, text='Guess a number',
            font=('sans-serif', 25), relief=SOLID)
msg.place(relx=0.5, rely=0.09, anchor=CENTER)

msg2 = Label(win, text='Remaninig Chances',
             font=('sans-serif', 25) )
msg2.place(relx=0.3, rely=0.85, anchor=CENTER)

try_no = Button(win, width=8, text='TRY', font=(
    'sans-serif', 25), command=fun, relief=GROOVE)
try_no.place(relx=0.5, rely=0.5, anchor=CENTER)

win.mainloop()