import tkinter.messagebox as msg_box

class calculator:
    def __init__(self, entry):
        #? get entry for displaying numbers and create a variable to know is calculation finished
        #? sayıları göstermek için ve hesaplama işlemini bitip bitmediğini gösteren bir değişken yarat
        self.entry, self.did_calculate = entry, False
    
    def press_num(self, number):
        #* if calculated delete refresh the entry
        #* eğer hesaplama yapılmışsa entry'i sıfırla
        if self.did_calculate:
            self.entry.delete(0, 'end')
            self.did_calculate = False
        
        #* write the number  (sayıyı yazdır)
        self.entry.insert('end', str(number))
    
    def delete_num(self):
        #? remove the last number (son sayıyı sil)
        self.entry.delete(len(self.entry.get())-1, 'end')

    def operator_press(self, operator):
        #* get the first number and control if its not valid
        #* ilk sayıyı al ve uygun mu kontrol et
        try:
            self.first_num = float(self.entry.get())
        except:
            msg_box.showerror('Error', 'Please insert a valid number.')
            return None

        #* get the operator and refresh the entry for user to enter the second number
        #* operatörü al ve entry'i ikinci sayının girilmesi için sil
        self.operator = operator
        self.entry.delete(0, 'end')
    
    def calculate(self):
        #* get second number and control if its not valid
        #* ikinci sayıyı al ve uygun mu kontrol et
        try:
            self.second_num = float(self.entry.get())
        except:
            msg_box.showerror('Error', 'Please insert a valid number.')
            return None
        
        #* refresh the entry and display the result
        #* entryi temizle ve sonucu yansıt

        self.entry.delete(0, 'end')
        try:
            if self.operator == '+':
                self.entry.insert(0, str( self.first_num + self.second_num ))
            elif self.operator == '-':
                self.entry.insert(0, str( self.first_num - self.second_num ))
            elif self.operator == 'x':
                self.entry.insert(0, str( self.first_num * self.second_num ))
            elif self.operator == '÷':
                self.entry.insert(0, str( self.first_num / self.second_num ))
        except ZeroDivisionError:
            self.entry.insert(0, 'Cannot divide by 0')


        self.did_calculate = True
