import tkinter as tk
from tkinter import ttk 
import random as r
root=tk.Tk()
root.title("Password Manager")
root.geometry("440x190")
root.config(background="#4E5050")

#password box
pwrd=tk.Label(text="PASSWORD",width=24).grid(row=1,column=0,columnspan=2)
password=tk.Entry(root,width=40)
password.grid(row=1,column=2,columnspan=4)

#Password length
pwrdLenLabel=tk.Label(text="Password Length",width=24).grid(row=2,column=0,columnspan=2)
coLen=tk.IntVar()
pwrdLen=ttk.Combobox(width=37,values=list(range(1,21)),textvariable=coLen).grid(row=2,column=2,columnspan=4)

#Checkbox
U_var=tk.BooleanVar()
labelUpper=tk.Label(text="Uppercase letters",width=20).grid(row=4,column=0)
checkUpper=tk.Checkbutton(variable=U_var).grid(row=4,column=1)

L_var=tk.BooleanVar()
labelLower=tk.Label(text="Lowercase letters",width=20).grid(row=5,column=0)
checkLower=tk.Checkbutton(variable=L_var).grid(row=5,column=1)

D_var=tk.BooleanVar()
labelDigits=tk.Label(text="Digits",width=20).grid(row=6,column=0)
checkDigit=tk.Checkbutton(variable=D_var).grid(row=6,column=1)

S_var=tk.BooleanVar()
labelSpecial=tk.Label(text="Special Characters",width=20).grid(row=7,column=0)
checkSpecial=tk.Checkbutton(variable=S_var).grid(row=7,column=1)


#clear button
def clear():
    password.delete(0,tk.END)
bclear=tk.Button(text="clear",width=16,command=clear).grid(row=3,column=2)

#copy button
def copy2clip():
    root.clipboard_append(password.get())
bcopy=tk.Button(text="copy",width=16,command=copy2clip).grid(row=3,column=3)
#create button
pass_list=[]
def createpass():
    global pass_list
    i=0
    while i<coLen.get():
        l=r.randint(97,122)
        u=r.randint(65,90)
        d=r.randint(48,57)
        s1=r.randint(33,38)
        s2=r.choice([63,64,94,95])
        if U_var.get():
            pass_list.append(u)
        if L_var.get():
            pass_list.append(l)
        if D_var.get():
            pass_list.append(d)
        if S_var.get():
            pass_list.append(s1)
            pass_list.append(s2)
        
        choose=r.choice(pass_list)
        password.insert(tk.END,chr(choose))
        pass_list.clear()
        
        i+=1

createb=tk.Button(text="create",width=24,command=createpass).grid(row=3,column=0,columnspan=2)

root.mainloop()
