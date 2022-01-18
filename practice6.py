from tkinter import *
root = Tk()
root.geometry("444x233")
root.title("My GUI with rocky")

# Important Label Options
# text - adds the text
# bd - background
# fg - foreground
# font - sets the font
# 1. font=("comicsansms", 19, "bold")
# 2. font="comicsansms 19 bold"
# padx - x padding
# pady - y padding
# relief - border styling - SUNKEN, RAISED, GROOVE, RIDGE

title_label = Label(text = '''Abdul Rashid Salim Salman Khan (pronounced [səlˈmaːn ˈxaːn]; Hindi: About this \nsoundpronunciation (help·info); 27 December 1965)[5] is \nan Indian film actor, producer, occasional singer and \n television personality. In a film career spanning over \n \nthirty years, Khan has received numerous awards, \nincluding two National Film Awards as a film producer, and two Filmfare Awards for acting.[6] He is cited in the \nmedia as one of the most commercially successful actors of\n both world and Indian cinema.[7][8] Forbes included him \nin their 2015 list of Top-Paid 100 Celebrity Entert
\n ainers in world; Khan tied with Amitabh Bachchan for ''', bg ="blue", fg = "white", padx=13, pady="94", font="comicsansms 9 bold", borderwidth=3, relief=SUNKEN)


# Important Pack options
# anchor = nw
# side =top, bottom, left, right
# fill
# padx
# pady

# title_label.pack(side=BOTTOM, anchor ="sw", fill=X)
title_label.pack(side=LEFT,  fill=Y, padx=34, pady=34)

title_label.pack()

root.mainloop()