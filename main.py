import tkinter as tk
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def password_maker():
    password_text_entry.delete(0, tk.END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)



    password_list1 = [random.choice(letters) for _ in range(nr_letters)]

    password_list2 = [random.choice(symbols) for _ in range(nr_symbols)]

    password_list3 = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_list1 + password_list2 + password_list3


    random.shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)
    password_text_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def password_saving():
    website = web_site_entry.get()
    email = email_text_entry.get()
    password = password_text_entry.get()
    new_data = {website: {
        'email': email,
        'password': password
    }}
    
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Bad input", message="One of the parameters is missing. Please check your input.")
    else:
        try:
            with open('data.json', 'r') as file:
                data = json.load(file)
                
                # Reading old data
        except FileNotFoundError:
            with open('data.json', 'w') as file:
                json.dump(new_data, file, indent=4)
        else:
            # Updating old data
            data.update(new_data)
            with open('data.json', 'w') as file:
                json.dump(data, file, indent=4)
        finally:
            web_site_entry.delete(0, tk.END)
            password_text_entry.delete(0, tk.END)
    

# ---------------------------- UI SETUP ------------------------------- #

def find_password():
    website = web_site_entry.get()
    try:
        with open('data.json', 'r') as file:
            new_data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found")
    else:
        if website in new_data:
            messagebox.showinfo('Your credentials', f'Website: {website} \nPassword: {new_data[website]["password"]}')
            
        else:
            messagebox.showinfo("No credentials", "You do not have account at this site.")



FONT = ("Arial", 10)


window = tk.Tk()
window.title("Password generator")
window.config(padx=50, pady=50, bg='white')

main_canv = tk.Canvas(width=200, height=200, bg='white', highlightthickness=0)
main_logo = tk.PhotoImage(file='logo.png')
main_canv.create_image(100, 100, image=main_logo)
main_canv.grid(row=0, column=0, columnspan=3)

web_text = tk.Label(text="Website:", font=FONT, bg='white')
web_text.grid(row=1, column=0)

web_site_entry = tk.Entry(width=23)
web_site_entry.focus()
web_site_entry.grid(row=1, column=1)

website_search = tk.Button(text="Search", width=14, command=find_password)
website_search.grid(row=1, column=2)

email_text = tk.Label(text="Email/Username:", font=FONT)
email_text.grid(row=2, column=0)

email_text_entry = tk.Entry(width=42)
email_text_entry.insert(0, "mimeosd@yahoo.com")
email_text_entry.grid(row=2, column=1, columnspan=2)

password_text = tk.Label(text="Password:", font=FONT)
password_text.grid(row=3, column=0)

password_text_entry = tk.Entry(width=23)
password_text_entry.grid(row=3, column=1)

generate_pass = tk.Button(text='Generate password', command=password_maker)
generate_pass.grid(row=3, column=2)

generate_pass = tk.Button(text='Add', width=35, command=password_saving)
generate_pass.grid(row=4, column=1, columnspan=2)








window.mainloop()

# 600fbf3d7b724730ebb3146aa367ce522bc41a8984f77ff3951e95e732423509
