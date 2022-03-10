from tkinter import *

# Like screen in turtle
window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)


def button_clicked():
    my_label.config(text=f"{input.get()}")
    #  or
    #  my_label["text"] = "New text value"


# Create Label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

# Create button
button = Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)

# New button
button = Button(text="New Button", command=button_clicked)
button.grid(column=2, row=0)

# Create Entry
input = Entry(width=10)
input.grid(column=3, row=2)


window.mainloop()
