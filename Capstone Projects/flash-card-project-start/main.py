from tkinter import *

import pandas
import pandas as pd
from random import choice

from pandas.core.interchange.dataframe_protocol import DataFrame

LANGUAGE_FONT = ("Arial", 40, "italic")
WORD_FONT = ("Arial", 60, "bold")
BACKGROUND_COLOR = "#B1DDC6"
WHITE_CLR = "#FFFFFF"
BLACK_CLR = "#000000"
card = None
timer = None

# Reading csv
try:
    df = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    df = pd.read_csv("data/french_words.csv")
finally:
    to_learn = df.to_dict(orient="records")


def next_card():
    global timer, card
    card = choice(to_learn)
    canvas.itemconfig(card_img, image=front_card)
    canvas.itemconfig(language_title, text="French", fill=BLACK_CLR)
    canvas.itemconfig(language_word, text=card["French"], fill=BLACK_CLR)
    timer = window.after(3000, flip_card, card) # global timer var from line 8


def flip_card(curr_card):
    global timer
    canvas.itemconfig(card_img, image=back_card)
    canvas.itemconfig(language_title, text="English", fill=WHITE_CLR)
    canvas.itemconfig(language_word, text=curr_card["English"], fill=WHITE_CLR)
    window.after_cancel(timer) # global timer changed in line 19 to after declared in line 8 as None


def known_word():
    global card
    to_learn.remove(card)
    new_df = pd.DataFrame(to_learn)
    pd.DataFrame.to_csv(new_df, path_or_buf="data/words_to_learn.csv", mode='w', index=False)
    next_card()

window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Canvas and card image
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
front_card = PhotoImage(file="images/card_front.png")
back_card = PhotoImage(file="images/card_back.png")
card_img = canvas.create_image(400, 263, image=front_card)
language_title = canvas.create_text(400, 150, text="", font=LANGUAGE_FONT)
language_word = canvas.create_text(400, 263, text="", font=WORD_FONT)
canvas.grid(row=0, column=0, columnspan=2)

# Buttons PhotoImages
checkmark_img = PhotoImage(file="images/right.png")
x_img = PhotoImage(file="images/wrong.png")

# Buttons
correct_button = Button(image=checkmark_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=known_word)
correct_button.grid(row=1, column=1)
wrong_button = Button(image=x_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_card)
wrong_button.grid(row=1, column=0)

next_card()

window.mainloop()
