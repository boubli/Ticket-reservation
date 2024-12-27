from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from dbConnect import DBBConnect
from ListRequist import LisTicket

dBConnect = DBBConnect()

root = Tk()
root.title("Ticket Reservation")
root.geometry("550x570+90+90")
root.configure(background="#2980b9")

# Style
style = ttk.Style()
style.theme_use('classic')
style.configure('TLabel', background="#2980b9", foreground="white", font=('Arial', 12))
style.configure('TButton', background="#3498db", foreground="white", font=('Arial', 12))
style.configure('TRadiobutton', background="#2980b9", foreground="white", font=('Arial', 12))

# Full Name
Label(root, text="Full Name:").grid(row=0, column=0, padx=10, pady=10, sticky=W)
entry_full_name = ttk.Entry(root, width=30, font=('Arial', 14))
entry_full_name.grid(row=0, column=1, columnspan=2, pady=10, sticky=W)

# Gender
Label(root, text="Gender:").grid(row=1, column=0, padx=10, pady=10, sticky=W)
gender_var = StringVar()
ttk.Radiobutton(root, text="Male", variable=gender_var, value="Male").grid(row=1, column=1, sticky=W)
ttk.Radiobutton(root, text="Female", variable=gender_var, value="Female").grid(row=1, column=2, sticky=W)

# Comments
Label(root, text="Comments:").grid(row=2, column=0, padx=10, pady=10, sticky=NW)
text_comments = Text(root, width=40, height=10, font=('Arial', 12))
text_comments.grid(row=2, column=1, columnspan=2, padx=10, pady=10, sticky=W)

# Buttons
btn_save = ttk.Button(root, text="Submit", command=lambda: save_data())
btn_save.grid(row=3, column=1, pady=20, sticky=W)

btn_list = ttk.Button(root, text="List Reservations", command=lambda: list_data())
btn_list.grid(row=3, column=2, pady=20, sticky=W)

# Functions
def save_data():
    if not entry_full_name.get().strip() or not gender_var.get():
        messagebox.showwarning("Input Error", "Please fill in all fields.")
        return

    message = dBConnect.Add(entry_full_name.get().strip(), gender_var.get(), text_comments.get(1.0, 'end').strip())
    messagebox.showinfo("Success", message)
    entry_full_name.delete(0, 'end')
    text_comments.delete(1.0, 'end')

def list_data():
    LisTicket()

root.mainloop()
