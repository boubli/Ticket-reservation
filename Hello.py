from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from dbConnect import DBBConnect
from ListRequist import LisTicket

dBConnect=DBBConnect()

root = Tk()
root.title("Ticket reservation")
root.geometry("550x570+90+90")
root.configure(background="#2980b9")

#style
style = ttk.Style()
style.theme_use('classic')
style.configure('TLabel', background="#2980b9")
style.configure('TButton', background="#2980b9")
style.configure('TRadiobutton', background="#2980b9")

#full Name
ttk.Label(root, text="Full Name:").grid(row=0, column=0, padx=0, pady=0)
EntryFullName = ttk.Entry(root, width=30, font=('Arial', 16))
EntryFullName.grid(row=0, column=1, columnspan=2, pady=10)


#gender
ttk.Label(root, text="Gender:").grid(row=3, column=0, pady=10 )
SpanGender = StringVar()
ttk.Radiobutton(root, text="Male", variable=SpanGender, value="Male").grid(row=3, column=1)
ttk.Radiobutton(root, text="Femle", variable=SpanGender, value="Female").grid(row=3, column=2)

# comments
ttk.Label(root, text="Comments:").grid(row=4, column=0, pady=10 )
xtComments = Text(root, width=30, height=15, font=('Arial, 16'))
xtComments.grid(row=4, column=1, columnspan=2, padx=30)

#buttons
buSave = ttk.Button(root, text="Submit")
buSave.grid(row=5, column=1, pady=10)
BuList = ttk.Button(root, text="list Res.")
BuList.grid(row=5, column=2)


def BusaveData():
    msg = dBConnect.Add(EntryFullName.get(),SpanGender.get(),xtComments.get(1.0, 'end'))
    messagebox.showinfo(title="Add Info", message=msg)
    EntryFullName.delete(0, 'end')
    xtComments.delete(1.0, 'end')


def BulistData():
    #TODO:Show orders
    ListRequest=LisTicket()


buSave.config(command=BusaveData)
BuList.config(command=BulistData)

root.mainloop()
