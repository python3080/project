# CS 3080 Course/Main Project
# NIck Barcalow
# Lynel Peregrino
# Due date: 12/14/20
# This is the database function

# imports
import os
import sqlite3
from sqlite3 import Error
import tkinter as printer

# Global variables, the database connection, and creator
fields = 'Firstname', 'Lastname', 'Phone Number', 'Email'
currentDir = str(os.getcwd()) + '\\contactbook.db'
conn = sqlite3.connect(currentDir)
newTable = 'CREATE TABLE IF NOT EXISTS contacts(id integer PRIMARY KEY, name text NOT NULL, phone integer, email text);'
cur = conn.cursor()
cur.execute(newTable)

# creates new ids that are going to be added
def new_id(name, number, email=''):

    with conn:
        project = (name, number, email)
        project_id = add_table(project)

# creates new database entry/adds new id to database
def add_table(table):


    sql = 'INSERT INTO contacts(name, phone, email) VALUES(?,?,?)'

    cur = conn.cursor()
    cur.execute(sql, table)
    conn.commit()
    return cur.lastrowid

# prints the database
def print_table():
    window = printer.Tk()
    window.geometry('530x250')
    set = conn.execute('SELECT * FROM contacts LIMIT 0,10')
    i=0


    # loops through database, printing to UI
    for contact in set:
        for j in range(len(contact)):
            e = printer.Text(window, height=1, width=15, padx=5, pady=5)
            e.grid(row=i, column=j)
            e.insert(printer.END, contact[j])
        i+=1
    buttonClose = printer.Button(window, text='Close', width=10, height=5, command=window.destroy)
    buttonClose.grid(row=i + 1, column=0)

# Deletes entry desired from database
def delete_table(contact):
    sql = 'DELETE FROM contacts WHERE name = ?'
    cur = conn.cursor()
    cur.execute(sql, (contact,))
    conn.commit()
    print_table()
