from tkinter import *
def btnclick(numbers):
    global operator
    operator=operator + str(numbers)
    text_input.set(operator)

def btnClearDisplay():
    global operator
    operator=""
    text_input.set("")

def btnEqual():
    global operator
    sumup=str(eval(operator))
    text_input.set(sumup)
    operator=""







cal=Tk()
cal.title("calculator")
cal.resizable(0, 0)
cal.geometry("385x500+0+0")
operator=""
text_input=StringVar()
textDisplay=Entry(cal,font=('arial',20,'bold'),textvariable=text_input,bd=30,insertwidth=4,
                  bg="powder blue",justify='right').grid(columnspan=4)
btn7=Button(cal,padx=16,pady=16,bd=8,fg="black",bg="powder blue",font=('arial',20,'bold'),text="7",command=lambda:btnclick(7)).grid(row=1,column=0)
btn8=Button(cal,padx=16,pady=16,bd=8,fg="black",bg="powder blue",command=lambda:btnclick(8),font=('arial',20,'bold'),text="8").grid(row=1,column=1)
btn9=Button(cal,padx=16,pady=16,bd=8,fg="black",bg="powder blue",command=lambda:btnclick(9),font=('arial',20,'bold'),text="9").grid(row=1,column=2)
addition=Button(cal,padx=16,pady=16,bd=8,fg="black",bg="powder blue",command=lambda:btnclick("+"),font=('arial',20,'bold'),text="+").grid(row=1,column=3)
# ......................................................................................................................
btn4=Button(cal,padx=16,pady=16,bd=8,fg="black",bg="powder blue",command=lambda:btnclick(4),font=('arial',20,'bold'),text="4").grid(row=2,column=0)
btn5=Button(cal,padx=16,pady=16,bd=8,fg="black",bg="powder blue",command=lambda:btnclick(5),font=('arial',20,'bold'),text="5").grid(row=2,column=1)
btn6=Button(cal,padx=16,pady=16,bd=8,fg="black",bg="powder blue",command=lambda:btnclick(6),font=('arial',20,'bold'),text="6").grid(row=2,column=2)
substraction=Button(cal,padx=16,pady=16,bd=8,fg="black",bg="powder blue",command=lambda:btnclick("-"),font=('arial',20,'bold'),text="-").grid(row=2,column=3)
# ........................................................................................................................
btn1=Button(cal,padx=16,pady=16,bd=8,fg="black",bg="powder blue",command=lambda:btnclick(1),font=('arial',20,'bold'),text="1").grid(row=3,column=0)

btn2=Button(cal,padx=16,pady=16,bd=8,fg="black",bg="powder blue",command=lambda:btnclick(2),font=('arial',20,'bold'),text="2").grid(row=3,column=1)

btn3=Button(cal,padx=16,pady=16,bd=8,fg="black",bg="powder blue",command=lambda:btnclick(3),font=('arial',20,'bold'),text="3").grid(row=3,column=2)
multiply=Button(cal,padx=16,pady=16,bd=8,fg="black",bg="powder blue",command=lambda:btnclick("*"),font=('arial',20,'bold'),text="*").grid(row=3,column=3)
# ........................................................................................................................
btn0=Button(cal,padx=16,pady=16,bd=8,fg="black",bg="powder blue",command=lambda:btnclick(0),font=('arial',20,'bold'),text="0").grid(row=4,column=0)

btnclear=Button(cal,padx=16,pady=16,bd=8,fg="black",command=btnClearDisplay,bg="powder blue",font=('arial',20,'bold'),text="C").grid(row=4,column=1)

btnequals=Button(cal,padx=16,pady=16,bd=8,fg="black",bg="powder blue",command=btnEqual,font=('arial',20,'bold'),text="=").grid(row=4,column=2)
division=Button(cal,padx=16,pady=16,bd=8,fg="black",command=lambda:btnclick("/"),bg="powder blue",font=('arial',20,'bold'),text="/").grid(row=4,column=3)






cal.mainloop()
