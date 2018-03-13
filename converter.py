from Tkinter import *

root= Tk()
root.geometry("400x400+250+250")
root.title("Covertor EURO/LEI")

headint = Label(root,text="Convertor Lei/Euro" , font=('arial 13 bold') , fg="steelblue").pack()

entr_amt= Label(root , text="Introduceti LEI/EURO:", font=('arial 20 bold')).place(x=10,y=50)

my_num=IntVar()
ent_box=Entry(root,width=50,textvariable=my_num).place(x=10,y=90)

def convertlei():
	aici= my_num.get()
	final= aici * 4.66071091
	lab = Label(root, text=str(final) + " lei").place(x=10,y=170)



buton1= Button(root,text="ConvertLEI" , width=12 , height=2 ,bg="lightgreen",command=convertlei).place(x=10 , y=130)

def convertEURO():
	aici= my_num.get()
	final= aici * 0.214559543
	lab = Label(root, text=str(final) + " euro").place(x=10,y=260)

buton1= Button(root,text="ConvertEURO" , width=12 , height=2 ,bg="lightgreen",command=convertEURO).place(x=10 , y=220)






root.mainloop()

