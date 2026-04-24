import customtkinter as ctk

ctk.set_appearance_mode("dark")

app = ctk.CTk()
app.geometry("320x480")
app.title("Calculator")
app.configure(fg_color="#0b0b0b")  # deep black

expression = ""

# Expression (upar)
exp_label = ctk.CTkLabel(
    app,
    text="",
    anchor="e",
    font=("Arial", 18),
    text_color="#888888"
)
exp_label.pack(fill="x", padx=15)

# Result (neeche)
result_label = ctk.CTkLabel(
    app,
    text="",
    anchor="e",
    font=("Arial", 32, "bold"),
    text_color="#00d1c1"
)
result_label.pack(fill="x", padx=15, pady=(0,10))

# Functions
def press(val):
    global expression
    expression += str(val)
    exp_label.configure(text=expression)

def clear():
    global expression
    expression = ""
    exp_label.configure(text="")
    result_label.configure(text="")

def equal():
    global expression
    try:
        result = str(eval(expression))
        exp_label.configure(text=expression)
        result_label.configure(text="= " + result)
        expression = result
    except:
        result_label.configure(text="Error")
        expression = ""

def percent():
    global expression
    try:
        result = str(eval(expression) / 100)
        expression.delete(0, "end")
        expression.insert("end", result)
        expression = result
    except:
        expression.insert("end", "Error")

# Frame
frame = ctk.CTkFrame(app, fg_color="#0b0b0b")
frame.pack(expand=True, fill="both", padx=10, pady=10)

for i in range(6):
    frame.rowconfigure(i, weight=1)
for j in range(4):
    frame.columnconfigure(j, weight=1)

# Colors
num_color = "#1a1a1a"      # dark buttons
op_color = "#00bfa5"       # teal buttons

# Button function
def btn(text, row, col, cmd, color, colspan=1):
    ctk.CTkButton(
        frame,
        text=text,
        command=cmd,
        corner_radius=8,         # 👈 slight round
        fg_color=color,
        hover_color="#009e8f",
        text_color="white",
        font=("Arial", 16)
    ).grid(row=row, column=col, columnspan=colspan,
           sticky="nsew", padx=5, pady=5)

# Top row
btn("CE", 0, 0, clear, op_color)
btn("+/-", 0, 1, lambda: press("-"), op_color)
btn("%", 0, 2, percent, op_color)
btn("/", 0, 3, lambda: press("/"), op_color)

# Numbers + operators
btn("7", 1, 0, lambda: press("7"), num_color)
btn("8", 1, 1, lambda: press("8"), num_color)
btn("9", 1, 2, lambda: press("9"), num_color)
btn("*", 1, 3, lambda: press("*"), op_color)

btn("4", 2, 0, lambda: press("4"), num_color)
btn("5", 2, 1, lambda: press("5"), num_color)
btn("6", 2, 2, lambda: press("6"), num_color)
btn("-", 2, 3, lambda: press("-"), op_color)

btn("1", 3, 0, lambda: press("1"), num_color)
btn("2", 3, 1, lambda: press("2"), num_color)
btn("3", 3, 2, lambda: press("3"), num_color)
btn("+", 3, 3, lambda: press("+"), op_color)

# Bottom row
btn("0", 4, 0, lambda: press("0"), num_color, colspan=2)
btn(".", 4, 2, lambda: press("."), num_color)
btn("=", 4, 3, equal, op_color)

app.mainloop()
