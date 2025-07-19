import pyttsx3
import tkinter as t
import tkinter.font as tfont

def say(element):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

    rates=engine.getProperty('rate')
    engine.setProperty('rate',rates-50)

    engine.say(str(element))
    engine.runAndWait()
"""
while True:
    inp=input("Got something to say(y/n)?").lower()
    if inp=='y':
        s2=str(input("Enter a sentence:"))
        say(s2) 
    else:
        say("Okay...Bye Bye")
        break
"""
#now converting this to gui
root=t.Tk()
root.title("Text to Speech")
root.geometry("350x150")
root.config(bg="#7796a8")

#s1=t.Label().grid(row=0)
s2=t.Label(width=3,bg="#7796a8").grid(row=1,column=0)
s3=t.Label(bg="#7796a8").grid(row=3)


var=t.StringVar()
custom=tfont.Font(size=18)
t1=t.Entry(width=23,textvariable=var,font=custom).grid(row=2,column=1)

b1=t.Button(text="SPEAK",command=lambda:say(var.get())).grid(row=4,column=1,columnspan=3)

root.mainloop()