from tkinter import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generator():
    """Generates a random hard to guess password."""
    pass


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    """Saves entries to a txt file."""

    website_data = website_input.get()
    email_data = email_input.get()
    password_data = password_input.get()

    with open('data.txt', 'a') as file:
        file.write(f"{website_data} | {email_data} | {password_data}\n")
    delete_all()


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
