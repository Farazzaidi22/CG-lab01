from tkinter import *

root = Tk()
photo = PhotoImage(file ='C:\\Users\\Faraz_0hm6\\OneDrive\\Desktop\\basketball.png')

#def key(event):
 #   print ("pressed", repr(event.char))

def callback(event):
    canvas.create_image(event.x, event.y, image = photo)
    #canvas.create_image(0,0, image= photo, anchor= NW)
    #print ("clicked at", event.x, event.y)
 
canvas= Canvas(root, width=1000, height=1000, bg= 'blue')
#canvas.bind("<Key>", key)
canvas.bind("<Button-1>", callback)
canvas.pack()

root.mainloop()