import tkinter
import customtkinter
from tkcalendar import DateEntry

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        self.geometry("400x240")
        cc_textbox = customtkinter.CTkEntry(master=self, placeholder_text="Chief complant")
        cc_textbox.grid(row=0, column=0)

        # Use CTkButton instead of tkinter Button
        button = customtkinter.CTkButton(master=self, text="CTkButton", command=self.button_function)
        button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    def button_function():
        print("button pressed")

if __name__ == "__main__":
    app = App()
    app.mainloop()