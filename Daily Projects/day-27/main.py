from tkinter import *

window = Tk()
window.title("Mile to Km Converter or Vice versa")
window.minsize(width=200, height=100)

entry = Entry(width=10)
entry.insert(END, string="0")
entry.grid(row=0, column=2)

label1 = Label(text="To choose")
label1.grid(row=0, column=3)

equalTo_label = Label(text="is equal to")
equalTo_label.grid(row=1, column=0)

result_label = Label(text='0')
result_label.grid(row=1, column=2)

label2 = Label(text="To choose")
label2.grid(row=1, column=3)

def calculate():
    choice = radio_state.get()
    entry_value = float(entry.get())
    if choice == 1:
        result = entry_value * 1.609
        result_label.config(text=result)
    elif choice == 2:
        result = entry_value / 1.609
        result_label.config(text=result)


def radio_used():
    choice = radio_state.get()
    if choice == 1:
        label1.config(text="Miles")
        label2.config(text="Km")
    elif choice == 2:
        label1.config(text="Km")
        label2.config(text="Miles")


radio_state = IntVar()
radiobutton1 = Radiobutton(text="Miles to KM", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="KM to Miles", value=2, variable=radio_state, command=radio_used)
radiobutton1.grid(row=2, column=0)
radiobutton2.grid(row=3, column=0)

calculate_button = Button(text="Calculate", command=calculate)
calculate_button.grid(row=2, column=2)


window.mainloop()