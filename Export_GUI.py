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

        # self.all_calc_list = []


        # Converter Main Screen GUI...
        self.converter_frame = Frame(width=600, heigh=600, bg=background_color, pady=10)
        self.converter_frame.grid()

        self.temp_converter_label = Label(self.converter_frame, text="Temperature Converter",
                                          font=("Arial", "16", "bold"),
                                          bg=background_color,
                                          padx=10, pady=10)
        self.temp_converter_label.grid(row=0)

        self.export_button = Button(self.converter_frame, text="export"
                                        , font=("Arial", "14"),
                                        padx=10, pady=10, command=lambda: self.export
                                        (self.all_calc_list))
        self.export_button.grid(row=1)

        if len(self.all_calc_list) == 0:
            self.export_button.config(state=DISABLED)

    def export(self, calc_export):
        Export(self, calc_export)


class Export:
    def __init__(self, partner, calc_export):

        background = 'white'

        partner.export_button.config(state=DISABLED)

        self.export_box = Toplevel()

        self.export_box.protocol('WM_DELETE_WINDOW', partial(self.close_export,partner))

        self.export_frame = Frame(self.export_box, width=300, bg=background)
        self.export_frame.grid()

        self.how_heading = Label(self.export_frame, text="Calculation export",
                                 font='arial 10 bold', bg=background)
        self.how_heading.grid(row=0)

        self.export_text = Label(self.export_frame,
                                  text="Here are your most recent"
                                  "calculations. Please use the"
                                  "export button to create a text"
                                  "file of all your calculations for"
                                  "this session ", wrap=250, font="arial 10 italic",
                                  justify=LEFT, bg=background, fg="maroon", padx=10,
                                  pady=10)

        self.export_text.grid(row=1)

        export_string = ""

        if len(calc_export) >=7:
            for item in range(0, 7):
                export_string += calc_export[len(calc_export)
                                                - item -1]+"\n"

        self.calc_label = Label(self.export_frame, text=export_string,
                                bg=background, font="Arial 12", justify=LEFT)
        self.calc_label.grid(row=2)

        self.export_dismiss_frame = Frame(self.export_frame)
        self.export_dismiss_frame.grid(row=3, pady=10)

        self.save_button = Button(self.export_dismiss_frame, text="Save",
                                    font="Arial 12 bold")
        self.save_button.grid(row=0, column=0)

        self.dismiss_button = Button(self.export_dismiss_frame, text="Dismiss",
                                     font="Arial 12 bold",
                                     command=lambda: self.close_export
                                     (partial))
        self.dismiss_button.grid(row=0, column=1)

    def close_export(self, partner):

        partner.export_button.config(state=NORMAL)
        self.export_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter()
    root.mainloop()