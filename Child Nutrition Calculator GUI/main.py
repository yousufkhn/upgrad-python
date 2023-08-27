from tkinter import *
import customtkinter

root = customtkinter.CTk()

root.geometry("1000x600")

root.title("Child Nutrition Calculator")

customtkinter.set_default_color_theme("green")

button = customtkinter.CTkButton(master=root, text="Button")

button.pack()

root.mainloop()
