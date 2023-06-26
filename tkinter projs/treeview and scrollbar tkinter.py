from tkinter import ttk
import tkinter as tk
root = tk.Tk()
treev = ttk.Treeview(root, selectmode ='browse')
treev.grid(row=1, column=1)
verscrlbar = ttk.Scrollbar(root,orient ="vertical",command = treev.yview)
verscrlbar.grid(row=1, column=2, sticky='news')
treev.configure(yscrollcommand = verscrlbar.set)
treev["columns"] = ("1", "2", "3")
treev['show'] = 'headings'
treev.column("1", width = 200, anchor ='c')
treev.column("2", width = 150, anchor ='c')
treev.column("3", width = 60, anchor ='c')
treev.heading("1", text ="Name")
treev.heading("2", text ="Surname")
treev.heading("3", text ="Age")
for i in range(50):
    treev.insert("", 'end', text =i, values =(f"MyName {i}", f"Surname {i}", i))
root.mainloop()