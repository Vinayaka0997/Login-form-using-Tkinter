from tkinter import *
from PIL import ImageTk
from tkinter import messagebox



class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login System") 
        self.root.geometry("1199x600+100+50")


        self.bg=ImageTk.PhotoImage(file="D:/images/login.jpg.JPG") #background image
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        

        Frame_login=Frame(self.root,bg="white")
        Frame_login.place(x=150,y=150,height=340,width=500)

        title=Label(Frame_login,text="Login Here",font=("Impact",35,"bold"),fg="#d77337",bg="white").place(x=90,y=30)#login here
        desc=Label(Frame_login,text="Student Login Area",font=("Goudy old style",15,"bold"),fg="#d25d17",bg="white").place(x=90,y=100)#student login area

        lbl_user=Label(Frame_login,text="Username",font=("Goudy old style",15,"bold"),fg="gray",bg="white").place(x=90,y=140)#enter username
        self.txt_user=Entry(Frame_login,font=("times new roman",15),bg="lightgray")
        self.txt_user.place(x=90,y=170,width=350,height=35)

        lbl_pass=Label(Frame_login,text="Password",font=("Goudy old style",15,"bold"),fg="gray",bg="white").place(x=90,y=210)#enter password
        self.txt_pass=Entry(Frame_login,font=("times new roman",15),bg="lightgray")
        self.txt_pass.place(x=90,y=240,width=350,height=35)

        forget_btn=Button(Frame_login,text="Forget Password?",cursor="hand2",bg="white",fg="#d77337",bd=0,font=("times new roman",12)).place(x=90,y=280)#forget password
        login_btn=Button(self.root,command=self.login_function,cursor="hand2",text="Login",fg="white",bg="#d77337",font=("times new roman",20)).place(x=300,y=470,width=180,height=40)

        
    def login_function(self):
        if self.txt_pass.get()=="" or self.txt_user.get()=="":  #check login credentials
            messagebox.showerror("Error","All fields are mandatory",parent=self.root)
        elif self.txt_pass.get()!="123456" or self.txt_user.get()!="Vikram Batra":
            messagebox.showerror("Error","Invalid Username/Password",parent=self.root)
        else:
            messagebox.showinfo("Welcome",f"Welcome {self.txt_user.get()}\nYour password is :{self.txt_pass.get()}",parent=self.root)#getting username and password
        


root=Tk()
obj=Login(root)
root.mainloop()
