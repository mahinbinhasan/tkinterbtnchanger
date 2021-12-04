from tkinter import *
root = Tk()
root.title("Mahin Button Changer")
root.geometry("500x500")
root.configure(bg="white")
stop_button = PhotoImage(file='Images/1.png')
play_button = PhotoImage(file='Images/2.png')
y = 1
def play():
    global y
    if y %2!=0:
        y = y+1
        playbtn = Button(Control, image=stop_button, borderwidth=0, command=lambda: play())
        playbtn.grid(row=0, column=1)
    else:
        playbtn = Button(Control, image=play_button, borderwidth=0, command=lambda: play())
        playbtn.grid(row=0, column=1)
        y = y+1
Control = Frame(root)
Control.pack()

playbtn = Button(Control, image = play_button,borderwidth = 0,command = lambda: play())

playbtn.grid(row = 0,column = 1)


root.mainloop()
