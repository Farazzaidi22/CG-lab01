from tkinter import *
import time

root = Tk()

basketball = PhotoImage( file = "C:\\Users\\Faraz_0hm6\\OneDrive\\Desktop\\basketball.png")


varr = Canvas(root, width = 1000, height = 600, bg= 'blue')

def onclick(event):
        img = varr.create_image(event.x, event.y, image = basketball)
        for i in range(0,60):
                varr.move(img , 0,  7)
                varr.update()
                time.sleep(0.05)



varr.bind("<Button-1>", onclick)
varr.pack()

root.mainloop()