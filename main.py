from tkinter import *
from tkinter import messagebox
from passwordgenerator import Password
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
password = Password()


def generator():
    """Generates a random hard to guess password."""
    password_input.delete(0, END)
    new_password = password.generate()
    password_input.insert(0, f"{new_password}")
    pyperclip.copy(new_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    """Saves entries to a txt file, and confirms submission"""

    website_data = website_input.get()
    email_data = email_input.get()
    password_data = password_input.get()

    new_data = {
        website_data.lower():
            {"email": email_data.lower(),
             "password": password_data}
    }

    if len(website_data) == 0 or len(email_data) == 0 or len(password_data) == 0:
        messagebox.showerror(title="Password Manager", message="Fields can not be empty!")

    elif "@" not in email_data or ".com" not in email_data:
        messagebox.showerror(title="Password Manager", message="Email is invalid")

    else:
        valid = messagebox.askokcancel(title="Password Manager", message=f"Is the information correct?\n"
                                                                           f"Website: {website_data.title()}\n"
                                                                           f"Email: {email_data}\n"
                                                                           f"Password: {password_data}")
        if valid:
            try:
                with open('data.json', 'r') as file:
                    data = json.load(file)
            except FileNotFoundError:
                with open('data.json', 'w') as file:
                    json.dump(new_data, file, indent=4)
            else:
                data.update(new_data)
                with open('data.json', 'w') as file:
                    json.dump(data, file, indent=4)

            delete_all()
            messagebox.showinfo(title="Password Manager", message='Password Saved!')


def delete_all():
    """Deletes all fields after saving to file."""
    website_input.delete(0, END)
    email_input.delete(0, END)
    password_input.delete(0, END)

# --------------------------- Search Data ----------------------------- #


def search_password():
    """Searches through the stores passwords displays them to user."""
    website_search = website_input.get()
    try:
        with open('data.json', 'r') as file:
            search_data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="Password Manager", message="No Stored Passwords.")

    if website_search.lower() in search_data:
        found_data = search_data.get(website_search.lower())
        messagebox.showerror(title="Password Manager", message=f"Website: {website_search.title()}\n"
                                                               f"Email/Username: {found_data['email']}\n"
                                                               f"Password: {found_data['password']}")
    else:
        messagebox.showerror(title="Password Manager", message="Website Not Found.")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Lock Logo Display
canvas = Canvas(width=200, height=200)
lock_logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_logo)
canvas.grid(column=1, row=0)

# Website label, & input fields
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
website_input = Entry(width=21)
website_input.focus()
website_input.grid(column=1, row=1)

# Email label, & input fields
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
email_input = Entry(width=37)
email_input.grid(column=1, row=2, columnspan=2)

# Password label, and input fields
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
password_input = Entry(width=21)
password_input.grid(column=1, row=3)

# -------------------Buttons----------------------- #
generate_pass_button = Button(text="Generate Password", width=12, command=generator)
generate_pass_button.grid(column=2, row=3)

add_button = Button(text="Add", width=35, command=save)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", width=12, command=search_password)
search_button.grid(column=2, row=1)

window.mainloop()
