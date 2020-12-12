import os
import sqlite3
from sqlite3 import Error
import tkinter as printer

currentDir = str(os.getcwd()) + '\\contactbook.db'
conn = sqlite3.connect(currentDir)
newTable = 'CREATE TABLE IF NOT EXISTS contacts(id integer PRIMARY KEY, name text NOT NULL, phone integer, email text);'
cur = conn.cursor()
cur.execute(newTable)


def new_id(name, number, email=''):

    with conn:
        project = (name, number, email)
        project_id = add_table(project)


def add_table(table):


    sql = 'INSERT INTO contacts(name, phone, email) VALUES(?,?,?)'

    cur = conn.cursor()
    cur.execute(sql, table)
    conn.commit()
    return cur.lastrowid


def print_table():
    window = printer.Tk()
    window.geometry('530x250')
    set = conn.execute('SELECT * FROM contacts LIMIT 0,10')
    i=0



    for contact in set:
        for j in range(len(contact)):
            e = printer.Text(window, height=1, width=15, padx=5, pady=5)
            e.grid(row=i, column=j)
            e.insert(printer.END, contact[j])
            if j == (len(contact)-1):
                print('inside')
                buttonClose = printer.Button(window, text='Close', width=10, height=5, command=window.destroy)
                buttonClose.grid(row=i+1, column=0)
        i+=1



def edit_table(contact):
    sql = 'UPDATE contacts SET name = ?, phone = ?, email = ?'
    cur = conn.cursor()
    cur.execute(sql, contact)
    conn.commit()
