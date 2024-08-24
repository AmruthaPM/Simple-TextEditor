import sys
import tkinter
#import filedialog
import tkinter.filedialog
v=sys.version

if "2.7" in v:
    from tkinter import *
elif "3.3" in v or "3.4" in v:
    from tkinter import *
root=tkinter.Tk()
root.title("Text Editor")
text=tkinter.Text(root)
text.grid()
def saves():
    global text
    t=text.get("1.0","end-1c")
    savelocation=filedialog.asksaveasfilename()
    f1=open(savelocation,"w+")
    f1.write()
    f1.close()
button=tkinter.Button(root, text="save", command=saves)
button.grid()
def FontHelvetica():
    global text
    text.config(font="Helvetica")
def FontCourier():
    global text
    text.config(font="Courier")
font=tkinter.Menubutton(root, text="Font")
font.grid()
font.menu=tkinter.Menu(font, tearoff=0)
font["menu"]=font.menu
helvetica=tkinter.IntVar()
courier=tkinter.IntVar()
font.menu.add_checkbutton(label="Courier", variable=courier, command=FontCourier)
font.menu.add_checkbutton(label="Helvetica", variable=helvetica,command=FontHelvetica)


root.mainloop()    