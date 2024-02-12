import tkinter as tk
from tkinter import messagebox

class ContactBookApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Colorful Contact Book")
        self.master.configure(bg='#F0F0F0')

        self.contacts = []

        self.name_var = tk.StringVar()
        self.phone_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.address_var = tk.StringVar()

        # Labels and Entry Widgets
        tk.Label(master, text="Name:", bg='#F0F0F0').grid(row=0, column=0, padx=5, pady=5)
        tk.Entry(master, textvariable=self.name_var).grid(row=0, column=1, padx=5, pady=5)

        tk.Label(master, text="Phone:", bg='#F0F0F0').grid(row=1, column=0, padx=5, pady=5)
        tk.Entry(master, textvariable=self.phone_var).grid(row=1, column=1, padx=5, pady=5)

        tk.Label(master, text="Email:", bg='#F0F0F0').grid(row=2, column=0, padx=5, pady=5)
        tk.Entry(master, textvariable=self.email_var).grid(row=2, column=1, padx=5, pady=5)

        tk.Label(master, text="Address:", bg='#F0F0F0').grid(row=3, column=0, padx=5, pady=5)
        tk.Entry(master, textvariable=self.address_var).grid(row=3, column=1, padx=5, pady=5)

        # Buttons
        tk.Button(master, text="Add Contact", command=self.add_contact, bg='#4CAF50', fg='white').grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="ew")
        tk.Button(master, text="View Contacts", command=self.view_contacts, bg='#2196F3', fg='white').grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="ew")
        tk.Button(master, text="Search Contact", command=self.search_contact, bg='#FFC107', fg='black').grid(row=6, column=0, columnspan=2, padx=5, pady=5, sticky="ew")
        tk.Button(master, text="Update Contact", command=self.update_contact, bg='#FF5722', fg='white').grid(row=7, column=0, columnspan=2, padx=5, pady=5, sticky="ew")
        tk.Button(master, text="Delete Contact", command=self.delete_contact, bg='#F44336', fg='white').grid(row=8, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

    def add_contact(self):
        name = self.name_var.get().strip()
        phone = self.phone_var.get().strip()
        email = self.email_var.get().strip()
        address = self.address_var.get().strip()

        if name and phone:
            self.contacts.append({"name": name, "phone": phone, "email": email, "address": address})
            messagebox.showinfo("Success", "Contact added successfully!")
            self.clear_entries()
        else:
            messagebox.showwarning("Warning", "Name and Phone fields are required.")

    def clear_entries(self):
        self.name_var.set("")
        self.phone_var.set("")
        self.email_var.set("")
        self.address_var.set("")

    def view_contacts(self):
        contact_list = "\n".join([f"Name: {contact['name']}, Phone: {contact['phone']}" for contact in self.contacts])
        messagebox.showinfo("Contact List", contact_list)

    def search_contact(self):
        search_term = self.name_var.get().strip()
        if not search_term:
            messagebox.showwarning("Warning", "Please enter a search term.")
            return

        found_contacts = [contact for contact in self.contacts if search_term.lower() in contact['name'].lower() or search_term in contact['phone']]
        if found_contacts:
            contact_list = "\n".join([f"Name: {contact['name']}, Phone: {contact['phone']}" for contact in found_contacts])
            messagebox.showinfo("Search Results", contact_list)
        else:
            messagebox.showinfo("Search Results", "No contacts found.")

    def update_contact(self):
        pass  # To be implemented

    def delete_contact(self):
        pass  # To be implemented

def main():
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
