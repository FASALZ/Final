import tkinter as tk
from tkinter import simpledialog, messagebox

# Base class for any person
class Person:
    def __init__(self, id, name, address, contact_details):
        self.id = id
        self.name = name
        self.address = address
        self.contact_details = contact_details

# Specific classes for each entity
class Employee(Person):
    def __init__(self, id, name, address, contact_details, job_title, salary):
        super().__init__(id, name, address, contact_details)
        self.job_title = job_title
        self.salary = salary

class Client(Person):
    def __init__(self, id, name, address, contact_details):
        super().__init__(id, name, address, contact_details)

class Guest(Person):
    def __init__(self, id, name, address, contact_details):
        super().__init__(id, name, address, contact_details)

class Supplier:
    def __init__(self, id, name, service):
        self.id = id
        self.name = name
        self.service = service

class Event:
    def __init__(self, id, name, date, venue):
        self.id = id
        self.name = name
        self.date = date
        self.venue = venue

class Venue:
    def __init__(self, id, name, address, capacity):
        self.id = id
        self.name = name
        self.address = address
        self.capacity = capacity

# Management system class
class ManagementSystem:
    def __init__(self, master):
        self.master = master
        self.master.title("Management System")
        self.employees = {}
        self.clients = {}
        self.guests = {}
        self.suppliers = {}
        self.events = {}
        self.venues = {}

        # Setup GUI for all entities
        self.setup_gui('Employee', self.employees, Employee)
        self.setup_gui('Client', self.clients, Client)
        self.setup_gui('Guest', self.guests, Guest)
        self.setup_gui('Supplier', self.suppliers, Supplier)
        self.setup_gui('Event', self.events, Event)
        self.setup_gui('Venue', self.venues, Venue)

    def setup_gui(self, entity_name, storage_dict, entity_class):
        tk.Label(self.master, text=f"{entity_name} Management", font=("Arial", 16)).pack()
        tk.Button(self.master, text=f"Add {entity_name}", command=lambda: self.add_entity(entity_name, storage_dict, entity_class)).pack()
        tk.Button(self.master, text=f"Delete {entity_name}", command=lambda: self.delete_entity(entity_name, storage_dict)).pack()
        tk.Button(self.master, text=f"Modify {entity_name}", command=lambda: self.modify_entity(entity_name, storage_dict, entity_class)).pack()
        tk.Button(self.master, text=f"Display {entity_name}", command=lambda: self.display_entity(entity_name, storage_dict)).pack()

    def add_entity(self, entity_name, storage_dict, entity_class):
        details = {attr: simpledialog.askstring("Input", f"Enter {entity_name} {attr}:") for attr in entity_class.__init__.__code__.co_varnames[1:]}
        entity = entity_class(**details)
        if details['id'] in storage_dict:
            messagebox.showerror("Error", f"{entity_name} ID already exists.")
            return
        storage_dict[details['id']] = entity
        messagebox.showinfo("Success", f"{entity_name} added successfully!")

    def delete_entity(self, entity_name, storage_dict):
        id = simpledialog.askstring("Input", f"Enter {entity_name} ID to delete:")
        if id in storage_dict:
            del storage_dict[id]
            messagebox.showinfo("Success", f"{entity_name} deleted successfully!")
        else:
            messagebox.showerror("Error", f"{entity_name} not found.")

    def modify_entity(self, entity_name, storage_dict, entity_class):
        id = simpledialog.askstring("Input", f"Enter {entity_name} ID to modify:")
        if id not in storage_dict:
            messagebox.showerror("Error", f"{entity_name} not found.")
            return
        details = {attr: simpledialog.askstring("Input", f"Enter new {entity_name} {attr}:") for attr in entity_class.__init__.__code__.co_varnames[1:]}
        entity = entity_class(**details)
        storage_dict[id] = entity
        messagebox.showinfo("Success", f"{entity_name} details updated successfully!")

    def display_entity(self, entity_name, storage_dict):
        id = simpledialog.askstring("Input", f"Enter {entity_name} ID to display:")
        if id in storage_dict:
            entity = storage_dict[id]
            details = "\n".join([f"{attr}: {getattr(entity, attr)}" for attr in entity.__dict__])
            messagebox.showinfo(f"{entity_name} Details", details)
        else:
            messagebox.showerror("Error", f"{entity_name} not found.")

# Run the application
root = tk.Tk()
app = ManagementSystem(root)
root.mainloop()
