from tkinter import *
from tkinter import messagebox
import requests
import webview # pip install pywebview
import io
from PIL import Image, ImageTk
from urllib.request import urlopen

def start_movie(url, name="Sample"):
    webview.create_window(name, url)
    webview.start()

def find():
    tag = entry_tag.get().strip()
    tag=tag.replace("-", "")
    tag=tag.replace(" ", "")
    if len(tag)<3:
        messagebox.showwarning("Warning", "Please Insert three characters at least.")
        return
    data = requests.get(f"https://www.aparat.com/etc/api/videobytag/text/{tag}")
    data = data.json().get('videobytag')
    if data == None:
        messagebox.showwarning("Warning", "No Item found.")
        return
    links = []
    tk_imgs = []
    for item in data:
        links.append(item.get('frame'))
        # pic_url = "http://www.google.com/intl/en/images/logo.gif"
        pic_url = item.get('small_poster')
        my_page = urlopen(pic_url)
        my_picture = io.BytesIO(my_page.read())
        pil_img = Image.open(my_picture)
        pil_img = pil_img.resize((200, 80))
        tk_img = ImageTk.PhotoImage(pil_img)
        tk_imgs.append(tk_img)
    for i in range(20):
        btns[i].config(image=tk_imgs[i], command=lambda i=i: start_movie(links[i]))
        btns[i].config()
        btns[i].grid(row=i//5, column=i%5, padx=5, pady=5)
    mainloop()


root=Tk()
frame1 = LabelFrame(root, text='Search')
frame1.pack(padx=10, pady=5)
frame2 = LabelFrame(root, text='Result')
frame2.pack(padx=10, pady=5)
lbl_tag = Label(frame1,text="tag: ")
lbl_tag.grid(row=1, column=1, padx=10, pady=5)
entry_tag = Entry(frame1)
entry_tag.grid(row=1, column=2, padx=10, pady=5)
btn = Button(frame1,text="Serach", command=lambda:find())
btn.grid(row=1, column=3, padx=10, pady=5)
btns = []

for i in range(20):
    btns.append(Button(frame2))

root.mainloop()