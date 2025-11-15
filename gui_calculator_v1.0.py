import tkinter as tk
from tkinter import messagebox

#   THEMES (Light & Dark)
light_theme = {
    "window_bg": "#ffffff",
    "display_bg": "#ffffff",
    "display_fg": "#000000",
    "button_bg": "#e6e6e6",
    "button_fg": "#000000",
    "operator_bg": "#d9d9d9",
    "special_bg": "#ff6666",
    "equal_bg": "#4CAF50"
}

dark_theme = {
    "window_bg": "#1e1e1e",
    "display_bg": "#2d2d2d",
    "display_fg": "#ffffff",
    "button_bg": "#333333",
    "button_fg": "#ffffff",
    "operator_bg": "#444444",
    "special_bg": "#d9534f",
    "equal_bg": "#4CAF50"
}

current_theme = dark_theme  # Default theme


#   TKINTER WINDOW
window = tk.Tk()
window.title("Calculator")
window.geometry("320x450")
window.resizable(False, False)


#   DISPLAY / SCREEN
display = tk.Entry(window, font=("Arial", 22), borderwidth=2, relief="solid",
                   justify="right")
display.grid(row=0, column=0, columnspan=4, sticky="nsew",
             padx=10, pady=10, ipady=10)


# Configure grid to expand properly
for i in range(4):
    window.grid_columnconfigure(i, weight=1)
for r in range(1, 6):
    window.grid_rowconfigure(r, weight=1)


#   FUNCTIONS
def button_click(value):
    display.insert(tk.END, value)


def clear_display():
    display.delete(0, tk.END)


def calculate():
    try:
        expression = display.get()
        result = eval(expression)
        display.delete(0, tk.END)
        display.insert(0, result)
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")


#   THEME APPLY FUNCTION
def apply_theme(theme):
    global current_theme
    current_theme = theme

    # Window color
    window.config(bg=theme["window_bg"])

    # Display theme
    display.config(bg=theme["display_bg"],
                   fg=theme["display_fg"],
                   insertbackground=theme["display_fg"])

    # Number buttons
    for btn in number_buttons:
        btn.config(bg=theme["button_bg"], fg=theme["button_fg"],
                   activebackground="#555555")

    # Operator buttons
    for btn in operator_buttons:
        btn.config(bg=theme["operator_bg"], fg="white",
                   activebackground="#666666")

    # Clear button
    clear_button.config(bg=theme["special_bg"], fg="white")

    # Equals button
    equals_button.config(bg=theme["equal_bg"], fg="white")


#   HELP MENU FUNCTIONS
def show_about():
    messagebox.showinfo(
        "About",
        "Calculator App\n"
        "Made by YourManZee\n"
        "Built as my first Python GUI project :)"
    )


def show_shortcuts():
    messagebox.showinfo(
        "Keyboard Shortcuts",
        "Future update:\n"
        "You will be able to type numbers and operators\n"
        "directly using your keyboard!"
    )


#   MENU BAR
menu_bar = tk.Menu(window)
window.config(menu=menu_bar)

# File Menu (empty for now)
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)

# View Menu
view_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="View", menu=view_menu)

# Theme Submenu
theme_menu = tk.Menu(view_menu, tearoff=0)
view_menu.add_cascade(label="Theme", menu=theme_menu)
theme_menu.add_command(label="Light Mode", command=lambda: apply_theme(light_theme))
theme_menu.add_command(label="Dark Mode", command=lambda: apply_theme(dark_theme))

# Help Menu
help_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=show_about)
help_menu.add_command(label="Keyboard Shortcuts", command=show_shortcuts)


#   BUTTON FACTORY
def create_button(text, row, col, colspan=1, bg=None, cmd=None):
    btn = tk.Button(
        window,
        text=text,
        font=("Arial", 18),
        bg=bg if bg else current_theme["button_bg"],
        fg=current_theme["button_fg"],
        activebackground="#555555",
        activeforeground="white",
        borderwidth=0,
        command=cmd
    )
    btn.grid(row=row, column=col, columnspan=colspan,
             sticky="nsew", padx=5, pady=5)
    return btn


#   CREATE BUTTONS
number_buttons = []
operator_buttons = []

# Number buttons 1–9
numbers = [
    ("1", 3, 0),
    ("2", 3, 1),
    ("3", 3, 2),
    ("4", 2, 0),
    ("5", 2, 1),
    ("6", 2, 2),
    ("7", 1, 0),
    ("8", 1, 1),
    ("9", 1, 2),
]

for (text, r, c) in numbers:
    number_buttons.append(
        create_button(text, r, c, cmd=lambda t=text: button_click(t))
    )

# Button 0
number_buttons.append(
    create_button("0", 4, 0, colspan=2, cmd=lambda: button_click("0"))
)

# Decimal button
number_buttons.append(
    create_button(".", 4, 2, cmd=lambda: button_click("."))
)

# Operators: / * - +
ops = [
    ("/", 1, 3),
    ("*", 2, 3),
    ("-", 3, 3),
    ("+", 4, 3),
]

for (op, r, c) in ops:
    operator_buttons.append(
        create_button(op, r, c, bg=current_theme["operator_bg"],
                      cmd=lambda t=op: button_click(t))
    )

# Clear button
clear_button = create_button("C", 5, 0, colspan=2,
                             bg=current_theme["special_bg"],
                             cmd=clear_display)

# Equals button
equals_button = create_button("=", 5, 2, colspan=2,
                              bg=current_theme["equal_bg"],
                              cmd=calculate)


#   APPLY DEFAULT DARK THEME
apply_theme(dark_theme)

#   RUN APP
window.mainloop()
