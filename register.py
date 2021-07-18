from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image, ImageTk #pip install pillow
import pymysql

class Register:
    def __init__(self,root):
        self.root = root
        self.root.title("Registration Window")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")

        #-----BG Image------------
        self.bg = ImageTk.PhotoImage(file="image/background.jpg")
        bg=Label(self.root, image=self.bg).place(x=250, y=0, relwidth=1, relheight=1)

        #----Left Image------
        self.left = ImageTk.PhotoImage(file="image/front.jpg")
        left = Label(self.root, image = self.left).place(x=80, y=100, width=400, height=500)

        #------Register Frame------
        frame1 = Frame(self.root, bg="white")
        frame1.place(x=480, y=100, width=700, height=500)

        title = Label(frame1, text="REGISTER HERE", font=("time new roman",20,"bold"),bg="white",fg="green").place(x=50, y=30)


        #------------Row 1------------------------------------- 
        self.var_fname = StringVar()   
        f_name = Label(frame1, text="First Name", font=("time new roman",15,"bold"),bg="white",fg="gray").place(x=50, y=100)
        txt_fname = Entry(frame1, font=("Time new roman",15),bg="lightgray", textvariable=self.var_fname).place(x=50, y=130, width=250)

        l_name = Label(frame1, text="Last Name", font=("time new roman",15,"bold"),bg="white",fg="gray").place(x=370, y=100)
        self.txt_lname = Entry(frame1, font=("Time new roman",15),bg="lightgray")
        self.txt_lname.place(x=370, y=130, width=250)
        #----------Row 2---------------------------
        self.var_contact = StringVar()
        contact = Label(frame1, text="Contact No.", font=("time new roman",15,"bold"),bg="white",fg="gray").place(x=50, y=170)
        txt_contact = Entry(frame1, font=("Time new roman",15),bg="lightgray",textvariable=self.var_contact).place(x=50, y=200, width=250)

        self.var_email = StringVar()
        email = Label(frame1, text="Email", font=("time new roman",15,"bold"),bg="white",fg="gray").place(x=370, y=170)
        txt_email = Entry(frame1, font=("Time new roman",15),bg="lightgray",textvariable=self.var_email).place(x=370, y=200, width=250)

        #----------Ro3--------------------------
        self.question = Label(frame1, text="Security Question", font=("time new roman",15,"bold"),bg="white",fg="gray").place(x=50, y=240)
        self.cmb_quest = ttk.Combobox(frame1, font=("Time new roman",13),state='readonly', justify=CENTER)
        self.cmb_quest['values']=("Select","Your First Pet Name", "Your Birth Place","Your Best Friend Name")
        self.cmb_quest.place(x=50, y=280, width=250)
        self.cmb_quest.current(0)

        answer = Label(frame1, text="Answer", font=("time new roman",15,"bold"),bg="white",fg="gray").place(x=370, y=240)
        self.txt_Answer = Entry(frame1, font=("Time new roman",15),bg="lightgray")
        self.txt_Answer.place(x=370, y=280, width=250)

        #--------Row 4-----------------------------
        password = Label(frame1, text="Password", font=("time new roman",15,"bold"),bg="white",fg="gray").place(x=50, y=320)
        self.txt_password = Entry(frame1, font=("Time new roman",15),bg="lightgray", show="*")
        self.txt_password.place(x=50, y=350, width=250)

        cpassword = Label(frame1, text="Confirm Password", font=("time new roman",15,"bold"),bg="white",fg="gray").place(x=370, y=320)
        self.txt_cpassword = Entry(frame1, font=("Time new roman",15),bg="lightgray", show="*")
        self.txt_cpassword.place(x=370, y=350, width=250)

        #------Terms---------------
        self.var_chk = IntVar()
        chk= Checkbutton(frame1, text="I agree The Terms & Conditions",variable=self.var_chk,onvalue=1, offvalue=0, bg="white", font=("time new roman",12)).place(x=50, y=390)

        self.btn_img=ImageTk.PhotoImage(file="image/register.png")
        btn_register = Button(frame1, image=self.btn_img, bd=0, cursor="hand2",command=self.register_data).place(x=50, y=430, width=250, height=45)

        btn_login = Button(self.root, text="Sign In",font=("times new roman",20),command=self.login_window, bd=0, cursor="hand2", bg="green").place(x=200, y=480, width=180)
    def clear(self):
        self.var_fname.delete(0,END)

    def login_window(self):
        self.root.destroy()
        import login


    def register_data(self):
        if self.var_fname.get()=="" or self.var_contact.get()=="" or self.var_email.get()=="" or self.cmb_quest.get()=="Select" or self.txt_Answer.get()=="" or self.txt_password.get()=="" or self.txt_cpassword.get()=="":
            messagebox.showerror("Error","All Fields Are Required", parent=self.root)
        elif self.txt_password.get()!=self.txt_cpassword.get():
            messagebox.showerror("Error","Password & confirm Password should be same", parent=self.root)
        elif self.var_chk.get()==0:
            messagebox.showerror("Error","Please Agree our Terms & conditions", parent=self.root)
        else:
            try:
                con = pymysql.connect(host="localhost",user="root",password="",database="employee2")
                cur = con.cursor()
                cur.execute("Select * from employee where email=%s", self.var_email.get())
                row=cur.fetchone()
                if row != None:
                    messagebox.showerror("Error","User already Exist, Please try with another email", parent=self.root)
                else:
                    cur.execute("insert into employee(f_name, l_name, contact, email, question, answer, password) values(%s,%s,%s,%s,%s,%s,%s)",
                                    (
                                        self.var_fname.get(),
                                        self.txt_lname.get(),
                                        self.var_contact.get(),
                                        self.var_email.get(),
                                        self.cmb_quest.get(),
                                        self.txt_Answer.get(),
                                        self.txt_password.get()
                                    ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success", "Register Successful", parent=self.root)
                    self.root.destroy()
                    import login
                    self.clear()
            except Exception as es:
                messagebox.showerror("Error", f"Error due to:{str(es)}", parent=self.root)



            

        

root = Tk()
obj = Register(root)
root.mainloop()