#Ask the user to enter their first name and then display the length of their first name. Then ask for their surname and display the length of their surname. Join their first name and surname together with a space between and display the result. Finally, display the length of their full name (including the space). 

from tkinter import *
import random

def click():
    num = random.randint(1,6)

    answer["text"] = num


window = Tk()

window.title("Roll a dice")

window.geometry("100x120")

button1 = Button(text = "Roll",command = click)
    
button1.place(x = 30,y = 30,height = 25,width = 50)

answer = Message(text = "")

answer.place(x = 40,y = 70,height = 25,width = 30)
                 
window.mainloop()