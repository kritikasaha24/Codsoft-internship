#!/usr/bin/env python
# coding: utf-8

# # CONTACT BOOK
# In this task we will create a contact book and will store and perform the following tasks.
# 
# Contact Information: Store name, phone number, email, and address for each contact.
# 
# Add Contact: Allow users to add new contacts with their details.
# 
# View Contact List: Display a list of all saved contacts with names and phone numbers. 
# 
# Search Contact: Implement a search function to find contacts by name or phone number.
# 
# Update Contact: Enable users to update contact details.
# 
# Delete Contact: Provide an option to delete a contact.
# 
# User Interface: Design a user-friendly interface for easy interaction

# In[1]:


import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os


# tkinter: The standard Python interface to the Tk GUI toolkit.
# messagebox: Module for showing messages to the user.
# simpledialog: Module for simple dialogs to take input from the user.
# json: Module for reading and writing JSON files.
# os: Module for interacting with the operating system, used here to check if a file exists.

# In[ ]:


class ContactManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Manager")
        
        self.contacts = self.load_contacts()
        
        self.contact_frame = tk.Frame(root)
        self.contact_frame.pack(pady=10)
        
        self.contact_listbox = tk.Listbox(self.contact_frame, height=10, width=50)
        self.contact_listbox.pack(side=tk.LEFT, fill=tk.BOTH)
        
        self.scrollbar = tk.Scrollbar(self.contact_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)
        
        self.contact_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.contact_listbox.yview)
        
        self.entry_frame = tk.Frame(root)
        self.entry_frame.pack(pady=10)
        
        self.name_entry = tk.Entry(self.entry_frame, width=50)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)
        self.phone_entry = tk.Entry(self.entry_frame, width=50)
        self.phone_entry.grid(row=1, column=1, padx=5, pady=5)
        self.email_entry = tk.Entry(self.entry_frame, width=50)
        self.email_entry.grid(row=2, column=1, padx=5, pady=5)
        self.address_entry = tk.Entry(self.entry_frame, width=50)
        self.address_entry.grid(row=3, column=1, padx=5, pady=5)
        
        tk.Label(self.entry_frame, text="Name").grid(row=0, column=0, padx=5, pady=5)
        tk.Label(self.entry_frame, text="Phone").grid(row=1, column=0, padx=5, pady=5)
        tk.Label(self.entry_frame, text="Email").grid(row=2, column=0, padx=5, pady=5)
        tk.Label(self.entry_frame, text="Address").grid(row=3, column=0, padx=5, pady=5)
        
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=10)
        
        self.add_contact_button = tk.Button(self.button_frame, text="Add Contact", command=self.add_contact)
        self.add_contact_button.pack(side=tk.LEFT, padx=5)
        
        self.update_contact_button = tk.Button(self.button_frame, text="Update Contact", command=self.update_contact)
        self.update_contact_button.pack(side=tk.LEFT, padx=5)
        
        self.delete_contact_button = tk.Button(self.button_frame, text="Delete Contact", command=self.delete_contact)
        self.delete_contact_button.pack(side=tk.LEFT, padx=5)
        
        self.search_button = tk.Button(self.button_frame, text="Search Contact", command=self.search_contact)
        self.search_button.pack(side=tk.LEFT, padx=5)
        
        self.update_contact_listbox()
    
    def load_contacts(self, filename="contacts.json"):
        if os.path.exists(filename):
            with open(filename, "r") as file:
                return json.load(file)
        else:
            return []
    
    def save_contacts(self, filename="contacts.json"):
        with open(filename, "w") as file:
            json.dump(self.contacts, file, indent=4)
    
    def add_contact(self):
        contact = {
            "name": self.name_entry.get(),
            "phone": self.phone_entry.get(),
            "email": self.email_entry.get(),
            "address": self.address_entry.get()
        }
        if all(contact.values()):
            self.contacts.append(contact)
            self.update_contact_listbox()
            self.clear_entries()
            self.save_contacts()
        else:
            messagebox.showwarning("Warning", "All fields must be filled.")
    
    def update_contact(self):
        try:
            selected_contact_index = self.contact_listbox.curselection()[0]
            contact = {
                "name": self.name_entry.get(),
                "phone": self.phone_entry.get(),
                "email": self.email_entry.get(),
                "address": self.address_entry.get()
            }
            if all(contact.values()):
                self.contacts[selected_contact_index] = contact
                self.update_contact_listbox()
                self.clear_entries()
                self.save_contacts()
            else:
                messagebox.showwarning("Warning", "All fields must be filled.")
        except IndexError:
            messagebox.showwarning("Warning", "You must select a contact to update.")
    
    def delete_contact(self):
        try:
            selected_contact_index = self.contact_listbox.curselection()[0]
            self.contacts.pop(selected_contact_index)
            self.update_contact_listbox()
            self.save_contacts()
        except IndexError:
            messagebox.showwarning("Warning", "You must select a contact to delete.")
    
    def search_contact(self):
        search_term = simpledialog.askstring("Search Contact", "Enter name or phone number:")
        results = [contact for contact in self.contacts if search_term.lower() in contact["name"].lower() or search_term in contact["phone"]]
        
        if results:
            self.contact_listbox.delete(0, tk.END)
            for contact in results:
                self.contact_listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")
        else:
            messagebox.showinfo("Search Result", "No contacts found.")
    
    def update_contact_listbox(self):
        self.contact_listbox.delete(0, tk.END)
        for contact in self.contacts:
            self.contact_listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")
    
    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManagerApp(root)
    root.mainloop()


# In[ ]:




