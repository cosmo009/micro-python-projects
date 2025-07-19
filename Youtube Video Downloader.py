
import yt_dlp
import tkinter as t
import tkinter.font as tfont
from tkinter import filedialog

root=t.Tk()
root.title("Youtube Video Download")
root.geometry("510x180")

#DECOR SPACES
s1=t.Label().grid(row=0)
s2=t.Label(width=3).grid(row=1,column=0)
s3=t.Label().grid(row=2)

#FONTS
custom1=tfont.Font(size=15)
custom2=tfont.Font(font="Georgia",size=7)
custom3=tfont.Font(size=9,font="Georgia")

#LINK RELATED STUFF
linkL=t.Label(text="Enter Video Link:  ",font=custom2).grid(row=1,column=1)
link=t.StringVar()
linkE=t.Entry(font=custom1,textvariable=link,width=25).grid(row=1,column=2,columnspan=3)

"""
#PATH

pStr=t.StringVar()
pLabel=t.Label(text="Enter path",font=custom3).grid(row=5,column=1)
pEntry=t.Entry(textvariable=pStr,state="readonly",font=custom3).grid(row=5,column=2)

def select_path():
    pStr.set(filedialog.askdirectory())

pStr_1=str(pStr.get())+"%(title)s.%(ext)s"
pathB=t.Button(text="📁",command=select_path).grid(row=5,column=3)
"""
#DOWNLOAD 
ydl_opts_1 = {
            "outtmpl":"Youtube Downloads/%(title)s.%(ext)s"
        }   
"""
ydl_opts_2 = {                                           #not working

            "outtmpl":"Youtube Downloads/%(title)s.%(ext)s",
            'postprocessors': [{                                # Post-process to convert to MP3
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',                            # Convert to mp3
            'preferredquality': '0',                            # '0' means best quality, auto-determined by source
            }],
        } """
def YtDownload_mp4():
    try:
        with yt_dlp.YoutubeDL(ydl_opts_1) as ydl:
            ydl.download([link.get()])
    except Exception as e:
        link.set("ERROR")

"""
def YtDownload_mp3():
    try:
        with yt_dlp.YoutubeDL(ydl_opts_2) as ydl:
            ydl.download([link.get()])
    except Exception as e:
        link.set("ERROR")
"""
dwnldB_mp4=t.Button(text="Download Video",font=custom2,command=YtDownload_mp4,width=25).grid(row=3,column=1,columnspan=4)
#dwnldB_mp3=t.Button(text="Download Audio",font=custom2,command=YtDownload_mp3,width=25).grid(row=4,column=1,columnspan=4)

root.mainloop()