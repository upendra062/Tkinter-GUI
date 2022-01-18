from tkinter import *
from PIL import Image, ImageTk #ImageTk python library k andar ek function hai jo ki madad karta hai Tkinter k ander jpg files ko lene ki#

upendra_root = Tk()

upendra_root.geometry("1255x944")

# photo = PhotoImage(file="")

# For Jpg Images
image = Image.open("photo.jpg")
photo = ImageTk.PhotoImage(image)

papa_label = Label(image=photo)
papa_label.pack()

upendra_root.mainloop()




# (pip install pillow) pillow means python image library