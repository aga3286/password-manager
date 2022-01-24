from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project

def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    letters = [random.choice(letters) for _ in range(nr_letters)]
    symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list.extend(letters)
    password_list.extend(symbols)
    password_list.extend(numbers)

    random.shuffle(password_list)

    password = ''.join(password_list)
    password_input.delete(0, END)
    password_input.insert(0, password)

    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email = email_user_name_input.get()
    password = password_input.get()
    new_data = {website: {
        'email': email,
        'password': password
    }}

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title='Oops', message="Please don't leave any fields empty!")
    else:
        try:
            with open('data.json', 'r') as f:
                data = json.load(f)

        except FileNotFoundError:
            with open('data.json', 'w') as f:
                json.dump(new_data, f, indent=4)
        else:
            data.update(new_data)
            with open('data.json', 'w') as f:
                json.dump(data, f, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)

def find_password():
    website = website_input.get()
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        messagebox.showinfo(title='Error', message='No Data File Found')
    else:
        try:
            target_password = data[website]['password']
        except KeyError:
            messagebox.showinfo(title='Error', message='No details for the website exists')
        else:
            messagebox.showinfo(title=website, message=f"website: {website}\npassword: {target_password}")



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

img_file = PhotoImage(file='logo.png')
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=img_file)
canvas.grid(column=1, row=0)

website_label = Label(text='Website:')
website_label.grid(column=0, row=1)
website_input = Entry(width=21)
website_input.grid(column=1, row=1)
website_input.focus()
search_button = Button(text='Search', width=14, command=find_password)
search_button.grid(column=2, row=1)

email_user_name_label = Label(text='Email/Username:')
email_user_name_label.grid(column=0, row=2)
email_user_name_input = Entry(width=35)
email_user_name_input.grid(column=1, row=2, columnspan=2)
email_user_name_input.insert(0, 'mickey@gmail.com')

password_label = Label(text='Password:')
password_label.grid(column=0, row=3)
password_input = Entry(width=21)
password_input.grid(column=1, row=3)
generate_button = Button(text='Generate Password', command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
