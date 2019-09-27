from tkinter import *
import time

root = Tk()

#saving images
photo_ball = PhotoImage(file ='C:\\Users\\Faraz_0hm6\\OneDrive\\Desktop\\basketball.png')
photo_hoop = PhotoImage(file ='C:\\Users\\Faraz_0hm6\\OneDrive\\Desktop\\hoop.png')

#creating a canvas
canvas = Canvas(root,width =800, height =500, bg= 'white')
canvas.pack()
#setting hoop as bg image
canvas.create_image(0,0, image= photo_hoop, anchor= NW)

#def anim():
    

#function to instantiation basketballs image
def callback(event):
    img=canvas.create_image(event.x, event.y, image = photo_ball)
    #print ("clicked at", event.x, event.y)
    for x in range(0,60):
        canvas.move(img,0,7)
        root.update()
        time.sleep(0.05)


canvas.bind("<Button-1>", callback)

canvas.pack()

root.mainloop()