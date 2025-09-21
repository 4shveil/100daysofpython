from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# ---------------------------- SEARCH FUNCTION ------------------------------- #
def search():
    website = website_entry.get()
    print(website)
    try:
        with open("data.json", "r") as f:  # open file in read mode
            # reading old data
            data = json.load(f)
            if data[website]:
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(title=f"{website} data", message=f"Email: {email}\nPassword: {password}")
            else:
                raise KeyError
    except FileNotFoundError:
        messagebox.showerror(title="Not found", message=f"No Data File Found.")
    except KeyError:
        messagebox.showerror(title="Not found", message=f"No details for {website} website exists")



# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    if password_entry != '':
        password_entry.delete(0, END)

    password_list_char = [choice(letters) for _ in range(randint(8, 10))]
    password_list_sym = [choice(symbols) for _ in range(randint(2, 4))]
    password_list_num = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_list_num + password_list_sym + password_list_char

    shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(END, password)
    pyperclip.copy(password)
    messagebox.showinfo(title="Notification", message="Your password has been copied")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password_s = password_entry.get()
    new_data = {website: {
        "email": email,
        "password": password_s,
        }
    }

    if website.strip() == "" or email.strip() == "" or password_s.strip() == "":
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details "
                                                              f"entered:"
                                                      f"\nEmail: {email}\n"
                                                      f"Password: {password_s}\n"
                                                      f"Is it ok to save?")
        if is_ok:
            try:
                with open("data.json", "r") as f: # open file in read mode
                    # reading old data
                    data = json.load(f)
            except FileNotFoundError:
                with open("data.json", "w") as f:
                    json.dump(new_data, f, indent=4)
            else:
                # updating old data with new data
                data.update(new_data)

                with open("data.json", "w") as f:
                    # saving updated data
                    json.dump(data, f, indent=4)
            finally:
                    website_entry.delete(0, END)
                    password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 102, image=logo)
canvas.grid(row=0, column=1)

label_1 = Label(text="Website:")
label_1.grid(row=1, column=0)

label_2 = Label(text="Email/Username:")
label_2.grid(row=2, column=0)

label_3 = Label(text="Password:")
label_3.grid(row=3, column=0)

website_entry = Entry(width=20)
website_entry.grid(row=1, column=1)
website_entry.focus()

email_entry = Entry(width=39)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(END, "manticgamer@gmail.com")

password_entry = Entry(width=20)
password_entry.grid(row=3, column=1)

gen_pass_butt = Button(text="Generate Password", command=generate_pass, width=15)
gen_pass_butt.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text="Search", command=search, width=15)
search_button.grid(row=1, column=2)

window.mainloop()
