import ast
import os
import tkinter as AddressBook
from ProjectSQ import print_table, new_id

fields = 'Firstname', 'Lastname', 'Phone Number', 'Email'


def saveContact(entries, window):
    name = entries['Firstname'].get() + ' ' + entries['Lastname'].get()
    number = entries['Phone Number'].get()
    email = entries['Email'].get()
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

    new_id(name, number, email)

    window.destroy()


def show_entry_fields(entries):
    window = AddressBook.Tk()

    for field in fields:
        row = AddressBook.Frame(window)
        lab = AddressBook.Label(row, width=15, text=field + ': ', anchor='w')
        ent = AddressBook.Text(row, height=1, width=40)
        ent.insert(AddressBook.END, entries[str(field)].get())
        row.pack(side=AddressBook.TOP, fill=AddressBook.X, padx=5, pady=5)
        lab.pack(side=AddressBook.LEFT)
        ent.pack(side=AddressBook.RIGHT, expand=AddressBook.YES, fill=AddressBook.X)

    buttonSave = AddressBook.Button(window, text='Save', width=10, height=5,
                                    command=(lambda e=ents: saveContact(e, window)))
    buttonSave.pack(side=AddressBook.LEFT, padx=5, pady=5)


def makeform(root, fields):
    entries = {}
    for field in fields:
        row = AddressBook.Frame(root)
        lab = AddressBook.Label(row, width=15, text=field, anchor='w')
        ent = AddressBook.Entry(row, width=40)
        row.pack(side=AddressBook.TOP, fill=AddressBook.X, padx=5, pady=5)
        lab.pack(side=AddressBook.LEFT)
        ent.pack(side=AddressBook.RIGHT, expand=AddressBook.YES, fill=AddressBook.X)
        entries[field] = ent
    return entries


if __name__ == '__main__':
    root = AddressBook.Tk()
    ents = makeform(root, fields)
    root.bind('<Return>', (lambda event, e=ents: show_entry_fields(e)))
    buttonShow = AddressBook.Button(root, text='Add', width=10, height=5, command=(lambda e=ents: show_entry_fields(e)))
    buttonShow.pack(side=AddressBook.LEFT, padx=10, pady=10)
    buttonShow = AddressBook.Button(root, text='Edit', width=10, height=5,
                                    command=(lambda e=ents: show_entry_fields(e)))
    buttonShow.pack(side=AddressBook.LEFT, padx=10, pady=10)
    buttonPrint = AddressBook.Button(root, text='Print', width=10, height=5, command=print_table())
    buttonPrint.pack(side=AddressBook.LEFT, padx=10, pady=10)
    buttonQuit = AddressBook.Button(root, text='Quit', width=10, height=5, command=root.quit)
    buttonQuit.pack(side=AddressBook.RIGHT, padx=10, pady=10)

    root.mainloop()
