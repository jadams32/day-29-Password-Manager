from tkinter import *
from tkinter import messagebox
from passwordgenerator import Password


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
password = Password()


def generator():
    """Generates a random hard to guess password."""
    password_input.delete(0, END)
    new_password = password.generate()
    password_input.insert(0, f"{new_password}")


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    """Saves entries to a txt file, and confirms submission"""

    website_data = website_input.get()
    email_data = email_input.get()
    password_data = password_input.get()

    if len(website_data) == 0 or len(email_data) == 0 or len(password_data) == 0:
        messagebox.showerror(title="Password Manager", message="Fields can not be empty!")

    elif "@" not in email_data or ".com" not in email_data:
        messagebox.showerror(title="Password Manager", message="Email is invalid")

    else:
        valid = messagebox.askokcancel(title="Password Manager", message=f"Is the information correct?\n "
                                                                           f"Website: {website_data}\n "
                                                                           f"Email: {email_data}\n "
                                                                           f"Password: {password_data}")
        if valid:
            with open('data.txt', 'a') as file:
                file.write(f"{website_data} | {email_data} | {password_data}\n")
            delete_all()
            messagebox.showinfo(title="Password Manager", message='Password Saved!')


def delete_all():
    """Deletes all fields after saving to file."""
    website_input.delete(0, END)
    email_input.delete(0, END)
    password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_logo)
canvas.grid(column=1, row=0)

# Website label, & input fields
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
website_input = Entry(width=35)
website_input.focus()
website_input.grid(column=1, row=1, columnspan=2)

# Email label, & input fields
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2)

# Password label, and input fields
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
password_input = Entry(width=18)
password_input.grid(column=1, row=3)

# -------------------Buttons----------------------- #
generate_pass_button = Button(text="Generate Password", width=13, command=generator)
generate_pass_button.grid(column=2, row=3)

add_button = Button(text="Add", width=35, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
