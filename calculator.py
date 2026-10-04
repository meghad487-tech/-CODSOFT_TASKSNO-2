import tkinter as tk


# Function to add numbers and operators to the display
def click_button(value):
    current = display_var.get()
    display_var.set(current + str(value))


# Function to calculate the result
def calculate():
    try:
        result = eval(display_var.get())
        display_var.set(result)

    except Exception:
        display_var.set("Error")


# Function to clear the display
def clear_display():
    display_var.set("")


# Function to delete the last character
def backspace():
    current = display_var.get()
    display_var.set(current[:-1])


# Create the main window
root = tk.Tk()

root.title("Simple Calculator")
root.geometry("400x550")
root.configure(bg="#24243E")
root.resizable(False, False)


# Variable for the calculator display
display_var = tk.StringVar()


# Title
title = tk.Label(
    root,
    text="CALCULATOR",
    font=("Arial", 22, "bold"),
    bg="#24243E",
    fg="white"
)

title.pack(pady=20)


# Display box
display = tk.Entry(
    root,
    textvariable=display_var,
    font=("Arial", 25, "bold"),
    justify="right",
    bd=0,
    bg="white",
    fg="#24243E"
)

display.pack(
    fill="x",
    padx=25,
    ipady=20
)


# Button frame
button_frame = tk.Frame(
    root,
    bg="#24243E"
)

button_frame.pack(
    pady=25
)


# Function to create calculator buttons
def create_button(text, row, column, color, command=None):

    button = tk.Button(
        button_frame,
        text=text,
        font=("Arial", 16, "bold"),
        width=5,
        height=2,
        bg=color,
        fg="white",
        activebackground="#6C63FF",
        activeforeground="white",
        bd=0,
        cursor="hand2",
        command=command
    )

    button.grid(
        row=row,
        column=column,
        padx=5,
        pady=5
    )


# Row 1
create_button(
    "C",
    0,
    0,
    "#FF6584",
    clear_display
)

create_button(
    "DEL",
    0,
    1,
    "#FF6584",
    backspace
)

create_button(
    "/",
    0,
    2,
    "#6C63FF",
    lambda: click_button("/")
)

create_button(
    "*",
    0,
    3,
    "#6C63FF",
    lambda: click_button("*")
)


# Row 2
create_button(
    "7",
    1,
    0,
    "#353550",
    lambda: click_button("7")
)

create_button(
    "8",
    1,
    1,
    "#353550",
    lambda: click_button("8")
)

create_button(
    "9",
    1,
    2,
    "#353550",
    lambda: click_button("9")
)

create_button(
    "-",
    1,
    3,
    "#6C63FF",
    lambda: click_button("-")
)


# Row 3
create_button(
    "4",
    2,
    0,
    "#353550",
    lambda: click_button("4")
)

create_button(
    "5",
    2,
    1,
    "#353550",
    lambda: click_button("5")
)

create_button(
    "6",
    2,
    2,
    "#353550",
    lambda: click_button("6")
)

create_button(
    "+",
    2,
    3,
    "#6C63FF",
    lambda: click_button("+")
)


# Row 4
create_button(
    "1",
    3,
    0,
    "#353550",
    lambda: click_button("1")
)

create_button(
    "2",
    3,
    1,
    "#353550",
    lambda: click_button("2")
)

create_button(
    "3",
    3,
    2,
    "#353550",
    lambda: click_button("3")
)

create_button(
    "=",
    3,
    3,
    "#32C48D",
    calculate
)


# Row 5
create_button(
    "0",
    4,
    0,
    "#353550",
    lambda: click_button("0")
)

create_button(
    ".",
    4,
    1,
    "#353550",
    lambda: click_button(".")
)


# Empty buttons for design
create_button(
    "(",
    4,
    2,
    "#6C63FF",
    lambda: click_button("(")
)

create_button(
    ")",
    4,
    3,
    "#6C63FF",
    lambda: click_button(")")
)


# Start the application
root.mainloop()
