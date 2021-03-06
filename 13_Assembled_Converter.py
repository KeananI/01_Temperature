from tkinter import *
from functools import partial  # To prevent unwanted windows

import random


class Converter:
    def __init__(self):

        background_color = 'Light blue'

        self.all_calc_list = []

        self.converter_frame = Frame(bg=background_color,
                                     pady=10)
        self.converter_frame.grid()

        self.temp_heading_label = Label(self.converter_frame,
                                        text="Temperature Converter",
                                        font="Arial 19 bold", bg=background_color,
                                        padx=10, pady=10)
        self.temp_heading_label.grid(row=0)

        self.temp_instructions_label = Label(self.converter_frame,
                                             text="Type in the amount to be"
                                                  "converted and then push"
                                                  "one of the buttons below...",
                                             font="Arial 10 italic", wrap=250,
                                             justify=LEFT, bg=background_color,
                                             padx=10, pady=10)
        self.temp_instructions_label.grid(row=1)

        self.to_convert_entry = Entry(self.converter_frame, width=20,
                                      font="Arial 14 bold")
        self.to_convert_entry.grid(row=2)

        self.conversion_buttons_frame = Frame(self.converter_frame)
        self.conversion_buttons_frame.grid(row=3, pady=10)

        self.to_c_button = Button(self.conversion_buttons_frame,
                                  text="To Centigrade", font="Arial 10 bold",
                                  bg="Khaki1", padx=10, pady=10,
                                  command=lambda: self.temp_convert(-459))
        self.to_c_button.grid(row=0, column=0)

        self.to_f_button = Button(self.conversion_buttons_frame,
                                  text="To Fahrenheit", font="Arial 10 bold",
                                  bg="Orchid1", padx=10, pady=10,
                                  command=lambda: self.temp_convert(-273))
        self.to_f_button.grid(row=0, column=1)

        self.converted_label = Label(self.converter_frame, font="Arial 14 bold",
                                     fg="purple", bg=background_color,
                                     pady=10, text="Conversion goes here")
        self.converted_label.grid(row=4)

        self.hist_help_frame = Frame(self.converter_frame)
        self.hist_help_frame.grid(row=5, pady=10)

        self.history_button = Button(self.hist_help_frame, font="Arial 12 bold",
                                     text="Calculation history", width=15,
                                     command=lambda: self.history(self.all_calc_list))
        self.history_button.grid(row=0, column=0)

        if len(self.all_calc_list) == 0:
            self.history_button.config(state=DISABLED)

        self.help_button = Button(self.hist_help_frame, font="Arial 12 bold",
                                  text="Help", width=5)
        self.help_button.grid(row=0, column=1)

    def temp_convert(self, low):
        print(low)

        error = "#ffafaf"
        answer = "answer"

        to_convert = self.to_convert_entry.get()

        try:
            to_convert = float(to_convert)
            has_errors = "no"

            if low == -273 and to_convert >= low:
                fahrenheit = (to_convert * 9 / 5) + 32
                to_convert = self.round_it(to_convert)
                fahrenheit = self.round_it(fahrenheit)
                answer = "{} degress C is {} degress F".format(to_convert, fahrenheit)

            elif low == -459 and to_convert >= low:
                celsius = (to_convert - 32) * 5 / 9
                to_convert = self.round_it(to_convert)
                celsius = self.round_it(celsius)
                answer = "{} degress F is {} degrees C".format(to_convert, celsius)

            else:
                answer = "Too Cold"
                has_errors = "yes"

            if has_errors == "no":
                self.converted_label.configure(text=answer, fg="blue")
                self.to_convert_entry.configure(bg="white")
            else:
                self.converted_label.configure(text=answer, fg="red")
                self.to_convert_entry.configure(bg=error)

            if has_errors != "yes":
                self.all_calc_list.append(answer)
                self.history_button.config(state=NORMAL)

        except ValueError:
            self.converted_label.configure(text="Enter a number!!", fg="red")
            self.to_convert_entry.configure(bg=error)

    def round_it(self, to_round):
        if to_round % 1 == 0:
            rounded = int(to_round)
        else:
            rounded = round(to_round, 1)

        return rounded

    def history(self, calc_history):
        History(self, calc_history)


class History:
    def __init__(self, partner, calc_history):

        background = 'white'

        partner.history_button.config(state=DISABLED)

        self.history_box = Toplevel()

        self.history_box.protocol('WM_DELETE_WINDOW', partial(self.close_history,partner))

        self.History_frame = Frame(self.history_box, width=300, bg=background)
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

        self.calc_label = Label(self.History_frame, text=history_string,
                                bg=background, font="Arial 12", justify=LEFT)
        self.calc_label.grid(row=2)

        self.export_dismiss_frame = Frame(self.History_frame)
        self.export_dismiss_frame.grid(row=3, pady=10)

        self.export_button = Button(self.export_dismiss_frame, text="Export",
                                    font="Arial 12 bold")
        self.export_button.grid(row=0, column=0)

        self.dismiss_button = Button(self.export_dismiss_frame, text="Dismiss",
                                     font="Arial 12 bold",
                                     command=partial(self.close_history, partner))
        self.dismiss_button.grid(row=0, column=1)

    def close_history(self, partner):

        partner.history_button.config(state=NORMAL)
        self.history_box.destroy()

    def export(self, partner, calc_export):
        Export(self, partner, calc_export)

class Export:
    def __init__(self, partner, calc_export):

        background = 'white'
        print(calc_export)

        partner.export_button.config(state=DISABLED)

        self.export_box = Toplevel()

        self.export_box.protocol('WM_DELETE_WINDOW', partial(self.close_export,partner))

        self.export_frame = Frame(self.export_box, width=300, bg=background)
        self.export_frame.grid()

        self.how_heading = Label(self.export_frame, text="Calculation export",
                                 font='arial 10 bold', bg=background)
        self.how_heading.grid(row=0)

        self.export_text = Label(self.export_frame,
                                  text="Enter a filename in the"
                                       "box below and press the"
                                       "save button to save your"
                                       "calculation history to a"
                                       "text file"
                                 , justify=LEFT, width=40,
                                    bg=background, wrap=250)
        self.export_text.grid(row=1)

        # Entry Box for file name goes here...
        self.filename_entry = Entry(self.export_frame,
                                width=20, font="Arial 14 bold", justify=CENTER)
        self.filename_entry.grid(row=3, pady=10)

        self.export_dismiss_frame = Frame(self.export_frame)
        self.export_dismiss_frame.grid(row=4, pady=10)

        self.save_button = Button(self.export_dismiss_frame, text="Save",
                                    font="Arial 12 bold")
        self.save_button.grid(row=0, column=0)

        self.dismiss_button = Button(self.export_dismiss_frame, text="Dismiss",
                                     font="Arial 12 bold",
                                     command=partial(self.close_export, partner))
        self.dismiss_button.grid(row=0, column=1)

    # closes export dialogue
    def close_export(self, partner):

        partner.export_button.config(state=NORMAL)
        self.export_box.destroy()



# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter()
    root.mainloop()