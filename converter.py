from Tkinter import *

root= Tk()
root.geometry("300x300+250+250")
root.title("Convert RON/EURO")
root.resizable(width=False, height=False)

headint = Label(root,text="Convertor RON/EURO" , font=('arial 13 bold') , fg="black").pack()

entr_amt= Label(root , text="Enter RON/EURO:", font=('arial 20 bold')).place(x=10,y=50)

my_num=IntVar()
ent_box=Entry(root,width=50,textvariable=my_num).place(x=10,y=90)

def convertlei():
	aici= my_num.get()
	final= aici * 4.66071091
	lab = Label(root, text=str(final) + " RON").place(x=10,y=170)



buton1= Button(root,text="ConvertRON" , width=12 , height=2 ,bg="lightgreen",command=convertlei).place(x=10 , y=130)

def convertEURO():
	aici= my_num.get()
	final= aici * 0.214559543
	lab = Label(root, text=str(final) + " EURO").place(x=10,y=260)

buton1= Button(root,text="ConvertEURO" , width=12 , height=2 ,bg="lightgreen",command=convertEURO).place(x=10 , y=220)
credits = Label(root,text="by Pacze" , font=("Times New Roman", 12, "italic") , fg="black").place(x=240,y=275)






root.mainloop()

