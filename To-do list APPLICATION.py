#!/usr/bin/env python
# coding: utf-8

# # TO-DO List Application
# This To-Do List application allows users to manage their tasks efficiently through a simple and intuitive graphical interface. Users can add, update, and delete tasks, with appropriate feedback and error handling provided through message boxes. The use of tkinter ensures that the interface is responsive and easy to use. Here we will perform some basic application of to observe how a task is added,updated or deleted
# 

# In[2]:


import tkinter as tk
from tkinter import messagebox


# tkinter: The standard Python interface to the Tk GUI toolkit. We use this to create the graphical user interface.
# messagebox: A module in tkinter that provides a set of standard dialog boxes for messages.

# In[3]:


class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        
        self.tasks = []
        
        self.task_frame = tk.Frame(root)
        self.task_frame.pack(pady=10)
        
        self.task_listbox = tk.Listbox(self.task_frame, height=10, width=50)
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)
        
        self.scrollbar = tk.Scrollbar(self.task_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)
        
        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)
        
        self.entry = tk.Entry(root, width=50)
        self.entry.pack(pady=10)
        
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=10)
        
        self.add_task_button = tk.Button(self.button_frame, text="Add Task", command=self.add_task)
        self.add_task_button.pack(side=tk.LEFT, padx=5)
        
        self.update_task_button = tk.Button(self.button_frame, text="Update Task", command=self.update_task)
        self.update_task_button.pack(side=tk.LEFT, padx=5)
        
        self.delete_task_button = tk.Button(self.button_frame, text="Delete Task", command=self.delete_task)
        self.delete_task_button.pack(side=tk.LEFT, padx=5)
    
    def add_task(self):
        task = self.entry.get()
        if task:
            self.tasks.append(task)
            self.update_listbox()
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")
    
    def update_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            new_task = self.entry.get()
            if new_task:
                self.tasks[selected_task_index] = new_task
                self.update_listbox()
                self.entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Warning", "You must enter a task.")
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to update.")
    
    def delete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.tasks.pop(selected_task_index)
            self.update_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to delete.")
    
    def update_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()


# Constructor (__init__ method):
# 
# Initializes the application with a root window, task list, and various UI components (frames, listbox, scrollbar, entry field, and buttons).
# self.tasks: A list to store tasks.
# self.task_frame: A frame to hold the listbox and scrollbar.
# self.task_listbox: A listbox to display tasks.
# self.scrollbar: A scrollbar for the listbox.
# self.entry: An entry field for entering new tasks.
# self.button_frame: A frame to hold the buttons.
# Three buttons: Add Task, Update Task, and Delete Task, each linked to their respective methods.
# 
# add_task method:
# 
# Gets the text from the entry field.
# Adds the task to the self.tasks list if the entry is not empty.
# Updates the listbox and clears the entry field.
# Shows a warning message if the entry is empty.
# 
# update_task method:
# 
# Gets the index of the selected task in the listbox.
# Replaces the selected task with the new task from the entry field if the entry is not empty.
# Updates the listbox and clears the entry field.
# Shows a warning message if no task is selected or the entry is empty.
# 
# delete_task method:
# 
# Gets the index of the selected task in the listbox.
# Removes the selected task from the self.tasks list.
# Updates the listbox.
# Shows a warning message if no task is selected.
# update_listbox method:
# 
# Clears the current listbox.
# Adds all tasks from self.tasks to the listbox
# 
# 
# 
# 

# In[ ]:




