from tkinter import *
from tkinter import messagebox
import pymysql

def enc_password(password):
    new_pass=""
    # for i in range(len(password)):
    #     new_pass+=chr(ord(password[i])+i+1)
    for i, char in enumerate(password):
        if chr(ord(char)+i+1) not in ["'", "\"", "\\","`", "-", "#", "$"]:
            new_pass+=chr(ord(char)+i+1)
        else:
            new_pass+=char
    return new_pass

connection = pymysql.connect(host='127.0.0.1', user='root', password='root')
mohammad = connection.cursor()
queries = [
    "DROP SCHEMA IF EXISTS `login`;",
    "CREATE SCHEMA IF NOT EXISTS `login`;",
    "CREATE TABLE IF NOT EXISTS `login`.`login` (`id` INT NOT NULL AUTO_INCREMENT, `username` VARCHAR(45) NOT NULL, `password` VARCHAR(45) NOT NULL, PRIMARY KEY (`id`), UNIQUE INDEX `username_UNIQUE` (`username` ASC) VISIBLE);",
    f"INSERT IGNORE INTO `login`.`login` (`username`, `password`) VALUES ('mohammad', '{enc_password('salam dadach khoobi :D')}');",
    f"INSERT IGNORE INTO `login`.`login` (`username`, `password`) VALUES ('ali', '{enc_password('omran befahmi chie :D')}');",
    f"INSERT IGNORE INTO `login`.`login` (`username`, `password`) VALUES ('benyamin', '{enc_password('i love python :D')}');",
]

for query in queries:
    mohammad.execute(query)
connection.commit()

def login():
    query = f"SELECT * FROM `login`.`login` WHERE username='{entry1.get()}' AND BINARY password='{enc_password(entry2.get())}';"
    # raveshe avval (be space e akhar deghat konam):  mohammad';-- 
    # raveshe dovvom:  mohammad';#
    # raveshe sevom:  mohammad'#
    # raveshe chaharom bedoone username: ' or 1=1#
    mohammad.execute(query)
    # query = "SELECT * FROM `login`.`login` WHERE username=%s AND BINARY password=%s;"
    # values = entry1.get(), enc_password(entry2.get())
    # mohammad.execute(query, values)
    information = mohammad.fetchone()
    print(information)
    if information!=None:
        messagebox.showinfo("Success", f"You really are a hacker :D")
    else:
        messagebox.showerror("Fail", "Wrong Password")


root = Tk()
label1 = Label(root, text="username: ", font=('', 40))
entry1 = Entry(root, font=('', 40))
entry1.insert(0, "mohammad")
label2 = Label(root, text="password: ", font=('', 40))
entry2 = Entry(root, font=('', 40))
btn_login = Button(root, text="Login", bd=10, font=('', 40), command=login)
label1.grid(row=1, column=1, padx=20, pady=10, sticky='news')
entry1.grid(row=1, column=2, padx=20, pady=10, sticky='news')
label2.grid(row=2, column=1, padx=20, pady=10, sticky='news')
entry2.grid(row=2, column=2, padx=20, pady=10, sticky='news')
btn_login.grid(row=3, column=2, padx=20, pady=10, sticky='nws')
root.mainloop()
