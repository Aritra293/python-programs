from tkinter import *
def click(event):
 global scvalue
text =event.widget.cget("text")
if text == '=':
    if scvalue.get().isdigit():
      value = int(scvalue.get())
    else:
        value = eval(screen.get())

    scvalue.set(value)
    screen.update()
elif text == 'C':
    scvalue.set("")
    screen.update()
else:
    screen.update()
    window = Tk()
    window.geometry(600,650)
    window.minsize(600,650)
    window.maxsize(600,650)
    window.config(bg="gray")
    window.title("calculator  by aritra")

    scvalue = StringVar()
    scvalue.set("")
    f= Frame(window,bg="gray")
    screen = Entry(f,textvar=scvalue,font= "lucida 50 bold",bg="green")
    screen.pack(fill=X,padx=20,pady=15)
    f.pack()

    options1 =["7","8","9","+"]
    options2 =["4","5","6","-"]
    options3 =["1","2","3","*"]
    options4 =["0","C","=","/"]

    f = Frame(window,bg='gray',padx =30, pady =10)
    for i in   options2:
        b =Button(f,text=i,padx=10,pady =10, font = "lucida 25 bold")
        b.pack(side=LEFT,padx= 10,pady=10)
        b.bind("<Button-l>",click)
    f.pack()
    f = Frame(window,bg='gray',padx =30, pady =10)
for i in   options3:
        b =Button(f,text=i,padx=10,pady =10, font = "lucida 25 bold")
        b.pack(side=LEFT,padx= 10,pady=10)
        b.bind("<Button-l>",click)
f.pack()
f = Frame(window,bg='gray',padx =30, pady =10)
for i in   options4:
        b =Button(f,text=i,padx=10,pady =10, font = "lucida 25 bold")
        b.pack(side=LEFT,padx= 10,pady=10)
        b.bind("<Button-l>",click)
f.pack()

window.mainloop()


