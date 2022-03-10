from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=400, height=300)
window.config(padx=20, pady=20)

def miles_to_km():
    miles_val = float(miles_input.get())
    km_val = round(miles_val * 1.60934, 3)
    km_value.config(text=f"{km_val}")


# Create Label
is_equal_to_label = Label(text="is equal to", font=("Arial", 16, "bold"))
is_equal_to_label.grid(column=1, row=2)
is_equal_to_label.config(padx=10, pady=10)

# Create Input
miles_input = Entry(width=20)
miles_input.grid(column=2, row=1)

# Create label
miles_label = Label(text="Miles", font=("Arial", 16, "bold"))
miles_label.grid(column=3, row=1)


# Create Label
km_value = Label(text="0", font=("Arial", 16, "bold"))
km_value.grid(column=2, row=2)

# Create Label
km_label = Label(text="Km", font=("Arial", 16, "bold"))
miles_label.grid(column=3, row=2)

# Create calc button
button = Button(text="Calculate", command=miles_to_km)
button.grid(column=2, row=3)


window.mainloop()

