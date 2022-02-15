from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
lock_logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_logo)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
website_input = Entry()
website_input.grid(column=1, row=1, columnspan=2)

email_label = Label(text="Email / Username:")
email_label.grid(column=0, row=2)
email_input = Entry()
email_input.grid(column=1, row=2, columnspan=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
password_input = Entry()
password_input.grid(column=1, row=3)

generate_pass_button = Button(text="Generate Password")
generate_pass_button.grid(column=2, row=3)

add_button = Button(text="Add")
add_button.grid(column=1, row=4, columnspan=2)




window.mainloop()