# CS 3080 Course/Main Project
# NIck Barcalow
# Lynel Peregrino
# Due date: 12/14/20
#This program creates and displays the UI.

# Imports and global variables.
import ast
import os
import tkinter as AddressBook
from ProjectSQ import print_table, new_id, delete_table

# global variables
fields = 'Firstname', 'Lastname', 'Phone Number', 'Email'

# function for saving contacts
def saveContact(entries, window):
    # variables for the contacts
    name = entries['Firstname'].get() + ' ' + entries['Lastname'].get()
    number = entries['Phone Number'].get()
    email = entries['Email'].get()

    # this was the temp .txt database mentioned in the report
    '''
    fileExist = str(os.getcwd()) + '/saved contacts.txt'

    if not os.path.exists(fileExist):
        dict = {}
        saveFile = open('saved contacts.txt', 'w')
        dict[name] = number, email
        saveFile.write(str(dict))

    else:
        with open('saved contacts.txt') as f:
            data = f.read()
        saveFile = open('saved contacts.txt', 'w+')

        dicky = ast.literal_eval(data)
        dicky[name] = number, email
        saveFile.write(str(dicky))

    saveFile.close()
    '''
    # calls new id function in database
    new_id(name, number, email)
    # closes "Save" window
    window.destroy()

# Display information that's entered before calling "Saved" Function
def show_entry_fields(entries):
   # calls new window
    window = AddressBook.Tk()

   # loops that fills the fields with the information in the window
    for field in fields:
        row = AddressBook.Frame(window)
        lab = AddressBook.Label(row, width=15, text=field + ': ', anchor='w')
        ent = AddressBook.Text(row, height=1, width=40)
        ent.insert(AddressBook.END, entries[str(field)].get())
        row.pack(side=AddressBook.TOP, fill=AddressBook.X, padx=5, pady=5)
        lab.pack(side=AddressBook.LEFT)
        ent.pack(side=AddressBook.RIGHT, expand=AddressBook.YES, fill=AddressBook.X)
    # created the save button that calls the save function
    buttonSave = AddressBook.Button(window, text='Save', width=10, height=5,
                                    command=(lambda e=ents: saveContact(e, window)))
    buttonSave.pack(side=AddressBook.LEFT, padx=5, pady=5)

# creates the first window with empty fields before entering the information
def makeform(root, fields):
    # dictionary that saves entered information
    entries = {}

    # loops that creates the empty fields
    for field in fields:
        row = AddressBook.Frame(root)
        lab = AddressBook.Label(row, width=15, text=field, anchor='w')
        ent = AddressBook.Entry(row, width=40)
        row.pack(side=AddressBook.TOP, fill=AddressBook.X, padx=5, pady=5)
        lab.pack(side=AddressBook.LEFT)
        ent.pack(side=AddressBook.RIGHT, expand=AddressBook.YES, fill=AddressBook.X)
        entries[field] = ent
    return entries

# main function that creates windows and buttons Ex. creates the buttons Add, Delete, Print, Quit
if __name__ == '__main__':
    root = AddressBook.Tk()
    ents = makeform(root, fields)
    root.bind('<Return>', (lambda event, e=ents: show_entry_fields(e)))
    buttonAdd = AddressBook.Button(root, text='Add', width=10, height=5, command=(lambda e=ents: show_entry_fields(e)))
    buttonAdd.pack(side=AddressBook.LEFT, padx=10, pady=10)
    buttonDelete = AddressBook.Button(root, text='Delete', width=10, height=5,
                                    command=(lambda e=ents: delete_table((ents[str('Firstname')].get()) + ' ' + ents[str('Lastname')].get())))
    buttonDelete.pack(side=AddressBook.LEFT, padx=10, pady=10)
    buttonPrint = AddressBook.Button(root, text='Print', width=10, height=5, command=print_table)
    buttonPrint.pack(side=AddressBook.LEFT, padx=10, pady=10)
    buttonQuit = AddressBook.Button(root, text='Quit', width=10, height=5, command=root.quit)
    buttonQuit.pack(side=AddressBook.RIGHT, padx=10, pady=10)

    root.mainloop()
