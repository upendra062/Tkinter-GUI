from tkinter import *
root = Tk()
root.geometry("655x444")
root.title("programmerRocky - Title of My GUI")
root.wm_iconbitmap("photo.jpg")
root.configure(background="grey")

width = root.winfo_screenwidth()
height = root.winfo_screenheight()

print(f"{width}x{height}")
Button(text="Close Ritu badmash", command = root.destroy).pack()

root.mainloop()