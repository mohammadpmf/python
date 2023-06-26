from tkinter import *
from tkinter import ttk
class MyGameForm():
    def __init__(self, root, title='Game Info', l1='Name: ', l2='Company: ', l3='Genre: ', l4='Price: ', l5='Age: ', size=18):
        self.root       = root
        self.frame      = LabelFrame(self.root, bg='#333333', fg='orange', text=title, font=('', size), labelanchor='n', padx=5, pady=20)
        self.l_name     = Label(self.frame, text=l1, bg='#333333', fg='orange', font=('', size), padx=5, pady=5)
        self.l_company  = Label(self.frame, text=l2, bg='#333333', fg='orange', font=('', size), padx=5, pady=5)
        self.l_genre    = Label(self.frame, text=l3, bg='#333333', fg='orange', font=('', size), padx=5, pady=5)
        self.l_price    = Label(self.frame, text=l4, bg='#333333', fg='orange', font=('', size), padx=5, pady=5)
        self.l_age      = Label(self.frame, text=l5, bg='#333333', fg='orange', font=('', size), padx=5, pady=5)
        self.name       = Entry(self.frame, bg='#333333', fg='orange', width=20, font=('', size))
        self.company    = Entry(self.frame, bg='#333333', fg='orange', width=20, font=('', size))
        self.genre      = Entry(self.frame, bg='#333333', fg='orange', width=20, font=('', size))
        self.price      = Entry(self.frame, bg='#333333', fg='orange', width=20, font=('', size))

        # Stackoverflow
        combostyle = ttk.Style()
        combostyle.theme_create('combostyle', parent='alt', settings = {
            'TCombobox': {
                'configure': {
                    'selectbackground': '#333333',
                    'selectforeground': 'orange',
                    'fieldbackground': '#333333',
                    'background': '#333333',
                    }
                }
            })
        combostyle.theme_use('combostyle')
        # End of Stackoverflow

        self.age        = ttk.Combobox(self.frame, values=["+7", "+8", "+12", "+15", "+18", "+25"], foreground='orange', width=20, justify='center', font=('', size))
        self.age        .insert(0, "+7")
        self.age        .config(state='readonly')
        self.l_name     .grid(row=1, column=1, sticky='w', padx=3, pady=2)
        self.l_company  .grid(row=2, column=1, sticky='w', padx=3, pady=2)    
        self.l_genre    .grid(row=3, column=1, sticky='w', padx=3, pady=2)    
        self.l_price    .grid(row=4, column=1, sticky='w', padx=3, pady=2)    
        self.l_age      .grid(row=5, column=1, sticky='w', padx=3, pady=2)
        self.name       .grid(row=1, column=2, sticky='news', padx=3, pady=2)
        self.company    .grid(row=2, column=2, sticky='news', padx=3, pady=2)    
        self.genre      .grid(row=3, column=2, sticky='news', padx=3, pady=2)
        self.price      .grid(row=4, column=2, sticky='news', padx=3, pady=2)
        self.age        .grid(row=5, column=2, sticky='news', padx=3, pady=2)

    def grid(self, row=1, column=1, rowspan=1, columnspan=1, sticky='news', padx=20, pady=10):
        self.frame.grid(row=row, column=column, rowspan=rowspan, columnspan=columnspan, sticky=sticky, padx=padx, pady=pady)
    
    def place(self, *args, **kwargs):
        self.frame.place(*args, **kwargs)

    def pack(self, *args, **kwargs):
        self.frame.pack(*args, **kwargs)

if __name__ == '__main__':
    root = Tk()
    insert_form = MyGameForm(root)
    insert_form.grid(row=1, column=2)
    root.mainloop()