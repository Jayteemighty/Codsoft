import tkinter as tk
from tkinter import ttk

class CalculatorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Colorful Calculator")
        self.master.configure(bg='#F0F0F0')

        self.expression = ""

        #Entry widget to display expression
        self.entry = ttk.Entry(master, font=('Arial', 20), justify='right')
        self.entry.grid(row=0, column=0, columnspan=4, sticky="ew", padx=10, pady=10)

        # Buttons for digits and operations
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]

        for (text, row, col) in buttons:
            button = ttk.Button(master, text=text, command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)
            button.config(style='C.TButton')

       
        s = ttk.Style()
        s.configure('C.TButton', font=('Arial', 18), background='#4CAF50', foreground='white')

    def on_button_click(self, char):
        if char == '=':
            try:
                self.expression = str(eval(self.expression))
            except Exception as e:
                self.expression = "Error"
        else:
            if self.expression == "Error":
                self.expression = ""
            self.expression += char

        self.entry.delete(0, tk.END)
        self.entry.insert(0, self.expression)

def main():
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
