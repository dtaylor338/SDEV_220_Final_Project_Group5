import tkinter as tk
from tkinter.ttk import Treeview
from tkinter import *
from classes import *


# Main window options
window = tk.Tk()
window.title('Kenny Kent Chevrolet Inventory Search')
window.geometry('300x200')
window.columnconfigure(0, weight=1)
window.columnconfigure(4, weight=1)


# Variables
used_var = tk.IntVar()
new_var = tk.IntVar()
make_var = tk.StringVar()
model_var = tk.StringVar()
year_var = tk.IntVar()
price_var = tk.IntVar()
result_set = []


# New/Used Checkboxes
used_box = tk.Checkbutton(window, text='Used', variable=used_var, onvalue=1, offvalue=0)
new_box = tk.Checkbutton(window, text='New', variable=new_var, onvalue=1, offvalue=0)
used_box.grid(row=1, column=2)
new_box.grid(row=1, column=3)

# Make entry box
make_label = tk.Label(window, text='Make: ')
make_entry = tk.Entry(window, textvariable=make_var)
make_label.grid(row=2, column=2)
make_entry.grid(row=2, column=3)

# Model entry box
model_label = tk.Label(window, text='Model: ')
model_entry = tk.Entry(window, textvariable=model_var)
model_label.grid(row=3, column=2)
model_entry.grid(row=3, column=3)

# Year entry box
year_label = tk.Label(window, text='Year: ')
year_entry = tk.Entry(window, textvariable=year_var)
year_label.grid(row=4, column=2)
year_entry.grid(row=4, column=3)

# Price Entry
price_label = tk.Label(window, text='Price')
price_entry = tk.Entry(window, textvariable=price_var)
price_label.grid(row=5, column=2)
price_entry.grid(row=5, column=3)


# Search Button Click
def search():
    if used_var.get() == 1:
        used_inventory_search()
    elif new_var.get() == 1:
        new_inventory_search()
    else:
        if not make_var.get() and not model_var.get() and not year_var.get() and not price_var.get():
            error()
        else:
            all_inventory_search()


# Search button
search_button = tk.Button(window, text='Search', command=search)
search_button.grid(row=7, column=3)


# Error Window
def error():
    error_window = tk.Tk()
    error_window.title('Error')
    error_label = tk.Label(error_window, text='Invalid Input')
    error_label.pack()


# Used Search Function
def used_inventory_search():
    us = used_search()
    make = make_var.get()
    print(make)
    model = model_var.get()
    year = int(year_var.get())
    price = int(price_var.get())
    if make != " ":
        make_result = us.make_search(make)
        for n in make_result:
            if n not in result_set:
                result_set.append(n)
    if model:
        model_result = us.model_search(model)
        for n in model_result:
            if n not in result_set:
                result_set.append(n)
    if year:
        year_result = us.year_search(year)
        for n in year_result:
            if n not in result_set:
                result_set.append(n)
    if price:
        price_result = us.price_search(price)
        for n in price_result:
            if n not in result_set:
                result_set.append(n)
    result_window()


def new_inventory_search():
    ns = new_search()
    model = model_var.get()
    price = int(price_var.get())
    if model:
        model_result = ns.model_search(model)
        for n in model_result:
            if n not in result_set:
                result_set.append(n)
    if price:
        price_result = ns.price_search(price)
        for n in price_result:
            if n not in result_set:
                result_set.append(n)
    result_window()


def all_inventory_search():
    alls = all_search()
    make = make_var.get()
    model = model_var.get()
    year = int(year_var.get())
    price = int(price_var.get())
    if make:
        make_result = alls.make_search(make)
        for n in make_result:
            if n not in result_set:
                result_set.append(n)
    if model:
        model_result = alls.model_search(model)
        for n in model_result:
            if n not in result_set:
                result_set.append(n)
    if year:
        year_result = alls.year_search(year)
        for n in year_result:
            if n not in result_set:
                result_set.append(n)
    if price:
        price_result = alls.price_search(price)
        for n in price_result:
            if n not in result_set:
                result_set.append(n)
    result_window()


# Search Result Window
def result_window():
    result_win = tk.Tk()
    result_win.title('Results')

    tree = Treeview(result_win, columns=('Make', 'Model', 'Year', 'Price'), show='headings')
    tree["columns"] = ('Make', 'Model', 'Year', 'Price')

    tree.column('#1', anchor=CENTER)
    tree.heading('#1', text='Make')
    tree.column('#2', anchor=CENTER)
    tree.heading('#2', text='Model')
    tree.column('#3', anchor=CENTER)
    tree.heading('#3', text='Year')
    tree.column('#4', anchor=CENTER)
    tree.heading('#4', text='Price')

    tree.pack()
    for i, n in enumerate(result_set):
        col1 = n[0]
        col2 = n[1]
        col3 = n[2]
        col4 = n[3]

        tree.insert('', 'end', text=f'{i}', values=(col1, col2, col3, col4))


window.mainloop()
