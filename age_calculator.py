
from tkinter import *
import tkinter.messagebox as tmsg
root=Tk()
root.geometry('400x400')

My_age=''
def click(event):
    global My_age
    from datetime import date
    today=date.today()
    year_today=(today.year)
    months_today=(today.month)
    day_today=(today.day)
    r_year=year_today-int(year.get())
    r_months=months_today-int(months.get())
    r_days=day_today-int(day.get())
    My_age=r_year
    age.config(text=f'Your Are {My_age} years old')
    if int(day.get())>31:
        tmsg.showinfo('Error', 'You Entered Beyond Limit')
    
    elif int(months.get())>12:
        tmsg.showinfo('Error','You Entered Beyond Limit')
    
        

    

name=StringVar()
year=StringVar()
months=StringVar()
day=StringVar()
result=StringVar()
result.set('')
f1=Frame(root,pady=10)
f1.grid()
Label(f1,text='Age Calculator',font='cooperblack 20 bold',pady=10).grid(row=0,column=3)
Label(f1,text='Name:',font='lucida 19 bold').grid(row=1)
Label(f1,text='Year:',font='lucida 19 bold').grid(row=2)
Label(f1,text='Month:',font='lucida 19 bold').grid(row=3)
Label(f1,text='Day:',font='lucida 19 bold').grid(row=4)
Entry(f1,textvariable=name,font='lucida 19').grid(row=1,column=3)
Entry(f1,textvariable=year,font='lucida 19').grid(row=2,column=3)
Entry(f1,textvariable=months,font='lucida 19').grid(row=3,column=3)
Entry(f1,textvariable=day,font='lucida 19').grid(row=4,column=3)
b=Button(f1,text='Calculate Age',font='lucida 19')
b.bind('<Button-1>',click)
b.grid(row=5,column=3)
age=Label(text=My_age,font='lucida 19')
age.grid()









root.mainloop()