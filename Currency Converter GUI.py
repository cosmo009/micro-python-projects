import json
import requests
from tkinter import Label,StringVar,IntVar,Entry,Tk,Button,messagebox,ttk
res=json.loads((requests.get("https://api.exchangerate-api.com/v4/latest/INR")).text)

win=Tk()
win.title("Currency Converter")
win.geometry("310x120")
win.configure(bg="#749874")

#DECORATING SPACES
s1=Label(bg="#749874").grid(row=0)
s2=Label(bg="#749874").grid(row=1,column=0)
s3=Label(bg="#749874").grid(row=2,column=3)
s4=Label(bg="#749874").grid(row=5,column=0)

#LABELS
l1=Label(text="Convert from",width=19,bg="#415B41",fg="#D0CD75").grid(row=1,column=1,columnspan=2)
l2=Label(text="Convert to",width=19,bg="#415B41",fg="#D0CD75").grid(row=1,column=4,columnspan=2)

#(COMBOBOX)currency name list
currency=list(filter(lambda x:x,res["rates"]))

c1_var=StringVar()
c2_var=StringVar()

cb1=ttk.Combobox(values=currency,textvariable=c1_var).grid(row=2,column=1,columnspan=2)
cb2=ttk.Combobox(values=currency,textvariable=c2_var).grid(row=2,column=4,columnspan=2)

#AMT ENTRY
a1=IntVar()
a2=IntVar()
e1=Entry(width=23,textvariable=a1).grid(row=4,column=1)
e2_ans=Entry(win,textvariable=a2,width=23,state="readonly").grid(row=4,column=4)


def convert():
    value=a1.get()
    a,b=c1_var.get(),c2_var.get()
    a2.set(float(value)*float(res["rates"][b])/float(res["rates"][a]))

cConvert=Button(text="convert",command=convert,width=20,bg="#D0CD75").grid(row=5,column=1,columnspan=4)


win.mainloop()
