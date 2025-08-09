from tkinter import Label,Tk,Entry,END,Button,messagebox
import re

t=Tk()
t.title("Calculator")
t.geometry("363x147")
t.configure(bg="#242424")
branding=Label(text="𝐆𝐂𝐀𝐋𝐂𝐢𝐢𝟎𝟎𝟕",height="2",width="16",bg="#000000",fg="#ffe600")
branding.grid(row=0,column=3,rowspan=2,columnspan=4)
#input dialog
inDialog=Entry(t,width="40")
inDialog.grid(row=0,column=0,columnspan=3)

#solution box
solution=Entry(t,width="40")
solution.grid(row=1,column=0,columnspan=3)

#input in input dialog box
def outDialog(a):
    inDialog.insert(END,a)

#ALL CLEAR BUTTON + command
def clearAll():
    inDialog.delete(0,END)
    #solution.delete(0,END)

bAC=Button(text="AC",width="7",height="1",bg="#8b77e2",fg="#fff",command=clearAll)
bAC.grid(row=4,column=3)


#BACKSPACE BUTTON
def backspace():
    inDialog.delete(inDialog.index("end") - 1)

    
bBack=Button(text="⌫",width="7",height="1",bg="#4e4646",fg="#fff",command=backspace)
bBack.grid(row=2,column=3)


#EQUAL TO BUTTON

def searchOP():
    if not (inDialog.get()):
        solution.delete(0,END)
        solution.insert(0,"ERROR")
    else: 
        try:
            inputText=eval(inDialog.get())
            solution.delete(0,END)
            solution.insert(0,inputText)
        except ZeroDivisionError:
            messagebox.showerror("INVALID REQUEST","Cannot divide by zero")
        
            

bEqual2=Button(text="=",width="7",height="1",bg="#ACACAC",fg="black",command=searchOP)
bEqual2.grid(row=5,column=3)  

#DECIMAL BUTTON
bDecimal=Button(text=".",width="10",height="1",bg="#575050",fg="#fff",command=lambda:outDialog("."))
bDecimal.grid(row=5,column=2)


#OFF Button

bOFF=Button(text="  OFF",width="7",height="1",bg="#ea813a",fg="#fff",command=t.destroy)
bOFF.grid(row=3,column=3)


#Number buttons

b0=Button(text="0",width="22",height="1",bg="#575050",fg="#fff",command=lambda:outDialog(0))
b0.grid(row=5,column="0",columnspan=2)

b1=Button(text="1",width="10",height="1",bg="#575050",fg="#fff",command=lambda:outDialog(1))
b1.grid(row=2,column=0)

b2=Button(text="2",width="10",height="1",bg="#575050",fg="#fff",command=lambda:outDialog(2))
b2.grid(row=2,column=1)

b3=Button(text="3",width="10",height="1",bg="#575050",fg="#fff",command=lambda:outDialog(3))
b3.grid(row=2,column=2)

b4=Button(text="4",width="10",height="1",bg="#575050",fg="#fff",command=lambda:outDialog(4))
b4.grid(row=3,column=0)

b5=Button(text="5",width="10",height="1",bg="#575050",fg="#fff",command=lambda:outDialog(5))
b5.grid(row=3,column=1)

b6=Button(text="6",width="10",height="1",bg="#575050",fg="#fff",command=lambda:outDialog(6))
b6.grid(row=3,column=2)

b7=Button(text="7",width="10",height="1",bg="#575050",fg="#fff",command=lambda:outDialog(7))
b7.grid(row=4,column=0)

b8=Button(text="8",width="10",height="1",bg="#575050",fg="#fff",command=lambda:outDialog(8))
b8.grid(row=4,column=1)

b9=Button(text="9",width="10",height="1",bg="#575050",fg="#fff",command=lambda:outDialog(9))
b9.grid(row=4,column=2)

#OPERATORS
def add(a,b):
    return solution.insert(0,a+b)
bAdd=Button(text="+",width="7",height="1",bg="#575050",fg="#fff",command=lambda:outDialog("+"))
bAdd.grid(row=2,column=4)

def subtract(c,d):
    return solution.insert(0,c-d)
bSub=Button(text="-",width="7",height="1",bg="#575050",fg="#fff",command=lambda:outDialog("-"))
bSub.grid(row=3,column=4)

def product(e,f):
    return solution.insert(0,e*f)
bProd=Button(text="X",width="7",height="1",bg="#575050",fg="#fff",command=lambda:outDialog("*"))
bProd.grid(row=4,column=4)

def division(g,h):
    return solution.insert(0,g/h)
bDiv=Button(text="÷",width="7",height="1",bg="#575050",fg="#fff",command=lambda:outDialog("/"))
bDiv.grid(row=5,column=4)

t.mainloop()

