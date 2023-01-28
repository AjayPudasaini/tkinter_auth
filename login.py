import tkinter as tk
base=tk.Tk()
base.title('Login')
width= base.winfo_screenwidth()
height= base.winfo_screenheight()

base.geometry("%dx%d" % (width, height))

labl_0 = tk.Label(base, text="Login",width=50,font=("bold", 30)).place(x=300,y=60)  

user_name = tk.Label(base, text = "Username", width=50,font=("bold", 15)).place(x = 300, y = 150)
user_name_input_area = tk.Entry(base, width = 50).place(x = 750,y = 150) 

password = tk.Label(base, text = "Password", width=50,font=("bold", 15)).place(x = 300, y = 200)
password_input_area = tk.Entry(base, width = 50).place(x = 750,y = 200) 


submit_button = tk.Button(base,text = "Login", font=("bold", 18), width=10, height=1).place(x = 800, y = 250)

already_acc = tk.Label(base, text="Don't have account?",width=50,fg="blue" font=("bold", 12, 'underline')).place(x=635,y=300)  


base.mainloop()
