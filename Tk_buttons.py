from tkinter import *

root = Tk()

#thelabel = Label(root, text="Faraz")
#thelabel.pack()

frame = Frame(root)
button1 = Button(frame, text="Play")
button2 = Button(frame, text="Menu")
button3 = Button(frame, text="Exit")


button1.pack()
button2.pack(side = LEFT)
button3.pack()

frame.pack()

root.mainloop()