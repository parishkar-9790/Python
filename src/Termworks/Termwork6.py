from tkinter import* 
def operate(m):
    if m=='+':
        res.set( int(num1.get())+int(num2.get()))
    elif m=='-':
        res.set( int(num1.get())-int(num2.get()))
    elif m=='*':
        res.set( int(num1.get())*int(num2.get()))
    elif m=='/':
        res.set( int(num1.get())/int(num2.get()))
    elif m=='clear':
        res.set('')
        num1.set('')
        num2.set('')
if __name__ == '__main__':
    rootWindow=Tk()
    num1=StringVar()
    num2=StringVar()
    res=StringVar()
    rootWindow.title('Calculator')
    rootWindow.geometry('640x480')
    myFirstNum=Entry(rootWindow,width=40,borderwidth=3,background='red',foreground='white',textvariable=num1)
    myFirstNum.grid(row=0,column=0,padx=40,pady=10  )
    mySecondNum=Entry(rootWindow,width=40,borderwidth=3,background='red',foreground='white',textvariable=num2)
    mySecondNum.grid(row=1,column=0,padx=40,pady=10 )
    myResult=Entry(rootWindow,width=40,borderwidth=3,background='yellow',foreground='black',textvariable=res)
    myResult.grid(row=2,column=0,padx=40,pady=10 )
    plus=Button(rootWindow, text="+",padx=40 ,pady=10,command=lambda x = '+': operate(x) )
    plus.grid(row=3,column=0)
    minus=Button(rootWindow, text="-",padx=40 ,pady=10,command=lambda x = '-': operate(x) )
    minus.grid(row=3,column=1)
    mul=Button(rootWindow, text="*",padx=40 ,pady=10,command=lambda x = '*': operate(x)  )
    mul.grid(row=4,column=0)
    div=Button(rootWindow, text="/",padx=40 ,pady=10,command=lambda x = '/': operate(x) )
    div.grid(row=4,column=1)
    Clear=Button(rootWindow, text="Clear",padx=40 ,pady=10,command=lambda x = 'clear':operate(x))
    Clear.grid(row=5,column=1)
    rootWindow.mainloop()
    