from tkinter import *
import db

window = Tk()
window.winfo_toplevel().title('Book List Recorder')

label_title = Label(master=window, text='Title')
label_title.grid(row=0, column=0)
title_text = StringVar()
entry_title = Entry(window, textvariable=title_text)
entry_title.grid(row=0, column=1)

label_author = Label(window, text='Author')
label_author.grid(row=0, column=2)
author_text = StringVar()
entry_title = Entry(window, textvariable=author_text)
entry_title.grid(row=0, column=3)

label_year = Label(window, text='Year')
label_year.grid(row=1, column=0)
year_text = StringVar()
entry_title = Entry(window, textvariable=year_text)
entry_title.grid(row=1, column=1)

label_isbn = Label(window, text='ISBN')
label_isbn.grid(row=1, column=2)
isbn_text = StringVar()
entry_title = Entry(window, textvariable=isbn_text)
entry_title.grid(row=1, column=3)

scrollbar = Scrollbar(window)
scrollbar.grid(row=2, column=2, rowspan=6)
listbox = Listbox(window, height=6, width=35)
listbox.grid(row=2, column=0, columnspan=2, rowspan=6)
listbox.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=listbox.yview)


def refresh():
    title_text.set('')
    author_text.set('')
    year_text.set('')
    isbn_text.set('')
    listbox.delete(0,END)


def view_command():
    refresh()
    for row in db.view():
        listbox.insert(END,'{:3d} | {:6s} | {:6s} | {:4d} | {:10d}'.format(row[0],row[1],row[2],row[3],row[4]))

btn_viewall = Button(window, text='View All', width=12,command=view_command)
btn_viewall.grid(row=2, column=3)

btn_search = Button(window, text='Search', width=12)
btn_search.grid(row=3, column=3)

btn_add = Button(window, text='Add', width=12)
btn_add.grid(row=4, column=3)

btn_update = Button(window, text='Update', width=12)
btn_update.grid(row=5, column=3)

btn_delete = Button(window, text='Delete', width=12)
btn_delete.grid(row=6, column=3)

btn_close = Button(window, text='Close', width=12)
btn_close.grid(row=7, column=3)

if __name__ == "__main__":
    window.mainloop()
