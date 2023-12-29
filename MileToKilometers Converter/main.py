from tkinter import *


def conversion():
    result = int(miles_entry.get()) * 1.6
    result = round(result)
    result_label.config(text=f"{result}")


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=50, pady=50)

# Miles Entry
miles_entry = Entry(width=10)
miles_entry.grid(column=1, row=0)

# Miles Text
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

# Equal to Text
equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

# Converted Result
result_label = Label(text="0")
result_label.grid(column=1, row=1)

# Km Text label
miles_label = Label(text="Km")
miles_label.grid(column=2, row=1)

# Calculate Button
button = Button(text="Calculate",command=conversion)
button.grid(column=1, row=2)

window.mainloop()
