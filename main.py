from tkinter import *
from tkinter import messagebox
import pandas
import random
import pyperclip

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


try:
    data = pandas.read_csv("data.csv")
except FileNotFoundError:
    web_list = []
    user_list = []
    passw_list = []
else:
    web_list = data.website.to_list()
    user_list = data.user.to_list()
    passw_list = data.password.to_list()


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_pass():
    rand_letters = random.choices(letters, k=random.randint(5, 8))
    rand_numbers = random.choices(numbers, k=random.randint(2, 5))
    rand_symbols = random.choices(symbols, k=random.randint(2, 5))
    rand_pass_list = rand_letters + rand_numbers + rand_symbols
    random.shuffle(rand_pass_list)
    random.shuffle(rand_pass_list)
    rand_pass = "".join(rand_pass_list)
    pass_entry.delete(0, END)
    pass_entry.insert(0, rand_pass)
    pyperclip.copy(rand_pass)


# ---------------------------- SAVING & POP-UPS ------------------------------- #


def adding():
    web = web_entry.get().lower()
    user = user_entry.get()
    passw = pass_entry.get()
    if len(web) == 0 or len(user) == 0 or len(passw) == 0:
        messagebox.showerror(title="Error", message="Please don't leave any blank space!")
    else:
        confirm = messagebox.askokcancel(title="Data Entered", message=f"The data you entered: \nWebsite: {web}"
                                                                     f"\nEmail: {user} \nPassword: {passw} "
                                                                     f"\nIs this data correct?")
        if confirm:
            global web_list, user_list, passw_list
            web_list.append(web)
            user_list.append(user)
            passw_list.append(passw)
            new_data_dict = {
                "website": web_list,
                "user": user_list,
                "password": passw_list
            }
            new_data = pandas.DataFrame(new_data_dict)
            new_data.to_csv("data.csv")
            web_entry.delete(0, END)
            user_entry.delete(0, END)
            pass_entry.delete(0, END)


# ---------------------------- SEARCH ------------------------------- #


def searching():
    the_input = web_entry.get().lower()
    try:
        data = pandas.read_csv("data.csv")
    except FileNotFoundError:
        messagebox.showerror(title="No Data", message="Your data archive is empty.")
    else:
        password = [row.password for (index, row) in data.iterrows() if row.website == the_input]
        user = [row.user for (index, row) in data.iterrows() if row.website == the_input]
        user_entry.delete(0, END)
        pass_entry.delete(0, END)
        if len(password) == 1:
            user_entry.insert(0, user[0])
            pass_entry.insert(0, password[0])
        else:
            messagebox.showerror(title="Not Found", message="No saved data for this website")


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()

window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
the_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=the_img)
canvas.grid(column=1, row=0)

web_label = Label(text="Website:")
web_label.grid(column=0, row=1)

user_label = Label(text="Email/Username:", pady=5)
user_label.grid(column=0, row=2)

pass_label = Label(text="Password:", pady=5)
pass_label.grid(column=0, row=3)

web_entry = Entry(width=33)
web_entry.focus()
web_entry.grid(column=1, row=1)

user_entry = Entry(width=44)
user_entry.grid(column=1, row=2, columnspan=2)

pass_entry = Entry(width=33)
pass_entry.grid(column=1, row=3)

generate_button = Button(text="Generate", width=8, command=generate_pass)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=37, command=adding)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", width=8, command=searching)
search_button.grid(column=2, row=1)

window.mainloop()
