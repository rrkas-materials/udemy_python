from tkinter import *
from tkinter.ttk import Style
import db

window = Tk()
window.wm_title('Book List Recorder')

monospace_font='TkFixedFont'

label_title = Label(master=window, text='Title')
label_title.grid(row=0, column=0)
title_text = StringVar()
entry_title = Entry(window, textvariable=title_text)
entry_title.grid(row=0, column=1)

label_author = Label(window, text='Author')
label_author.grid(row=0, column=2)
author_text = StringVar()
entry_author = Entry(window, textvariable=author_text)
entry_author.grid(row=0, column=3)

label_year = Label(window, text='Year')
label_year.grid(row=1, column=0)
year_text = StringVar()
entry_year = Entry(window, textvariable=year_text)
entry_year.grid(row=1, column=1)

label_isbn = Label(window, text='ISBN')
label_isbn.grid(row=1, column=2)
isbn_text = StringVar()
entry_isbn = Entry(window, textvariable=isbn_text)
entry_isbn.grid(row=1, column=3)

def get_selected_row(event):
    try:
        global global_data
        idx = listbox.curselection()[0]
        global_data = listbox.get(idx)
        row_data = global_data.split('|')[1:]
        entry_title.delete(0,END)
        entry_title.insert(END,row_data[0].strip())
        entry_author.delete(0,END)
        entry_author.insert(END,row_data[1].strip())
        entry_year.delete(0,END)
        entry_year.insert(END,row_data[2].strip())
        entry_isbn.delete(0,END)
        entry_isbn.insert(END,row_data[3].strip())
    except IndexError:
        pass

scrollbar = Scrollbar(window)
scrollbar.grid(row=2, column=2, rowspan=6)
listbox = Listbox(window, height=6, width=40)
listbox.grid(row=2, column=0, columnspan=2, rowspan=6)
listbox.configure(yscrollcommand=scrollbar.set, font=monospace_font)
scrollbar.configure(command=listbox.yview)
listbox.bind('<<ListboxSelect>>', get_selected_row)

def refresh():
    title_text.set('')
    author_text.set('')
    year_text.set('')
    isbn_text.set('')

def refresh_list():
    listbox.delete(0,END)


def view_command():
    refresh()
    refresh_list()
    for row in db.view():
        listbox.insert(END,'{:2d}|{:6s}|{:6s}|{:4d}|{:10d}'.format(row[0],row[1],row[2],row[3],row[4]))

def search_command():
    refresh_list()
    for row in db.search(title_text.get(), author_text.get(),year_text.get(),isbn_text.get()):
        listbox.insert(END,'{:2d}|{:6s}|{:6s}|{:4d}|{:10d}'.format(row[0],row[1],row[2],row[3],row[4]))

def add_command():
    db.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    view_command()

def update_command():
    data = global_data.split('|')
    db.update(data[0].strip(), title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    view_command()

def delete_command():
    global_data.split('|')[0].strip()
    view_command()
    

btn_viewall = Button(window, text='View All', width=12,command=view_command)
btn_viewall.grid(row=2, column=3)

btn_search = Button(window, text='Search', width=12,command=search_command)
btn_search.grid(row=3, column=3)

btn_add = Button(window, text='Add', width=12,command=add_command)
btn_add.grid(row=4, column=3)

btn_update = Button(window, text='Update', width=12, command=update_command)
btn_update.grid(row=5, column=3)

btn_delete = Button(window, text='Delete', width=12, command=delete_command)
btn_delete.grid(row=6, column=3)

btn_close = Button(window, text='Close', width=12, command=window.destroy)
btn_close.grid(row=7, column=3)

if __name__ == "__main__":
    view_command()
    window.mainloop()