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
canvas.grid(column=2, row=0)



window.mainloop()