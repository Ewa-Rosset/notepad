import sqlite3
from tkinter import *
from tkinter import ttk
from datetime import datetime

def add_note():
    conn = sqlite3.connect('db_notes.db')
    c = conn.cursor()

    title = input("Type the title: ")
    note = input("Input Note: ")
    datetimeObj = datetime.now()
    timestamp = datetimeObj.strftime("%d-%b-%Y (%H:%M:%S)")

    c.execute("INSERT INTO tb_notes VALUES (?, ?, ?)", (title, note, timestamp))
    
    conn.commit()
    print("Note added successfully")

def delete_note():
    deletion = input("Input the title of the note you wish to remove: ")

    with conn:
        c.execute("DELETE from tb_notes WHERE title=?", (deletion,))
        conn.commit()
        print("Note removed successfully")
    

def display_notes():

    conn = sqlite3.connect('db_notes.db')
    c = conn.cursor()

    c.execute("SELECT * FROM tb_notes")
    items = c.fetchall()

    index = 1

    for item in items:
        print(str(index) + ".", item[0]+ ":", item[1], item[2])
        index += 1

    conn.commit()

def search():

    letters = input('Search: ')

    with conn:
        c.execute("SELECT * FROM tb_notes WHERE title LIKE ? or note LIKE ?", ('%'+letters+'%', '%'+letters+'%'))
        print(c.fetchall())

    

def main_display():

    while True:

        answer = input("Welcome to sister notepad. Please select a, b or c \n a) add new note \n b) display notes \n c) delete note\n d) search\n e) exit \nAnswer: ")

        if answer.upper() == "A":
            add_note()
        elif answer.upper() == "B":
            display_notes()
        
        elif answer.upper() == "C":
            display_notes()
            delete_note()

        elif answer.upper() == 'D':
            search()
        
        elif answer.upper() == "E":
            return False
        
    
        
conn = sqlite3.connect('db_notes.db')
c = conn.cursor()

main_display()

conn.commit()
conn.close()



