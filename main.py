#Author: Apostolos Halis 2023
#This is a small unit converter written in python
import tkinter
from tkinter import *

# fucntions that do the conversions
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def celsius_to_kelvin(celsius):
    kelvin = celsius + 273.15
    return kelvin

def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius

def kelvin_to_fahrenheit(kelvin):
    fahrenheit = (kelvin - 273.15) * 9/5 + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def fahrenheit_to_kelvin(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    kelvin = celsius_to_kelvin(celsius)
    return kelvin

def click():
    print("Processing...")
    contents = toBeConverted.get()
    intContents = int(contents)
    selectionMade = selected.get()
    if contents.isdigit() != True:
        return
    if selectionMade == "":
        return

    # checks about the type of conversion
    if selectionMade == "ctf":
        x = celsius_to_fahrenheit(intContents)
        displayField.delete(0.0,END)
        displayField.insert(END, x)
    elif selectionMade == "ctk":
        x = celsius_to_kelvin(intContents)
        displayField.delete(0.0, END)
        displayField.insert(END, x)
    elif selectionMade == "ftc":
        x = fahrenheit_to_celsius(intContents)
        displayField.delete(0.0, END)
        displayField.insert(END, x)
    elif selectionMade == "ftk":
        x = fahrenheit_to_kelvin(intContents)
        displayField.delete(0.0, END)
        displayField.insert(END, x)
    elif selectionMade == "ktc":
        x = kelvin_to_celsius(intContents)
        displayField.delete(0.0, END)
        displayField.insert(END, x)
    elif selectionMade == "ktf":
        x = kelvin_to_fahrenheit(intContents)
        displayField.delete(0.0, END)
        displayField.insert(END, x)

window = Tk()
selected = tkinter.StringVar()
window.title("Unit conversions")
window.geometry("550x400")
window.configure(background="grey")
window.resizable(height=False, width=True)

#window components
titleLabel = Label(window,text="Unit Conversions", foreground="black", background="grey",font=16)
toBeConverted = Entry(window, fg="black", bg="white", width=25)
# celsius options
cTFOption = Radiobutton(window, text="Celsius to Fahrenheit", variable=selected, bg="grey", value="ctf")
cTKOption = Radiobutton(window, text="Celsius to Kelvin", variable=selected,  bg="grey", value="ctk")
# fahrenheit options
fTCOption = Radiobutton(window, text="Fahrenheit to Celsius", variable=selected,  bg="grey", value="ftc")
fTKOption = Radiobutton(window, text="Fahrenheit to Kelvin", variable=selected,  bg="grey", value="ftk")
# Kelvin options
kTCOption = Radiobutton(window, text="Kelvin to Celsius", variable=selected,  bg="grey", value="ktc")
kTFOption = Radiobutton(window, text="Kelvin to Fahrenheit", variable=selected,  bg="grey", value="ktf")
convertButtton = Button(window, text="Convert", command=click)
displayField = Text(window, bg="grey", width=25, height=5)

# implementing the grid layout in tkinter
titleLabel.grid(row=0, column=2, sticky="nsew")
toBeConverted.grid(row=1, column=2, sticky="n")
cTKOption.grid(row=2, column=2)
cTFOption.grid(row=3, column=2)
fTKOption.grid(row=4, column=2)
fTCOption.grid(row=5, column=2)
kTCOption.grid(row=6, column=2)
kTFOption.grid(row=7, column=2)
convertButtton.grid(row=8, column=2, sticky="n")
displayField.grid(row=9, column=2, sticky="n")

#default things for making tkinter work
window.columnconfigure(2, weight=1)
window.mainloop()