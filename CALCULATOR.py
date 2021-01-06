from tkinter import *


def click(event):
    text = event.widget.cget("text")
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            value = eval(screen.get())

        scvalue.set(value)
        screen.update()

    elif text == "C" or text == "DEL":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()


root = Tk()
root.geometry("480x660")
root.title("CALCULATOR")
root['bg'] = '#26e'


scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="lucida 30 bold",
               bg="lawn green", border="7px")
screen.pack(fill=X, ipadx=10, padx=5)

# =========================================================================================================
f = Frame(root, bg="grey")
b = Button(f, text="9", padx=18, font="lucida 25 bold",
           bg="orange", border="5px")
b.pack(padx=5, pady=10, side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="8", padx=18, font="lucida 27 bold",
           bg="yellow", border="2px", fg="green")
b.pack(padx=5, pady=10, side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="7", padx=17, font="lucida 25 bold",
           bg="lightgreen", border="5px", fg="red")
b.pack(padx=5, pady=10, side=LEFT)
b.bind("<Button-1>", click)
f.pack()
# =====================================================================================================
f = Frame(root, bg="grey")
b = Button(f, text="6", padx=13, font="lucida 25 bold",
           bg="lightgreen", border="2px", fg="darkOrchid4")
b.pack(padx=5, pady=10, side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="5", padx=15, font="lucida 25 bold",
           bg="lawn green", border="6px")
b.pack(padx=5, pady=15, side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="4", padx=17, font="lucida 25 bold",
           bg="orange", border="2px", fg="blue")
b.pack(padx=5, pady=10, side=LEFT)
b.bind("<Button-1>", click)
f.pack()
# =================================================================================================
f = Frame(root, bg="grey")
b = Button(f, text="3", padx=15, font="lucida 25 bold",
           bg="yellow", border="7px", fg="#34F")
b.pack(padx=5, pady=10, side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="2", padx=15, font="lucida 25 bold",
           bg="VioletRed1", border="2px")
b.pack(padx=5, pady=10, side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="1", padx=15, font="lucida 25 bold",
           bg="lightgreen", border="6px", fg="IndianRed2")
b.pack(padx=5, pady=10, side=LEFT)
b.bind("<Button-1>", click)
f.pack()
# ===============================================================================================
f = Frame(root, bg="grey")
b = Button(f, text="0", padx=15, font="lucida 25 bold",
           bg="SteelBlue2", border="5px", fg="salmon4")
b.pack(padx=5, pady=10, side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="-", padx=20, font="lucida 25 bold",
           bg="gold2", border="2px")
b.pack(padx=5, pady=10, side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="*", padx=16, font="lucida 25 bold",
           bg="navajo white", border="4px", fg="deep sky blue")
b.pack(padx=5, pady=10, side=LEFT)
b.bind("<Button-1>", click)
f.pack()
# ----------------------------------------------------------------------------------------------
f = Frame(root, bg="grey")
b = Button(f, text="/", padx=20, font="lucida 25 bold",
           bg="cyan2", border="2px")
b.pack(padx=5, pady=10, side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="+", padx=15, font="lucida 25 bold",
           bg="red", border="5px", fg="yellow")
b.pack(padx=5, pady=10, side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="=", padx=19, font="lucida 25 bold",
           bg="coral", border="2px")
b.pack(padx=5, pady=10, side=LEFT)
b.bind("<Button-1>", click)
f.pack()
# -----------------------------------------------------------------------------------------------
f = Frame(root, bg="grey")
b = Button(f, text="C", padx=8, font="lucida 25 bold",
           bg="orange3", border="2px")
b.pack(padx=5, pady=10, side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text=".", padx=14, font="lucida 26 bold",
           bg="lightblue", border="2px")
b.pack(padx=5, pady=10, side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="DEL", font="lucida 25 bold",
           bg="cyan", border="2px", fg="red")
b.pack(padx=5, pady=12, side=LEFT)
b.bind("<Button-1>", click)
f.pack()
# -------------------------------------------------------------------------------------------------


root.mainloop()
