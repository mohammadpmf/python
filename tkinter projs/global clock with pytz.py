from datetime import datetime
import pytz
from tkinter import *
import threading
from time import sleep

class MyTime():
    def __init__(self, h=0, m=0, s=0, ms=0):
        self.h=h
        self.m=m
        self.s=s
        self.ms=ms
    def __str__(self):
        return f"{self.h:02}:{self.m:02}:{self.s:02}.{self.ms:02}"    
    def count(self):
        self.ms += 1
        sleep(0.01)
        if self.ms == 100:
            self.ms = 0
            self.s += 1
            if self.s == 60:
                self.s = 0
                self.m += 1
                if self.m == 60:
                    self.m = 0
                    self.h += 1
                    if self.h == 24:
                        self.h = 0

def count(country: MyTime, sv: StringVar):
    while True:
        country.count()
        sv.set(country)

iran = datetime.now(pytz.timezone('Iran'))
new_york = datetime.now(pytz.timezone('US/Eastern'))
Johannesburg = datetime.now(pytz.timezone('Africa/Johannesburg'))
iran_time = MyTime(iran.hour, iran.minute, iran.second)
US_time = MyTime(new_york.hour, new_york.minute, new_york.second)
South_Aferica_time = MyTime(Johannesburg.hour, Johannesburg.minute, Johannesburg.second)
root = Tk()
Label(root, text='Iran Time: ').grid(row=1, column=1)
Label(root, text='US Time: ').grid(row=2, column=1)
Label(root, text='South Aferica Time: ').grid(row=3, column=1)
ir = StringVar()
us = StringVar()
sa = StringVar()
Label(root, textvariable=ir).grid(row=1, column=2)
Label(root, textvariable=us).grid(row=2, column=2)
Label(root, textvariable=sa).grid(row=3, column=2)
threading.Thread(target=count, args=(iran_time, ir), daemon=True).start()
threading.Thread(target=count, args=(US_time, us), daemon=True).start()
threading.Thread(target=count, args=(South_Aferica_time, sa), daemon=True).start()

root.mainloop()