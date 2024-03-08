#Ask the user to enter their first name and then display the length of their first name. Then ask for their surname and display the length of their surname. Join their first name and surname together with a space between and display the result. Finally, display the length of their full name (including the space). 

from tkinter import *

def click():
    name = textbox1.get()

    message = str("Hello", name)

    textbox2["text"] = message


window = Tk()

window.title("Names")

window.geometry("500x250")

window.configure(background="black")

label1 = Label(text = "Enter your name: ")

label1.place(x = 30,y = 20)

textbox1 = Entry(text = "")
    
textbox1.place(x = 150,y = 20,height = 25,width = 200)

textbox1["justify"] = "center"

textbox1.focus()

button1 = Button(text = "Press me",command = click)
    
button1.place(x = 30,y = 50,height = 25,width = 110)

textbox2 = Entry(text = "")
    
textbox2.place(x = 150,y = 50,height = 25,width = 200)

textbox2["bg"] = "white"
    
textbox2["fg"] = "black"

window.mainloop()