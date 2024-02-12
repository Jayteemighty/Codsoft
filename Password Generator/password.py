import tkinter as tk
import random
import string

class PasswordGeneratorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Colorful Password Generator")
        self.master.configure(bg='#F0F0F0')  #Background color

        self.password_var = tk.StringVar()

        self.password_label = tk.Label(master, text="Generated Password:", bg='#F0F0F0')
        self.password_label.grid(row=0, column=0, padx=5, pady=5)

        self.password_entry = tk.Entry(master, textvariable=self.password_var, width=30, bd=2, relief=tk.GROOVE)
        self.password_entry.grid(row=0, column=1, padx=5, pady=5)

        self.generate_button = tk.Button(master, text="Generate Password", command=self.generate_password, bg='#4CAF50', fg='white', relief=tk.GROOVE)
        self.generate_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

    def generate_password(self):
        password_length = 12
        password_characters = string.ascii_letters + string.digits + string.punctuation
        generated_password = ''.join(random.choice(password_characters) for i in range(password_length))
        self.password_var.set(generated_password)

def main():
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
