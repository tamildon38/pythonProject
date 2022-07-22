from tkinter import *
master =Tk()
def callback():
    a=5
    b=10
    c=a+b
    print(c)
    print("you have clicked the button")
btn = Button(master,text='ok',command = callback)
btn.pack()
mainloop()



