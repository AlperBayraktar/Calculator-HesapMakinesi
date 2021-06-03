from tkinter import *
from calculator import calculator

#create window
window = Tk()
window.title('Hesap Makinesi')
window.geometry('300x450')
bg = 'white'
font = ('Ligconsolata', 21)
window.configure(background=bg)

#entry for numbers (sayılar için entry)
ent_numbers = Entry(font=(font[0], 26), borderwidth=4, width=16, justify='right')
ent_numbers.place(x=0,y=0)
calculator = calculator(ent_numbers)

#buttons (butonlar)
number = 0
for row in range(3, 0, -1):
    for column in range(3):
        number += 1
        Button(text=number, font=(font[0], 21), borderwidth=2, bg=bg, width=4, height=1, command=lambda num=number: calculator.press_num(num)).place(x=column*75, y=row*75)

# operators (operatörler)
y=0
for operator in ['÷', 'x', '-', '+']:
    y+=75
    Button(text=operator, font=font, borderwidth=2, bg=bg, width=4, height=1, command=lambda x=operator: calculator.operator_press(x) ).place(x=225, y=y)

# delete, 0, . and = buttons (silme, 0, . and = butonları)
Button(text='C', font=font, borderwidth=2, bg=bg, width=4, height=1, command=calculator.delete_num).place(x=0, y=y)
Button(text='0', font=font, borderwidth=2, bg=bg, width=4, height=1, command=lambda num='0': calculator.press_num(num)).place(x=75, y=y)
Button(text='.', font=font, borderwidth=2, bg=bg, width=4, height=1, command=lambda num='.': calculator.press_num(num)).place(x=150, y=y)
Button(text='=', font=font, borderwidth=2, bg=bg, width=4, height=1, command=calculator.calculate).place(x=75, y=375)

#run app (uygulamayı çalıştır)
window.mainloop()
