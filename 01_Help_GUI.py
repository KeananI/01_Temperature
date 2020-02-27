from tkinter import *
from functools import partial  # To prevent unwanted windows

import random


class Converter:
    def __init__(self):

        # Formatting Variables...
        background_color = "light blue"

        self.all_calc_list = ['123 degress F is 50.6 degrees C',
                              '123 degress C is 253.4 degress F',
                              '123 degress F is 50.6 degrees C',
                              '123 degress C is 253.4 degress F',
                              '123 degress F is 50.6 degrees C',
                              '123 degress C is 253.4 degress F',
                              '123 degress F is 50.6 degrees C']

        # Converter Main Screen GUI...
        self.converter_frame = Frame(width=600, heigh=600, bg=background_color, pady=10)
        self.converter_frame.grid()

        self.temp_converter_label = Label(self.converter_frame, text="Temperature Converter",
                                          font=("Arial", "16", "bold"),
                                          bg=background_color,
                                          padx=10, pady=10)
        self.temp_converter_label.grid(row=0)

        self.history_button = Button(self.converter_frame, text="history",font=("Arial", "14")
                                  , padx=10, pady=10, command=self.history)
        self.history_button.grid(row=1)

    def history(self):
        print("You asked for history")
        get_history = history(self)
        get_history.history_text.configure(text="history text goes here")

class history:
    def __init__(self, partner):

        background = 'orange'

        partner.history_button.config(state=DISABLED)

        self.history_box = Toplevel()

        self.history_box.protocol('WM_DELETE_WINDOW', partial(self.close_history,partner))

        self.history_frame = Frame(self.history_box, width=300, bg=background)
        self.history_frame.grid()

        self.how_heading = Label(self.history_frame, text="history / Instructions",
                                 font='arial 10 bold', bg=background)
        self.how_heading.grid(row=0)

        self.history_text = Label(self.history_frame,
                                  text="Here are your most recent"
                                  "calculations. Please use the"
                                  "export button to create a text"
                                  "file of all your calculations for"
                                  "this session ",justify=LEFT, width=40, bg=background, wrap=250)
        self.history_text.grid(column=0, row=1)

        self.dismiss_btn = Button(self.history_frame, text="Dismiss", width=10, bg="orange",
                                  command=partial(self.close_history,partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_history(self, partner):

        partner.history_button.config(state=NORMAL)
        self.history_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter()
    root.mainloop()