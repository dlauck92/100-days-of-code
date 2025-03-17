import tkinter as tk
from tkinter import messagebox as msgbox
import random

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project

def gen_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols

    random.shuffle(password_list)

    password = "".join(password_list)
    
    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_data():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    
    if website == "" or email == "" or password == "":
        msgbox.showwarning(title="Missing Information", message="Please enter information in all fields.")
    else:
        is_ok = msgbox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}\nPassword: {password}\n Is it ok to save?")
        
        if is_ok:
            try:
                with open("data.txt", "a") as file:
                    file.write(f"{website} | {email} | {password}\n")
                    website_entry.delete(0, tk.END)
                    email_entry.delete(0, tk.END)
                    email_entry.insert(0, "example@gmail.com")
                    password_entry.delete(0, tk.END)
                    website_entry.focus()
            except Exception as e:
                print(e)
    


# ---------------------------- UI SETUP ------------------------------- #
root = tk.Tk()
root.title("Password Manager")
root.config(padx=50, pady=50)

# Canvas
canvas = tk.Canvas(width=200, height=200, highlightthickness=0)
lock_img = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0) 

# Labels
website_label = tk.Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = tk.Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = tk.Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = tk.Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = tk.Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "example@gmail.com")
password_entry = tk.Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
gen_pass_btn = tk.Button(text="Generate Password", command=gen_pass)
gen_pass_btn.grid(row=3, column=2)
add_button = tk.Button(text="Add", width=36, command=save_data)
add_button.grid(row=4, column=1, columnspan=2)


root.mainloop()