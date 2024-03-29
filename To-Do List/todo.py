import tkinter as tk
from tkinter import messagebox

class TodoListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Colorful To-Do List App")
        self.master.configure(bg='#F0F0F0')  #Background color

        self.tasks = []

        self.task_var = tk.StringVar()
        self.task_entry = tk.Entry(master, textvariable=self.task_var, width=40, bd=2, relief=tk.GROOVE)
        self.task_entry.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

        self.add_button = tk.Button(master, text="Add Task", command=self.add_task, bg='#4CAF50', fg='white', relief=tk.GROOVE)
        self.add_button.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

        self.task_listbox = tk.Listbox(master, width=50, height=15, bd=2, relief=tk.GROOVE)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky=tk.W)

        self.complete_button = tk.Button(master, text="Mark as Completed", command=self.mark_completed, bg='#FFC107', fg='white', relief=tk.GROOVE)
        self.complete_button.grid(row=2, column=0, padx=5, pady=5, sticky="ew")

        self.delete_button = tk.Button(master, text="Delete Task", command=self.delete_task, bg='#F44336', fg='white', relief=tk.GROOVE)
        self.delete_button.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

        self.populate_task_listbox()

    def add_task(self):
        task = self.task_var.get().strip()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_var.set("")
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def populate_task_listbox(self):
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

    def mark_completed(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task_index = selected_task_index[0]
            self.task_listbox.itemconfig(task_index, {'bg': 'green', 'fg': 'white'})

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task_index = selected_task_index[0]
            self.task_listbox.delete(task_index)
            del self.tasks[task_index]

def main():
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
