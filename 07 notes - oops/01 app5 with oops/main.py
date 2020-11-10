from tkinter import *
from tkinter.ttk import Style
from db import Database

database = Database('books.db')

monospace_font='TkFixedFont'

class Window():

    def __init__(self,window):
        self.label_title = Label(master=window, text='Title')
        self.label_title.grid(row=0, column=0)
        self.title_text = StringVar()
        self.entry_title = Entry(window, textvariable=self.title_text)
        self.entry_title.grid(row=0, column=1)

        self.label_author = Label(window, text='Author')
        self.label_author.grid(row=0, column=2)
        self.author_text = StringVar()
        self.entry_author = Entry(window, textvariable=self.author_text)
        self.entry_author.grid(row=0, column=3)

        self.label_year = Label(window, text='Year')
        self.label_year.grid(row=1, column=0)
        self.year_text = StringVar()
        self.entry_year = Entry(window, textvariable=self.year_text)
        self.entry_year.grid(row=1, column=1)

        self.label_isbn = Label(window, text='ISBN')
        self.label_isbn.grid(row=1, column=2)
        self.isbn_text = StringVar()
        self.entry_isbn = Entry(window, textvariable=self.isbn_text)
        self.entry_isbn.grid(row=1, column=3)

        self.scrollbar = Scrollbar(window)
        self.scrollbar.grid(row=2, column=2, rowspan=6)
        self.listbox = Listbox(window, height=6, width=40)
        self.listbox.grid(row=2, column=0, columnspan=2, rowspan=6)
        self.listbox.configure(yscrollcommand=self.scrollbar.set, font=monospace_font)
        self.scrollbar.configure(command=self.listbox.yview)
        self.listbox.bind('<<ListboxSelect>>', self.get_selected_row)

        self.btn_viewall = Button(window, text='View All', width=12,command=self.view_command)
        self.btn_viewall.grid(row=2, column=3)

        self.btn_search = Button(window, text='Search', width=12,command=self.search_command)
        self.btn_search.grid(row=3, column=3)

        self.btn_add = Button(window, text='Add', width=12,command=self.add_command)
        self.btn_add.grid(row=4, column=3)

        self.btn_update = Button(window, text='Update', width=12, command=self.update_command)
        self.btn_update.grid(row=5, column=3)

        self.btn_delete = Button(window, text='Delete', width=12, command=self.delete_command)
        self.btn_delete.grid(row=6, column=3)

        self.btn_close = Button(window, text='Close', width=12, command=window.destroy)
        self.btn_close.grid(row=7, column=3)

    def get_selected_row(self,event):
        try:
            idx = self.listbox.curselection()[0]
            self.global_data = self.listbox.get(idx)
            row_data = self.global_data.split('|')[1:]
            self.entry_title.delete(0,END)
            self.entry_title.insert(END,row_data[0].strip())
            self.entry_author.delete(0,END)
            self.entry_author.insert(END,row_data[1].strip())
            self.entry_year.delete(0,END)
            self.entry_year.insert(END,row_data[2].strip())
            self.entry_isbn.delete(0,END)
            self.entry_isbn.insert(END,row_data[3].strip())
        except IndexError:
            pass

    def refresh(self):
        self.title_text.set('')
        self.author_text.set('')
        self.year_text.set('')
        self.isbn_text.set('')

    def refresh_list(self):
        self.listbox.delete(0,END)

    def view_command(self):
        self.refresh()
        self.refresh_list()
        for row in database.view():
            self.listbox.insert(END,'{:2d}|{:6s}|{:6s}|{:4d}|{:10d}'.format(row[0],row[1],row[2],row[3],row[4]))

    def search_command(self):
        self.refresh_list()
        for row in database.search(self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get()):
            self.listbox.insert(END,'{:2d}|{:6s}|{:6s}|{:4d}|{:10d}'.format(row[0],row[1],row[2],row[3],row[4]))

    def add_command(self):
        database.insert(self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get())
        self.view_command()

    def update_command(self):
        data = self.global_data.split('|')
        database.update(data[0].strip(), self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get())
        self.view_command()

    def delete_command(self):
        database.delete(self.global_data.split('|')[0].strip())
        self.view_command()

if __name__ == "__main__":
    window = Tk()
    window.wm_title('Book List Recorder')   
    Window(window).view_command()
    window.mainloop()