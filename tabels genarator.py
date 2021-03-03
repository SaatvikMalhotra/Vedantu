from tkinter import *
from tkinter.ttk import *

def genarateTable():
    end=int(stop.get())
    table=""
    for x in range(1,end+1,1):
        table=table+str(num.get())+"  x  "+str(x)+"  =  "+str(num.get()*x)+"\n"
    result.configure(text=table)



win=Tk()
win.title("Maths Table Generator")
win.geometry('400x600')
win.configure(bg="black")
heading=Label(win,text="Matematical Table Genatator",foreground="black")
quests=Label(win,text="Choose a number:",foreground="white")
button=Button(win,text="GENERATE",command=genarateTable)

heading.grid(row=0,column=1)
quests.grid(row=1,column=0,pady=20,padx=10)
button.grid(row=4,column=1)

num=IntVar()
numbers=Combobox(win,textvariable = num,width=6)
numbers['values'] = tuple(range(101))

stop = IntVar()
r10=Radiobutton(win,text="10",variable=stop,value=10)
r20=Radiobutton(win,text="20",variable=stop,value=20)
r30=Radiobutton(win,text="30",variable=stop,value=30)
stop.set(10)

numbers.grid(row=1,column=1)
r10.grid(column=2,row=1,padx=30)
r20.grid(column=2,row=2,padx=30)
r30.grid(column=2,row=3,padx=30)
result=Label(win,anchor="center")
result.grid(row=5,column=1,pady=20)

win.mainloop()


