from tkinter import *

window = Tk()
window.title("Miles to Kilometers")
window.minsize(width=300, height=100)
window.config(padx=20, pady=20)

equivalent = Label(text="Is equal to: ", font=("Arial", 16, "normal"))
equivalent.grid(row=1, column=0)

label_miles = Label(text="Miles", font=("Arial", 16, "normal"))
label_miles.grid(row=0, column=2)

label_km = Label(text="Km", font=("Arial", 16, "normal"))
label_km.grid(row=1, column=2)

answer = Label(text="0", font=("Arial", 16, "normal"))
answer.grid(row=1, column=1)

input = Entry(width=10)
input.grid(row=0, column=1)


def convert():
    miles = int(input.get())
    km = miles * 1.60934
    answer.config(text=km)


button = Button(text = "Convert", command=convert)
button.grid(row=2, column=1)


window.mainloop()