import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import tkinter as tk
from tkinter import ttk

from PIL import ImageTk, Image

root = tk.Tk()
root.geometry('800x600')
root.title('Azimuth Indicator')
root.columnconfigure(index=0, weight=1)
#root.rowconfigure(index=0, weight=1)

cursor_var = tk.StringVar(value='')
lbl_position = ttk.Label(root, textvariable=cursor_var)
lbl_position.grid(row=0, column=0, pady=(10,0))

angle_var = tk.StringVar(value='')
lbl_angle = ttk.Label(root, textvariable=angle_var)
lbl_angle.grid(row=1, column=0, pady=10)

def get_theta(op,adj):
    theta = np.rad2deg(np.arctan(op/adj))
    return theta


def get_position(e):
    x = e.x - 200
    y = e.y - 200
    cursor_var.set(f"x={x}, y={y}")
    angle = np.round(get_theta(x,y),1)
    angle_var.set(angle)
    #print("Mouse is at %d, %d" %(x,y))


c = tk.Canvas(root, width=400, height=400, bg='black')
c.grid()

#c.create_line((199,200), (201,200), width=2, fill='red')
#c.create_line((200,199), (200,201), width=2, fill='red')

img1 = Image.open('circle2.png')
img1 = img1.resize((400,400))
img2 = ImageTk.PhotoImage(img1)
#c_image = tk.PhotoImage(file='circle.jpg')
c.create_image(
    (200,200),
    image=img2
)


#c.bind('<Motion>', get_position)
c.bind('<Button-1>', get_position)

root.mainloop()
