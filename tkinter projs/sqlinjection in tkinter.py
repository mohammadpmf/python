from tkinter import *
from tkinter import messagebox
import pymysql

connection = pymysql.connect(host='127.0.0.1', user='root', password='root')
mohammad = connection.cursor()
queries = [
    "CREATE SCHEMA IF NOT EXISTS `login`;",
    "CREATE TABLE IF NOT EXISTS `login`.`login` (`id` INT NOT NULL AUTO_INCREMENT, `username` VARCHAR(45) NOT NULL, `password` VARCHAR(45) NOT NULL, PRIMARY KEY (`id`), UNIQUE INDEX `username_UNIQUE` (`username` ASC) VISIBLE);",
    f"INSERT IGNORE INTO `login`.`login` (`username`, `password`) VALUES ('mohammad', '{chr(109)}{chr(11**2)} {chr(2**4*7)}{chr(97)}{chr(115)}s{chr(219-100)}{chr(111)}{chr(114)}{chr(100)}{chr(32)}{chr(215%110)}{chr(110+5)}{' '}{chr(58)}{chr(68)}');",
    f"INSERT IGNORE INTO `login`.`login` (`username`, `password`) VALUES ('ali', 'mbd46');",
    f"INSERT IGNORE INTO `login`.`login` (`username`, `password`) VALUES ('benyamin', 'cs50mrt');",
]

for query in queries:
    mohammad.execute(query)
connection.commit()

def login():
    query = f"SELECT * FROM `login`.`login` WHERE username='{entry1.get()}' AND password='{entry2.get()}';"
    # query = f"SELECT * FROM `login`.`login` WHERE username='{entry1.get()}''; -- ' AND password='{entry2.get()}';"
    # raveshe avval (be space e akhar deghat konam):  mohammad';-- 
    # raveshe dovvom:  mohammad';#
    # raveshe sevom:  mohammad'#
    mohammad.execute(query)
    # query = "SELECT * FROM `login`.`login` WHERE username=%s AND password=%s;"
    # values = entry1.get(), entry2.get()
    # mohammad.execute(query, values)
    # ' or 1=1#
    information = mohammad.fetchone()
    print(information)
    if information!=None:
        if information[2]==entry2.get():
            messagebox.showinfo("Warning", f"You are close to find passwords 😉\n\
You have searched them in Database😁\n But they are Encrypted😎\nAnd this is not \n\
the message that your teacher wants and would not give you the extra point.")
        else:
            messagebox.showinfo("Success", f"You really hacked the program")
    else:
        messagebox.showerror("Fail", "Wrong Password")


root = Tk()
label1 = Label(root, text="username: ", font=('', 40))
entry1 = Entry(root, font=('', 40))
entry1.insert(0, "mohammad")
label2 = Label(root, text="password: ", font=('', 40))
entry2 = Entry(root, font=('', 40), show="●")
btn_login = Button(root, text="Login", bd=10, font=('', 40), command=login)
label1.grid(row=1, column=1, padx=20, pady=10, sticky='news')
entry1.grid(row=1, column=2, padx=20, pady=10, sticky='news')
label2.grid(row=2, column=1, padx=20, pady=10, sticky='news')
entry2.grid(row=2, column=2, padx=20, pady=10, sticky='news')
btn_login.grid(row=3, column=2, padx=20, pady=10, sticky='nws')
root.mainloop()