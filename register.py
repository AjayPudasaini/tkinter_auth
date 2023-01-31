import tkinter as tk
import db as database
from login import login_form

global base
base=tk.Tk()
base.title('Register')
width= base.winfo_screenwidth()
height= base.winfo_screenheight()

base.geometry("%dx%d" % (width, height))

def register_user():
    registred = False
    username = user_name_input_area.get()
    fullname = full_name_input_area.get()
    email = email_input_area.get()
    password = password_input_area.get()

    # database.cursor.execute("SELECT COUNT(*) from users WHERE username = '"+username+"' ")
    # result = database.cursor.fetchall()
    if registred == False:
        database.cursor.execute("INSERT INTO users(username, email, full_name, password)VALUES(?,?,?,?)",(username,email,fullname,password))
        database.db.commit()
        registred = True
    
    if registred == True:
        error_message["text"] = f"User: {username} registred success"
        base.destroy()
        a = login_form(base, tk)
        tk.Toplevel(a)
    else:
        error_message["text"] = f"Register failed"





labl_0 = tk.Label(base, text="Register New User",width=50,font=("bold", 30)).place(x=300,y=60)  

user_name = tk.Label(base, text = "Username", width=50,font=("bold", 15)).place(x = 300, y = 150)
user_name_input_area = tk.Entry(base, text="", width = 50)
user_name_input_area.place(x = 750,y = 150)

full_name = tk.Label(base, text = "Full Name", width=50,font=("bold", 15)).place(x = 300, y = 200)
full_name_input_area = tk.Entry(base, text="", width = 50)
full_name_input_area.place(x = 750,y = 200)

email = tk.Label(base, text = "Email", width=50,font=("bold", 15)).place(x = 300, y = 250)
email_input_area = tk.Entry(base, text="", width = 50)
email_input_area.place(x = 750,y = 250)

password = tk.Label(base, text = "Password", width=50,font=("bold", 15)).place(x = 300, y = 300)
password_input_area = tk.Entry(base, text="", width = 50)
password_input_area.place(x = 750,y = 300)


error_message = tk.Message(text="", width=100, fg="red")
error_message.place(x=700,y=350)

submit_button = tk.Button(base,text = "Register", command=register_user, font=("bold", 18), width=10, height=1).place(x = 800, y = 400)

already_acc = tk.Label(base, text="Already have account?", width=50,fg='blue', font=("bold", 12, 'underline')).place(x=635,y=450)  


base.mainloop()
