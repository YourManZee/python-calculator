import tkinter as tk

window = tk.Tk()
window.title("Calculator")
window.geometry("300x400")
window.resizable(False, False)

# Display using grid
display = tk.Entry(window, font=("Arial", 20), borderwidth=2, relief="solid", justify="right")
display.grid(row=0, column=0, columnspan=3, sticky="nsew", padx=10, pady=10, ipady=10)

# Make rows and columns resize evenly
for i in range(3):
    window.grid_columnconfigure(i, weight=1)
for r in range(1, 5):
    window.grid_rowconfigure(r, weight=1)

def button_click(value):
    display.insert(tk.END, value)

# Buttons 1–9
numbers = [
    ("1", 1, 0),
    ("2", 1, 1),
    ("3", 1, 2),
    ("4", 2, 0),
    ("5", 2, 1),
    ("6", 2, 2),
    ("7", 3, 0),
    ("8", 3, 1),
    ("9", 3, 2),
]

for (text, r, c) in numbers:
    tk.Button(window, text=text, font=("Arial", 18), command=lambda t=text: button_click(t))\
        .grid(row=r, column=c, sticky="nsew", padx=5, pady=5)

# Button 0 spans 2 columns
tk.Button(window, text="0", font=("Arial", 18),
          command=lambda: button_click("0"))\
    .grid(row=4, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)

# Decimal button
tk.Button(window, text=".", font=("Arial", 18),
          command=lambda: button_click("."))\
    .grid(row=4, column=2, sticky="nsew", padx=5, pady=5)

operators = [
    ("/", 1, 3),
    ("*", 2, 3),
    ("-", 3, 3),
    ("+", 4, 3),
]

for (op, r, c) in operators:
    tk.Button(window, text=op, font=("Arial", 18),
              command=lambda t=op: button_click(t))\
              .grid(row=r, column=c, sticky="nsew", padx=5, pady=5) 

tk.Button(window, text="C", font=("Arial", 18), bg="#ff6666",
              command=lambda: display.delete(0, tk.END))\
              .grid(row=5, column=0, columnspan=2, sticky="nsew", padx=5, pady=5) 

def calculate():
    try:
        expression = display.get()
        result = eval(expression)
        display.delete(0, tk.END)
        display.insert(0, result)
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")

tk.Button(window, text="=", font=("Arial", 18), bg="#66cc66",
          command=calculate)\
    .grid(row=5, column=2, columnspan=2, sticky="nsew", padx=5, pady=5)

    

window.mainloop()
