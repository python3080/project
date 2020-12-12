import os
import sqlite3
from sqlite3 import Error

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

    cur = conn.cursor()
    cur.execute('SELECT * from contact')
    rows = cur.fetchall()

    for row in rows:
        print(row)


def edit_table(contact):
    sql = 'UPDATE contacts SET name = ?, phone = ?, email = ?'
    cur = conn.cursor()
    cur.execute(sql, contact)
    conn.commit()
