import tkinter as tk   #importing tkinter library

from pytube import YouTube #importing the pytube library

def downloadVid():
    global E1

string=E1.get()

yt= YouTube(str(string))

videos = yt.get_videos() #this will return a list to choose the video quality

s=1

for v in videos:
    print(st(s)+'.'+str(v))

s+=1

n=int(input("Enter your choice"))

vid = videos[n-1]

destination=str(input("Enter your destination"))

vid.download(destination)

print(yt.filename+"\n is downloaded")

root=tk.Tk() #initializing root component

w=tk.Label(root,text="Youtube Downloader") #widget creation

w.pack()

#entry box is created to past the link

E1=tk.Entry(root,bd=5)

E1.pack(side=tk1.TOP)  #it is organized using pack function

#Button is created so the program is triggered when it is pressed

button=tk.Button(root,text="Download",command=downloadVid )

button.pack(side=tk.BOTTOM)

#When the button is clicked whatever the function inside the command will be executed in our case the command is to download the youtube video.

root.mainloop()

