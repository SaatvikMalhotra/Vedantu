from tkinter import*
from tkinter import ttk
from gtts import gTTS
import os
import speech_recognitionas as sr
from googletrans import Translator,LANGUAGES




win=Tk()
win.title("Language converter")
win.configure(bg="gold")

def convertAudio():
  audio=gTTS(text=entry1.get(),lang="en")
  audio.save("sample123.mp3")
  os.system("sample123.mp3")

def Translate():
  translator=Translator()
  translated=translator.translate(text=entry1.get(),src="en",dest=comb.get())
  output.delete(1.0,END)
  output.insert(END,translated.text)






heading=Label(win,text="Converter",font=("Showcard Gothic",30),background="gold")
heading.grid(row=0,column=1,padx=20,pady=20)

btn1=Button(win,text="Convert to audio",width=30,height=3,background="red",command=convertAudio)
btn2=Button(win,text="Translate",width=30,height=3,background="red",command=Translate)

label1=Label(win,text="Enter your text:",width=30,height=3,background="red")

languages=list(LANGUAGES.values())

comb=ttk.Combobox(win,value=languages,width=30,background="red")

output=Text(win,width=40,height=2)

entry1=Entry(win,width=50)

btn1.grid(row=1,column=2,padx=20,pady=20)
btn2.grid(row=2,column=2,padx=20,pady=20)

entry1.grid(row=1,column=1,padx=20,pady=20)

label1.grid(row=1,column=0,padx=20,pady=20)

comb.grid(row=2,column=0,padx=20,pady=20)

output.grid(row=2,column=1,padx=20,pady=20)
