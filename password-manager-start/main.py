from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
FONT_LABEL = ("Courier", 10, "bold")



# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for char in range(randint(8, 10))]
    password_symbols = [choice(symbols) for char in range(randint(2, 4))]
    password_numbers = [choice(numbers) for char in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)


    password = "".join(password_list)

    password_input.delete(0, "end")
    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_pass():
    new_data = {
        website_input.get(): {
            "email": user_input.get(),
            "password": password_input.get()
        }
    }
    if len(password_input.get()) == 0 or len(user_input.get()) == 0 or len(website_input.get()) == 0:
        messagebox.showwarning(message="You left some details blank, kindly check your entry.")
    else:
        save_pass = messagebox.askokcancel(title=website_input.get(), message=f"Are you okay with these details? "
                                                                  f"Username/Email: {user_input.get()} Password: "
                                                                   f"{password_input.get()}")
        if save_pass:
            try:
                with open("data.json", mode="r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", mode="w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)
                with open("data.json", mode="w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                website_input.delete(0, "end")
                password_input.delete(0, "end")

#---------------------------search password -------------------------------------------------#


def search_pass():
    try:
        with open("data.json", mode="r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="File not found", message="No data file found. Generate a password first.")
    else:
        if website_input.get() in data:
            messagebox.showinfo(title=website_input.get(), message=f"Username: {data[website_input.get()]['email']}"
                                                             f"\nPassword: {data[website_input.get()]['password']}")
        else:
            messagebox.showinfo(title="No Data Found", message="No details for the website exists")




# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
aws_img = PhotoImage(file="aws.jpg")
canvas.create_image(100, 300, image=aws_img)
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)


### labels

website_label = Label(text="Website:", font=FONT_LABEL)
website_label.grid(row=1, column=0)
user_label = Label(text="Email/Username:", font=FONT_LABEL)
user_label.grid(row=2, column=0)
password_label = Label(text="Password:", font=FONT_LABEL)
password_label.grid(row=3, column=0)


### entries
website_input = Entry(width=29)
website_input.grid(row=1, column=1)
website_input.focus()
user_input = Entry(width=49)
user_input.grid(row=2, column=1, columnspan=3)
user_input.insert(0, "")
password_input = Entry(width=29)
password_input.grid(row=3, column=1)


search_pass = Button(text ="Search", command=search_pass, width=15)
search_pass.grid(row=1, column=2)

generate_pass = Button(text ="Generate Password", command=gen_pass, width=15)
generate_pass.grid(row=3, column=2)

add_button = Button(text="Add", command=add_pass, width=45)
add_button.grid(row=4, column=1, columnspan=3)

window.mainloop()