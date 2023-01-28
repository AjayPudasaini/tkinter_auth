import tkinter as tk
import sqlite3

base=tk.Tk()
base.title('Register')
width= base.winfo_screenwidth()
height= base.winfo_screenheight()

base.geometry("%dx%d" % (width, height))

labl_0 = tk.Label(base, text="Register New User",width=50,font=("bold", 30)).place(x=300,y=60)  

user_name = tk.Label(base, text = "Username", width=50,font=("bold", 15)).place(x = 300, y = 150)
user_name_input_area = tk.Entry(base, width = 50).place(x = 750,y = 150) 

full_name = tk.Label(base, text = "Full Name", width=50,font=("bold", 15)).place(x = 300, y = 200)
full_name_input_area = tk.Entry(base, width = 50).place(x = 750,y = 200) 

email = tk.Label(base, text = "Email", width=50,font=("bold", 15)).place(x = 300, y = 250)
email_input_area = tk.Entry(base, width = 50).place(x = 750,y = 250) 

password = tk.Label(base, text = "Password", width=50,font=("bold", 15)).place(x = 300, y = 300)
password_input_area = tk.Entry(base, width = 50).place(x = 750,y = 300) 


submit_button = tk.Button(base,text = "Register", font=("bold", 18), width=10, height=1).place(x = 800, y = 400)

already_acc = tk.Label(base, text="Already have account?",width=50,fg='blue', font=("bold", 12, 'underline')).place(x=635,y=450)  


base.mainloop()
