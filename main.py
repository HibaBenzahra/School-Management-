import tkinter as tk
from tkinter import ttk, messagebox
import pymysql


#pymysql, mysql.connector, sqlite3

# =========== update status =================#
def update_status(event):
    selection = status_entry.get()

    if selection == "Professor":
        label1.config(text="Departement")
        label1.grid(row=7, column=0, padx=2, pady=10)
        entry1.grid(row=7, column=1, padx=4, pady=4)

        label2.config(text="Element")
        label2.grid(row=8, column=0, padx=2, pady=10)
        entry2.grid(row=8, column=1, padx=4, pady=4)
        
    elif selection == "Student":
        label1.config(text="Filiere")
        label1.grid(row=7, column=0, padx=2, pady=10)
        entry1.grid(row=7, column=1, padx=4, pady=4)

        label2.config(text="Semestre")
        label2.grid(row=8, column=0, padx=2, pady=10)
        entry2.grid(row=8, column=1, padx=4, pady=4)

    else:
        label1.grid_remove()
        label2.grid_remove()
        entry1.grid_remove()
        entry2.grid_remove()

    label1_entry.set("")
    label2_entry.set("")


root = tk.Tk()

# window geometry and head title
root.geometry("1400x800+0+0")
root.title("School Management System")

#whole window bg color
root.config(bg="pink")

#heading title  ADD PADING
title = tk.Label(root, text="ENSAM Management System", font=("Microsoft YaHei", 30, "bold"), border=3, relief=tk.RAISED, bg="pink3" )
title.pack(side=tk.TOP, fill= tk.X)

#data frame
data_frame = tk.LabelFrame(root, text="Enter Data", font=("Microsoft YaHei", 15, "bold"), border=3, relief=tk.RAISED, bg="pink3" )
data_frame.place(x=20,y=110,width=420,height=660)

#student data frame
student_frame = tk.LabelFrame(root, text="Student Data", font=("Microsoft YaHei", 15, "bold"),border=3, relief= tk.RAISED, bg="pink3")
student_frame.place(x=460,y=110,width=920,height=310)

#student data frame
Professor_frame = tk.LabelFrame(root, text="Professor Data", font=("Microsoft YaHei", 15, "bold"),border=3, relief= tk.RAISED, bg="pink3")
Professor_frame.place(x=460,y=460,width=920,height=310)

#=================== variables ==============
cin = tk.StringVar()
name = tk.StringVar()
email = tk.StringVar()
contact = tk.StringVar()
birthday = tk.StringVar()
address = tk.StringVar()
status = tk.StringVar()
label1_entry = tk.StringVar()
label2_entry = tk.StringVar()

searchby = tk.StringVar()
search = tk.StringVar()
searchby2 = tk.StringVar()
search2 = tk.StringVar()

#=================== date frame entry ==================

code = tk.Label(data_frame, text="CIN ", font=("Microsoft YaHei", 12,"bold"), bg="pink3")
code.grid(row=0, column=0, padx=2, pady=10)

code_entry = tk.Entry(data_frame, font=("Microsoft YaHei", 12), bg="white", textvariable=cin)
code_entry.grid(row=0, column=1, padx=4, pady=4)

namec = tk.Label(data_frame, text="Full Name ", font=("Microsoft YaHei", 12,"bold"), bg="pink3")
namec.grid(row=1, column=0, padx=2, pady=10)

name_entry = tk.Entry(data_frame, font=("Microsoft YaHei", 12), bg="white", textvariable=name)
name_entry.grid(row=1, column=1, padx=4, pady=4)

emailc = tk.Label(data_frame, text="Email ", font=("Microsoft YaHei", 12,"bold"), bg="pink3")
emailc.grid(row=2, column=0, padx=2, pady=10)

email_entry = tk.Entry(data_frame, font=("Microsoft YaHei", 12), bg="white", textvariable=email)
email_entry.grid(row=2, column=1, padx=4, pady=4)

phone = tk.Label(data_frame, text="Contact ", font=("Microsoft YaHei", 12,"bold"), bg="pink3")
phone.grid(row=3, column=0, padx=2, pady=10)

phone_entry = tk.Entry(data_frame, font=("Microsoft YaHei", 12), bg="white", textvariable=contact)
phone_entry.grid(row=3, column=1, padx=4, pady=4)

birthdayc = tk.Label(data_frame, text="Birthday ", font=("Microsoft YaHei", 12,"bold"), bg="pink3")
birthdayc.grid(row=4, column=0, padx=2, pady=10)

birthday_entry = tk.Entry(data_frame, font=("Microsoft YaHei", 12), bg="white", textvariable=birthday)
birthday_entry.grid(row=4, column=1, padx=4, pady=4)

addressc = tk.Label(data_frame, text="Address ", font=("Microsoft YaHei", 12,"bold"), bg="pink3")
addressc.grid(row=5, column=0, padx=2, pady=10)

address_entry = tk.Entry(data_frame, font=("Microsoft YaHei", 12), bg="white", textvariable=address)
address_entry.grid(row=5, column=1, padx=4, pady=4)

statusc = tk.Label(data_frame, text="Status ", font=("Microsoft YaHei", 12,"bold"), bg="pink3")
statusc.grid(row=6, column=0, padx=2, pady=10)

status_entry = ttk.Combobox(data_frame, font=("Microsoft YaHei", 11), state="readonly", textvariable=status)
status_entry["values"]= ("", "Professor", "Student")
status_entry.grid(row=6, column=1, padx=4, pady=4)
status_entry.bind("<<ComboboxSelected>>", update_status)

label1 = ttk.Label(data_frame, text="", font=("Microsoft YaHei", 12,"bold"), background="pink3")
label2 = ttk.Label(data_frame, text="", font=("Microsoft YaHei", 12,"bold"), background="pink3")

# Entries with StringVars for dynamic content
entry1 = ttk.Entry(data_frame, font=("Microsoft YaHei", 12), textvariable=label1_entry)
entry2 = ttk.Entry(data_frame, font=("Microsoft YaHei", 12), textvariable=label2_entry)

# Initially hide labels and entries
label1.grid_remove()
label2.grid_remove()
entry1.grid_remove()
entry2.grid_remove()

#============= Functions ======================#

def fetch_student_data():
    conn = pymysql.connect(host="localhost", user="root", password="", database="sms1")
    curr = conn.cursor()
    curr.execute("SELECT * FROM student_data")
    rows = curr.fetchall()
    if len(rows)!=0:
        student_table.delete(*student_table.get_children())
        for row in rows:
            student_table.insert("", tk.END, values=row)
        conn.commit()
    conn.close()

def fetch_professor_data():
    conn = pymysql.connect(host="localhost", user="root", password="", database="sms2")
    curr = conn.cursor()
    curr.execute("SELECT * FROM professor_data")
    rows = curr.fetchall()
    if len(rows)!=0:
        professor_table.delete(*professor_table.get_children())
        for row in rows:
            professor_table.insert("", tk.END, values=row)
        conn.commit()
    conn.close()

def add_func():
    '''this function will add the user data to the data base and display it'''
    if cin.get() == "" or name.get() == "" or status.get() == "":
        messagebox.showerror("Error", "Please fill the fields!")
    elif status.get() == "Student":
        conn = pymysql.connect(host="localhost", user="root", password="", database="sms1")
        curr = conn.cursor()
        curr.execute("INSERT INTO student_data VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)", (cin.get(), name.get(), email.get(), contact.get(), birthday.get(), address.get(), status.get(), label1_entry.get(), label2_entry.get()))
        conn.commit()
        conn.close()

        fetch_student_data()
    else:
        conn = pymysql.connect(host="localhost", user="root", password="", database="sms2")
        curr = conn.cursor()
        curr.execute("INSERT INTO professor_data VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)", (cin.get(), name.get(), email.get(), contact.get(), birthday.get(), address.get(), status.get(), label1_entry.get(), label2_entry.get()))
        conn.commit()
        conn.close()  
        
        fetch_professor_data()

def show_selected_student(event):
    '''Fonction qui permet d'afficher les données de la ligne sélectionnée du table des étudiants'''
    cursor_row = student_table.focus()
    content = student_table.item(cursor_row)
    row = content['values']
    cin.set(row[0])
    name.set(row[1])
    email.set(row[2])
    contact.set(row[3])
    birthday.set(row[4])
    address.set(row[5])
    status.set(row[6])
    label1_entry.set(row[7])
    label2_entry.set(row[8])

def show_selected_professor(event):
    '''Fonction qui permet d'afficher les données de la ligne sélectionnée de la table des professeurs'''
    cursor_row = professor_table.focus()
    content = professor_table.item(cursor_row)
    row = content['values']
    cin.set(row[0])
    name.set(row[1])
    email.set(row[2])
    contact.set(row[3])
    birthday.set(row[4])
    address.set(row[5])
    status.set(row[6])
    label1_entry.set(row[7])
    label2_entry.set(row[8])

def clear_funct():
    '''this function will clear the entries'''
    cin.set("")
    name.set("")
    email.set("")
    contact.set("")
    birthday.set("")
    address.set("")
    status.set("")
    label1_entry.set("")
    label2_entry.set("")
    search.set("")
    searchby.set("")
    search2.set("")
    searchby2.set("")


def update_func():
    '''this function will add the user data to the data base and display it'''
    if cin.get() == "" or name.get() == "" or status.get() == "":
        messagebox.showerror("Error", "Please fill the fields!")
    elif status.get() == "Student":
        conn = pymysql.connect(host="localhost", user="root", password="", database="sms1")
        curr = conn.cursor()
        curr.execute("UPDATE student_data SET name = %s, email = %s, contact = %s, birthday = %s, address = %s, status = %s, label1_entry = %s, label2_entry = %s where cin=%s", (name.get(), email.get(), contact.get(), birthday.get(), address.get(), status.get(), label1_entry.get(), label2_entry.get(), cin.get()))
        conn.commit()
        conn.close()
        fetch_student_data()
        clear_funct()
    else:
        conn = pymysql.connect(host="localhost", user="root", password="", database="sms2")
        curr = conn.cursor()
        curr.execute("UPDATE professor_data SET name = %s, email = %s, contact = %s, birthday = %s, address = %s, status = %s, label1_entry = %s, label2_entry = %s where cin=%s", (name.get(), email.get(), contact.get(), birthday.get(), address.get(), status.get(), label1_entry.get(), label2_entry.get(), cin.get()))
        conn.commit()
        conn.close()      
        fetch_professor_data()
        clear_funct()

def delete_func():
    """fonction supprimer un enregistrement dans la base de données en fonction de la valeur de CIN"""
    if cin.get() == "" or name.get() == "" or status.get() == "":
        messagebox.showerror("Error", "Please fill the fields!")
    elif status.get() == "Student":
        conn = pymysql.connect(host="localhost", user="root", password="", database="sms1")
        curr = conn.cursor()
        curr.execute("DELETE FROM student_data WHERE cin = %s", cin.get())
        conn.commit()   #enregistre les changements dans la base de données
        conn.close()   #termine la connexion avec la base de données
        fetch_student_data()
        clear_funct()
    else:
        conn = pymysql.connect(host="localhost", user="root", password="", database="sms2")
        curr = conn.cursor()
        curr.execute("DELETE FROM professor_data WHERE cin = %s", cin.get())
        conn.commit()
        conn.close()      
        fetch_professor_data()
        clear_funct()

def search_func_student():
    '''this function will display data depending on type and value of student data typed in the search entry'''
    if search.get() == "" or searchby.get() == "":
        messagebox.showerror("Error", "Please fill the search fields!")
    else:
        conn = pymysql.connect(host="localhost", user="root", password="", database="sms1")
        curr = conn.cursor()
        curr.execute(f"SELECT * FROM student_data WHERE {searchby.get()} = %s", (search.get(),))
        rows = curr.fetchall()
        if len(rows)!=0:
            student_table.delete(*student_table.get_children())
            for row in rows:
                student_table.insert("", tk.END, values=row)
            conn.commit()
        conn.close()

        if curr.rowcount <= 0:
            messagebox.showwarning("Error", "Not found")


def search_func_professor():
    '''this function will display data depending on type and value of professor data typed in the search entry'''
    if search2.get() == "" or searchby2.get() == "":
        messagebox.showerror("Error", "Please fill the search fields!")
    else:
        conn = pymysql.connect(host="localhost", user="root", password="", database="sms2")
        curr = conn.cursor()
        curr.execute(f"SELECT * FROM professor_data WHERE {searchby2.get()} = %s", (search2.get(),))
        rows = curr.fetchall()
        if len(rows)!=0:
            professor_table.delete(*professor_table.get_children())
            for row in rows:
                professor_table.insert("", tk.END, values=row)
            conn.commit()
        conn.close()

        if curr.rowcount <= 0:
            messagebox.showwarning("Error", "Not found")


#========== Buttons in Data Frame =========#

btn_frame = tk.Frame(data_frame, bg="pink3")
btn_frame.place(x=15,y=500,width=380,height=100)

add_btn = tk.Button(btn_frame, bg="white", text="Add", bd=3, font=("Microsoft YaHei", 12, "bold"), width=13,relief=tk.GROOVE, command=add_func)
add_btn.grid(row=0, column=0, padx=8, pady=1)

update_btn = tk.Button(btn_frame, bg="white", text="Update", bd=3, font=("Microsoft YaHei", 12, "bold"), width=13,relief=tk.GROOVE, command=update_func)
update_btn.grid(row=0, column=1, padx=8, pady=1)

clear_btn = tk.Button(btn_frame, bg="white", text="Clear", bd=3, font=("Microsoft YaHei", 12, "bold"), width=13,relief=tk.GROOVE, command=clear_funct)
clear_btn.grid(row=1, column=0, padx=8, pady=1)


delete_btn = tk.Button(btn_frame, bg="white", text="Delete", bd=3, font=("Microsoft YaHei", 12, "bold"), width=13,relief=tk.GROOVE, command=delete_func)
delete_btn.grid(row=1, column=1, padx=8, pady=1)


# ==================== Search bar in student data frame =========================

search_frame = tk.Frame(student_frame, bg="pink3")
search_frame.place(x=20,y=0,width=870,height=50)

searchby01 = tk.Label(search_frame, text="Search By ", font=("Microsoft YaHei", 12,"bold"), bg="pink3")
searchby01.grid(row=0, column=0, padx=8, pady=0)

search_entry = ttk.Combobox(search_frame, font=("Microsoft YaHei", 11), state="readonly", textvariable=searchby)
search_entry["values"]= ("cin", "name", "email", "contact", "birthday", "address", "label1_entry", "label2_entry")
search_entry.grid(row=0, column=1, padx=4, pady=0)

searchbar_entry = tk.Entry(search_frame, font=("Microsoft YaHei", 12), bg="white", textvariable=search )
searchbar_entry.grid(row=0, column=2, padx=10, pady=0)

search_btn = tk.Button(search_frame, bg="white", text="Search", bd=3, font=("Microsoft YaHei", 8, "bold"), width=8,relief=tk.GROOVE, command=search_func_student)
search_btn.grid(row=0, column=3, padx=10, pady=0)


showall_btn = tk.Button(search_frame, bg="white", text="Show All", bd=3, font=("Microsoft YaHei", 8, "bold"), width=8,relief=tk.GROOVE, command= fetch_student_data)
showall_btn.grid(row=0, column=4, padx=10, pady=0)

#======================== Student  Data Frame ============================
student_data_frame = tk.Label(student_frame, bg="white")
student_data_frame.place(x=20,y=50,width=870, height=205)

#-----to be able to scroll---
y_scroll = tk.Scrollbar(student_data_frame, orient=tk.VERTICAL)
y_scroll.pack(side=tk.RIGHT, fill=tk.Y)
x_scroll = tk.Scrollbar(student_data_frame, orient=tk.HORIZONTAL)
x_scroll.pack(side=tk.BOTTOM, fill=tk.X)

#-----student table---
student_table= ttk.Treeview(student_data_frame, columns=("CIN", "Full Name", "Email", "Contact", "Birthday", "Address", "Status", "Filiere", "Semestre"), yscrollcommand=y_scroll.set, xscrollcommand=x_scroll.set)
student_table.pack(side=tk.TOP, fill=tk.X)


y_scroll.config(command=student_table.yview)
x_scroll.config(command=student_table.xview)

student_table.heading("CIN", text="CIN")
student_table.heading("Full Name", text="Full Name")
student_table.heading("Email", text="Email")
student_table.heading("Contact", text="Contact")
student_table.heading("Birthday", text="Birthday")
student_table.heading("Address", text="Address")
student_table.heading("Status", text="Status")
student_table.heading("Filiere", text="Filiere")
student_table.heading("Semestre", text="Semestre")

student_table["show"] = "headings"

student_table.column("CIN", width=100)
student_table.column("Full Name", width=140)
student_table.column("Email", width=200)
student_table.column("Contact", width=140)
student_table.column("Birthday", width=100)
student_table.column("Address", width=100)
student_table.column("Status", width=100)
student_table.column("Filiere", width=100)
student_table.column("Semestre", width=100)

# ==================== Search bar in Professor data frame =========================

search_frame2 = tk.Frame(Professor_frame, bg="pink3")
search_frame2.place(x=20,y=0,width=870,height=50)

searchby02 = tk.Label(search_frame2, text="Search By ", font=("Microsoft YaHei", 12,"bold"), bg="pink3")
searchby02.grid(row=0, column=0, padx=8, pady=0)

search_entry2 = ttk.Combobox(search_frame2, font=("Microsoft YaHei", 11), state="readonly", textvariable=searchby2)
search_entry2["values"]= ("cin", "name", "email", "contact", "birthday", "address", "label1_entry", "label2_entry")
search_entry2.grid(row=0, column=1, padx=4, pady=0)

searchbar_entry2 = tk.Entry(search_frame2, font=("Microsoft YaHei", 12), bg="white", textvariable=search2 )
searchbar_entry2.grid(row=0, column=2, padx=10, pady=0)

search_btn2 = tk.Button(search_frame2, bg="white", text="Search", bd=3, font=("Microsoft YaHei", 8, "bold"), width=8,relief=tk.GROOVE, command=search_func_professor)
search_btn2.grid(row=0, column=3, padx=10, pady=0)


showall_btn2 = tk.Button(search_frame2, bg="white", text="Show All", bd=3, font=("Microsoft YaHei", 8, "bold"), width=8,relief=tk.GROOVE, command=fetch_professor_data)
showall_btn2.grid(row=0, column=4, padx=10, pady=0)

#======================== Professor  Data Frame ============================
professor_data_frame = tk.Label(Professor_frame, bg="white")
professor_data_frame.place(x=20,y=50,width=870, height=205)

#-----to be able to scroll---
y_scroll = tk.Scrollbar(professor_data_frame, orient=tk.VERTICAL)
y_scroll.pack(side=tk.RIGHT, fill=tk.Y)
x_scroll = tk.Scrollbar(professor_data_frame, orient=tk.HORIZONTAL)
x_scroll.pack(side=tk.BOTTOM, fill=tk.X)

#-----student table---
professor_table= ttk.Treeview(professor_data_frame, columns=("CIN", "Full Name", "Email", "Contact", "Birthday", "Address", "Status", "Departement", "Element"), yscrollcommand=y_scroll.set, xscrollcommand=x_scroll.set)
professor_table.pack(side=tk.TOP, fill=tk.X)


y_scroll.config(command=professor_table.yview)
x_scroll.config(command=professor_table.xview)

professor_table.heading("CIN", text="CIN")
professor_table.heading("Full Name", text="Full Name")
professor_table.heading("Email", text="Email")
professor_table.heading("Contact", text="Contact")
professor_table.heading("Birthday", text="Birthday")
professor_table.heading("Address", text="Address")
professor_table.heading("Status", text="Status")
professor_table.heading("Departement", text="Departement")
professor_table.heading("Element", text="Element")

professor_table["show"] = "headings"


professor_table.column("CIN", width=100)
professor_table.column("Full Name", width=140)
professor_table.column("Email", width=200)
professor_table.column("Contact", width=140)
professor_table.column("Birthday", width=100)
professor_table.column("Address", width=100)
professor_table.column("Status", width=100)
professor_table.column("Departement", width=100)
professor_table.column("Element", width=100)

fetch_student_data()
fetch_professor_data()

student_table.bind("<ButtonRelease-1>", show_selected_student)
professor_table.bind("<ButtonRelease-1>", show_selected_professor)


root.mainloop()


