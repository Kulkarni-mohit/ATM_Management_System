from tkinter import * 
from tkinter.ttk import * 
import sqlite3 as sql 
import tkinter.messagebox as tmsg 
from PIL import Image,ImageTk 
from datetime import datetime 
import random 
import smtplib 
from email.message import EmailMessage 


def tab1(): 
    global uv 
    global pv
    
    root=Tk() 
    root.geometry("640x440+250+100") 
    root.title("ATM SYSTEM") 
    p1=PhotoImage(file='data\Capture.png') 
    root.iconphoto(False,p1) 
    b=ImageTk.PhotoImage(file='data\image.jpg') 
    bgj=Label(root,image=b).place(x=0,y=0,relwidth=1,relheight=1)
    
    frame1=Frame(root) 
    frame1.place(x=20,y=20,width=600,height=400)
    
    a=Label(frame1,text=" Welcome To ATM Services ",background='light grey',foreground='green',font='comisansns 30 bold',borderwidth=5,relief=RIDGE) 
    a.place(x=40, y=10)
    
    user=Label(frame1,text="User ID:",background='white',foreground='blue',font='comisansns 15 bold') 
    password=Label(frame1,text="Password:",background='white',foreground='blue',font='comisansns 15 bold') 
    user.place(x=150, y=100) 
    password.place(x=150, y=150)
    
    uv=StringVar() 
    pv=StringVar() 
    ue=Entry(frame1,textvariable=uv,font=("times new roman",15)) 
    pe=Entry(frame1,textvariable=pv,font=("times new roman",15), show='*') 
    ue.place(x=300, y=100, height=25, width=150) 
    pe.place(x=300, y=150, height=25, width=150)
    
    Button(frame1,text="Login",command=connection1).place(x=300, y=200, height=40, width=100) 
    Button(frame1,text="Register",command=register).place(x=450, y=300, height=40, width=100)
    
    x=Label(frame1,text="Developed By Mohit Kulkarni",background='lavenderblush2',foreground='black',font='comisansns 10').place(x=420, y=380) 
    Label(frame1,text="New To The Bank? Please First Register:", background='lavenderblush2',foreground='red',font='comisansns 15').place(x=50, y=305)
    
    root.mainloop() 

 
def connection1(): 
    global a 
 
    #conn=mysql.connector.connect(host='localhost',user='root',passwd='user@12#')

    conn = sql.connect("data\dbms.sqlite")
    
    #m=conn.cursor()
    #conn.execute('use atm')
    
    a = conn.execute("select * from userinfo;")
    a=a.fetchall()
    
    conn.close()
    
    verify()

    
def verify(): 
    global a 
    global pv 
    global uv 
    global s

    ide=uv.get() 
    iii=pv.get()
    
    q=[] 
    p=[] 
    s=[]
    
    for i in range(0,len(a)):
        z1=a[i] 
        q.append(z1[2]) 
        p.append(z1[3]) 
        if (z1[2])==ide: 
            s=z1 
            i+=1 
        if ide not in q: 
            tmsg.showerror("Error","Invalid UserID")
            
    for i in q: 
        if i==ide: 
            x=q.index(i) 
            ii=int(iii) 
            if p[x]==ii: 
                tab2() 
            else: 
                tmsg.showerror("Error","Invalid Password")

                
def register(): 
    global uu 
    global us 
    global ug 
    global ur 
    global uz 
 
    root=Toplevel() 
    root.geometry("640x480+300+150") 
    root.title("ATM SYSTEM") 
    b=ImageTk.PhotoImage(file='data\image.jpg') 
    bgj=Label(root,image=b).place(x=0,y=0,relwidth=1,relheight=1)
    
    frame1=Frame(root) 
    frame1.place(x=20,y=20,width=600,height=440)
    
    a=Label(frame1,text=" Welcome To ATM Services ",background='light grey',foreground='green',font='comisansns 30 bold',borderwidth=5,relief=RIDGE) 
    a.place(x=40, y=10)
    
    Label(frame1,text="Registrationpage",background='lavenderblush2',foreground='orange',font='comisansns 20 bold').place(x=200, y=75) 
    user=Label(frame1,text="Enter Name(In Capital):",background='white',foreground='blue',font='comisansns 15').place(x=80, y=120) 
    ID=Label(frame1,text="User ID :",background='white',foreground='blue',font='comisansns 15').place(x=80, y=170) 
 
    password=Label(frame1,text="Password:",background='white',foreground='blue',font='comisansns 15').place(x=80, y=220) 
    cpass=Label(frame1,text="Confirm Password:",background='white',foreground='blue',font='comisansns 15').place(x=80, y=270) 
    email=Label(frame1,text="Enter Valid Email:",background='white',foreground='blue',font='comisansns 15').place(x=80, y=320)
    
    uu=StringVar() 
    us=StringVar() 
    ug=StringVar() 
    uz=StringVar() 
    ur=StringVar()
 
    user=Entry(frame1,textvariable=ug,font=("times new roman",13)).place(x=370, y=120, height=25, width=150) 
    IDD=Entry(frame1,textvariable=ur,font=("times new roman",13)).place(x=370, y=170, height=25, width=150) 
    passs=Entry(frame1,textvariable=uu,font=("times new roman",15),show='*').place(x=370, y=220, height=25, width=150) 
    cpasss=Entry(frame1,textvariable=us,font=("times new roman",15),show='*').place(x=370, y=270, height=25, width=150) 
    emaill=Entry(frame1,textvariable=uz,font=("times new roman",15)).place(x=370, y=320, height=25, width=150)
    
    Label(frame1,text='For Account Details please Login, By Default your balance will be ₹0',background='lavenderblush2',foreground='red',font="comisansns 12").place(x=50,y=360) 
    Button(frame1,text='Register',command=reg).place(x=350, y=400, height=30, width=150 )

    root.mainloop()

 
def reg(): 
     #conn=mysql.connector.connect(host='localhost',user='root',passwd='user@12#',database='atm')
     conn = sql.connect("data\dbms.sqlite")
     #m=conn.cursor() 
     a = conn.execute("select * from userinfo;") 
     a=a.fetchall()
     
     try:
         if len(ug.get())==0: 
             tmsg.showerror('Error'," Please enter Username. You cannot leave this field blank.")
     
         elif len(ur.get())==0:
             tmsg.showerror('Error'," Please enter UserID. You cannot leave this field blank")
             
         elif len(uu.get())==0: 
             tmsg.showerror('Error'," Please Enter Password. You cannot leave this field blank")
             
         elif len(uu.get()) > 5: 
             tmsg.showerror('Error'," Password execced it's Limit (i.e. 5 numbers)")
             
         elif len(uz.get())==0: 
             tmsg.showerror('Error'," Please Enter Email address. You cannot leave this field blank")
             
         else:
            
             if uu.get()==us.get():
                
                 val=((len(a)+1),ug.get(),ur.get(),uu.get(),0,random.randint(100000000,999999999),uz.get()) 
                 qry='insert into userinfo (SR_NO,NAME,username,PASSWORD,BALANCE,ACCOUNT_NO,EMAIL) values(?,?,?,?,?,?,?)' 

                 conn.execute(qry,val) 

                 conn.commit() 
                 conn.close() 

                 tmsg.showinfo('Successful','You are successfully registered')

                 
             elif uu.get() != us.get():
                 
                 tmsg.showerror('Unsuccessful',"Password Doesn't match") 

     except:
        
         tmsg.showerror('Error'," UserID Already Exists, Please Change") 
 

def tab2():
    
    root=Toplevel()
    root.geometry("640x440+300+150") 
    root.title("ATM SYSTEM") 
    bk=ImageTk.PhotoImage(file='data\image.jpg')
    bgj=Label(root,image=bk).place(x=0,y=0,relwidth=1,relheight=1)
    
    frame1=Frame(root) 
    frame1.place(x=20,y=20,width=600,height=400)
    
    a=Label(frame1,text=" Welcome To ATM Services ",background='light grey',foreground='green',font='comisansns 30 bold',borderwidth=5,relief=RIDGE) 
    a.place(x=40, y=10)
    
    Label(frame1,text ="HOME PAGE",background='lavenderblush2',foreground='orange',font='comisansns 20 bold').place(x=220, y=75) 
    Label(frame1,text ="We Provide Following Services",background='lavenderblush2',foreground='black',font='comisansns 17 bold').place(x=120, y=125) 

    Label(frame1,text ="To Check Your Account Details:",background='light blue',foreground='purple',font='comisansns 15').place(x=75, y=200)
    btn1=Button(frame1,text="Account Details", command=tab3).place(x=400, y=200, height=30, width=100) 

    Label(frame1,text ="To Withdraw Amount in ₹ :",background='light blue',foreground='blue',font='comisansns 15').place(x=75, y=250) 
    btn2=Button(frame1,text="Withdraw", command=tab4).place(x=400, y=250, height=30, width=100) 

    Label(frame1,text ="To Deposit Amount in ₹ :",background='light blue',foreground='red',font='comisansns 15').place(x=75, y=300) 
    btn3=Button(frame1,text="Deposit", command=tab5).place(x=400, y=300, height=30, width=100) 

    Button(frame1,text='Log out',command=root.destroy).place(x=250, y=350, height=30, width=100) 
    Button(frame1,text='↺',command=lambda:[root.destroy(), connection1()]).place(x=500,y=125, height=30, width=30) 

    root.mainloop()

 
def tab3():
    
    global s
    
    root=Toplevel() 
    root.geometry("640x500+300+150") 
    root.title("ATM SYSTEM") 
    b=ImageTk.PhotoImage(file='data\image.jpg')
    bgj=Label(root,image=b).place(x=0,y=0,relwidth=1,relheight=1)
    
    frame1=Frame(root) 
    frame1.place(x=20,y=20,width=600,height=450)
    
    a=Label(frame1,text=" Welcome To ATM Services ",background='light grey',foreground='green',font='comisansns 30 bold',borderwidth=5,relief=RIDGE) 
    a.place(x=40, y=10)
    
    Label(frame1,text =" Account Details: ", background='lavenderblush2',foreground='orange',font='comisansns 20 bold').place(x=170, y=75) 
    Label(frame1,text="Account Holder's Name:"+ str(s[1]), background='lavenderblush2', foreground='black', font='comisansns 15').place(x=100,y=125) 
    Label(frame1,text="Account Number :"+str(s[5]), background='lavenderblush2', foreground='black', font='comisansns 15').place(x=100,y=175) 
    Label(frame1,text="Your Username:"+ str(s[2]), background='lavenderblush2', foreground='black', font='comisansns 15').place(x=100,y=225) 
    Label(frame1,text="Your password:"+str(s[3]), background='lavenderblush2', foreground='black', font='comisansns 15').place(x=100,y=265) 
    Label(frame1,text="Current Balance Available:"+str(s[4]), background='lavenderblush2', foreground='black', font='comisansns 15').place(x=100,y=315) 
    Label(frame1,text="Email Address :"+str(s[6]), background='lavenderblush2', foreground='black', font='comisansns 15').place(x=100,y=365) 

    Button(frame1,text='Back To Home',command=root.destroy).place(x=470, y=400, height=30, width=100) 

    root.mainloop()

    
def tab4():
    
    global s 
    global q
    
    root=Toplevel() 
    root.geometry("640x440+300+150") 
    root.title("ATM SYSTEM")
    b=ImageTk.PhotoImage(file='data\image.jpg') 
    bgj=Label(root,image=b).place(x=0,y=0,relwidth=1,relheight=1)
    frame1=Frame(root)
    frame1.place(x=20,y=20,width=600,height=400)
    
    
    
    a=Label(frame1,text=" Welcome To ATM Services ",background='light grey',foreground='green',font='comisansns 30 bold',borderwidth=5,relief=RIDGE) 
    a.place(x=40, y=10)
    
    Label(frame1,text="Withdrawal page",background='lavenderblush2',foreground='orange',font='comisansns 20 bold').place(x=220, y=75)

    t='Your Current Balance is ₹ '+ str(s[4]) 
    a=Label(frame1,text=t,background='lavenderblush2',foreground='black',font="comisansns 15").place(x=50,y=140) 

    w=Label(frame1,text="Amount to be Withdraw in ₹ :",background='lavenderblush2',foreground='red',font="comisansns 15 bold").place(x=50, y=190) 
    q=Entry(frame1,font=("times new roman",15)) 
    q.place(x=200,y=230, height=39, width=200) 

    Button(frame1,text="Withdraw",command=connection2).place(x=225,y=280, height=30, width=150 ) 
    Button(frame1,text='Back To Home',command=root.destroy).place(x=350, y=350, height=30, width=150 ) 

    root.mainloop() 
 
def connection2(): 

    global q 
    global pv 
    global s 

    a=s[4] 
    w=int(q.get()) 
    query="update userinfo set balance=balance-? where password=?" 

    value=(q.get(),pv.get()) 
    v=tmsg.askquestion("Confirmation","Are You Sure You want to continue the Trasaction?") 

    if v=="yes":

        if int(s[4])>=int(q.get()): 

            #conn=mysql.connector.connect(host='localhost',user='root',passwd='user@12#') 
            conn = sql.connect("data\dbms.sqlite")
            #m=conn.cursor() 

            #m.execute('use atm') 
            conn.execute(query,value) 

            conn.commit() 
            conn.close()

            now=datetime.now()
        
            file=open("Transaction Details.txt",'a+') 
            line="Username: "+str(s[1])+'\n'+"Withdrawn Rs "+str(q.get())+' on '+str(now)+'\n' 
            file.write(line) 
            file.write('\n') 
            file.close()

            dis="Congratulations! Your transaction of ₹ "+str(q.get())+" is successful" 
            tmsg.showinfo("Done",dis) 

        else: 

            tmsg.showerror("Error","No Sufficient Balance In Your Account. Please Retry Again") 
    else:
        
        tmsg.showinfo("Cancel","Your Transaction is Cancelled")
         
def tab5():
    
    global s 
    global q

    root=Toplevel() 
    root.geometry("640x440+300+150") 
    root.title("ATM SYSTEM")
    b=ImageTk.PhotoImage(file='data\image.jpg') 
    bgj=Label(root,image=b).place(x=0,y=0,relwidth=1,relheight=1)
    
    frame1=Frame(root)
    frame1.place(x=20,y=20,width=600,height=440)
    
    a=Label(frame1,text=" Welcome To ATM Services ",background='light grey',foreground='green',font='comisansns 30 bold',borderwidth=5,relief=RIDGE) 
    a.place(x=40, y=10)
    Label(frame1,text="Deposition page",background='lavenderblush2',foreground='orange',font='comisansns 20 bold').place(x=220, y=75)
    
    t='Your Current Balance is ₹ '+ str(s[4])
    
    a=Label(frame1,text=t,background='lavenderblush2',foreground='black',font="comisansns 15").place(x=50,y=140) 
    w=Label(frame1,text="Amount to be deposit in ₹ :",background='lavenderblush2',foreground='red',font="comisansns 15 bold").place(x=50, y=190)
    
    q=Entry(frame1,font=("times new roman",15)) 
    q.place(x=200,y=230, height=39, width=200)
    
    Button(frame1,text="Deposit",command=connection3).place(x=225,y=280, height=30, width=150 ) 
    Button(frame1,text='Back To Home',command=root.destroy).place(x=350, y=350, height=30, width=150)
    
    root.mainloop() 


def connection3():
    
    global q 
    global pv 
    global s
    
    query="update userinfo set balance=balance+? where password=?" 
    values=(q.get(),pv.get()) 
    v=tmsg.askquestion("Confirmation","Are You Sure you want to continue the Transaction?")
    
    if v=="yes":
        
        #conn=mysql.connector.connect(host='localhost',user='root',passwd='user@12#') 
        #m=conn.cursor()
        conn = sql.connect("data\dbms.sqlite")
        #m.execute('use atm')
        conn.execute(query,values)
        
        conn.commit() 
        conn.close()
        
        now=datetime.now()
        
        file=open("Transaction Details.txt",'a+') 
        line="Username: "+str(s[1])+'\n'+"deposited Rs "+str(q.get())+' on '+str(now)+'\n' 
        file.write(line) 
        file.write('\n') 
        file.close()
        
        dis="Congratulations! Your transaction of ₹ "+str(q.get())+" is successful " 
        tmsg.showinfo("Done",dis)
        
    else:
        
        tmsg.showinfo("Cancel","Your transaction is Cancelled")

         

try:
    conn = sql.connect("data\dbms.sqlite")
    #conn.execute("""drop table DEMO;""")
    conn.execute(""" CREATE TABLE userinfo
    (SR_NO int NOT NULL,
    NAME char NOT NULL,
    username varchar NOT NULL,
    PASSWORD int NOT NULL,
    BALANCE int NOT NULL,
    ACCOUNT_NO int NOT NULL,
    EMAIL varchar NOT NULL);""")

    conn.close()
except:
    pass

tab1()
