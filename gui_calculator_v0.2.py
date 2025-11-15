import tkinter as tk

# Window
window = tk.Tk()
window.title("Calculator")
window.geometry("300x400")
window.resizable(False, False)
window.configure(bg="#1e1e1e")  # Dark mode background

# Display
display = tk.Entry(window, font=("Arial", 20), borderwidth=2, relief="solid",
                   justify="right", bg="#2d2d2d", fg="white", insertbackground="white")
display.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=10, ipady=10)


for i in range(4):
    window.grid_columnconfigure(i, weight=1)
for r in range(1, 6):
    window.grid_rowconfigure(r, weight=1)

# Functions
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

# Dark Buttons
def dark_button(parent, text, cmd, bg="#333333", fg="white"):
    return tk.Button(
        parent,
        text=text,
        font=("Arial", 18),
        bg=bg,
        fg=fg,
        activebackground="#555555",
        activeforeground="white",
        borderwidth=0,
        command=cmd
    )

# Number Buttons (1 - 9)
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
    dark_button(window, text, lambda t=text: button_click(t))\
        .grid(row=r, column=c, sticky="nsew", padx=5, pady=5)

# 0 Button
dark_button(window, "0", lambda: button_click("0"))\
    .grid(row=4, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)

# Decimal Button 
dark_button(window, ".", lambda: button_click("."))\
    .grid(row=4, column=2, sticky="nsew", padx=5, pady=5)

# Operator Buttons 
operators = [
    ("/", 1, 3),
    ("*", 2, 3),
    ("-", 3, 3),
    ("+", 4, 3),
]

for (op, r, c) in operators:
    dark_button(window, op, lambda t=op: button_click(t), bg="#444444")\
        .grid(row=r, column=c, sticky="nsew", padx=5, pady=5)

# Clear Button 
dark_button(window, "C", clear_display, bg="#d9534f")\
    .grid(row=5, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)

# Equals Button
dark_button(window, "=", calculate, bg="#4CAF50")\
    .grid(row=5, column=2, columnspan=2, sticky="nsew", padx=5, pady=5)

# App
window.mainloop()
