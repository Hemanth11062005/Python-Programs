#First GUI program. Creating a window

from tkinter import *

window = Tk()
window.geometry("420x420")
window.title("GUI window")
#icon = PhotoImage(file='logo.png')
#window.iconphoto(True,icon)
window.config(background="black")
window.mainloop()