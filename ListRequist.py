from tkinter import *
from tkinter import ttk
from dbConnect import DBBConnect

dBConnect = DBBConnect()

class LisTicket:

    def __init__(self):
        self._root = Toplevel()
        self._root.title("Reservation List")
        self._root.geometry("600x400")

        # Treeview
        tv = ttk.Treeview(self._root, columns=("#Name", "#Gender", "#Comment"), show='headings')
        tv.heading("#Name", text="Name")
        tv.heading("#Gender", text="Gender")
        tv.heading("#Comment", text="Comment")
        tv.column("#Name", width=150)
        tv.column("#Gender", width=100)
        tv.column("#Comment", width=300)
        tv.pack(fill=BOTH, expand=True)

        # Fetch data
        cursor = dBConnect.ListRequest()
        for row in cursor:
            tv.insert('', 'end', values=(row['Name'], row['Gender'], row['Comment']))
