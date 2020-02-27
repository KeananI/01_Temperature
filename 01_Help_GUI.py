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

        self.History_button = Button(self.converter_frame, text="History"
                                     ,font=("Arial", "14")
                                     ,padx=10, pady=10, command=lambda: self.History
                                     (self.all_calc_list))
        self.History_button.grid(row=1)

    def History(self, calc_History):
        History(self, calc_History)

class History:
    def __init__(self, partner, calc_history):

        background = 'white'

        partner.History_button.config(state=DISABLED)

        self.History_box = Toplevel()

        self.History_box.protocol('WM_DELETE_WINDOW', partial(self.close_History,partner))

        self.History_frame = Frame(self.History_box, width=300, bg=background)
        self.History_frame.grid()

        self.how_heading = Label(self.History_frame, text="Calculation History",
                                 font='arial 10 bold', bg=background)
        self.how_heading.grid(row=0)

        self.History_text = Label(self.History_frame,
                                  text="Here are your most recent"
                                  "calculations. Please use the"
                                  "export button to create a text"
                                  "file of all your calculations for"
                                  "this session ", wrap=250, font="arial 10 italic",
                                  justify=LEFT, bg=background, fg="maroon", padx=10,
                                  pady=10)

        self.History_text.grid(row=1)

        history_string = ""

        if len(calc_history) >=7:
            for item in range(0, 7):
                history_string += calc_history[len(calc_history)
                                                - item -1]+"\n"

        self.calc_label = Label(self.history_frame, text=history_string,
                                bg=background,front="Airal 12", justify=LEFT)
        self.calc_label.grid(row=2)

        self.export_dismiss_frame = Frame(self.History_frame)
        self.export_dismiss_frame.grid(row=3, pady=10)

        self.export_button = Button(self.export_dismiss_frame, text="Export",
                                    font="Arial 12 bold")
        self.export_button.grid(row=0, column=0)

        self.dismiss_button = Button(self.export_dismiss_frame, text="Dismiss",
                                     font="Arial 12 bold", command=partial(self.close_History()))
        self.dismiss_button.grid(row=0, column=1)


    def close_History(self, partner):

        partner.History_button.config(state=NORMAL)
        self.History_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter()
    root.mainloop()