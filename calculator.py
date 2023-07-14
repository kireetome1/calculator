# -*- coding: utf-8 -*-
"""
Created on Wed May 31 11:27:21 2023

@author: new-kensyu
"""

from tkinter import Tk, Button, Entry, END
import math

class Calc:
    def getandreplace(self):  # replace x, + and % to symbols that can be used in calculations
        # we wont re write this to the text box until we are done with calculations

        self.txt = self.e.get() # Get value from text box and assign it to the global txt var
        self.txt = self.txt.replace('÷', '/')
        self.txt = self.txt.replace('x', '*')
        self.txt = self.txt.replace('%', '/100')

    def evaluation(self, specfunc):  # Evaluate the items in the text box for calculation specfunc = eq, sqroot or power
        self.getandreplace()
        try:
            self.txt = eval(str(self.txt))  # evaluate the expression using the eval function
        except SyntaxError:
            self.displayinvalid()
        else:
            if any([specfunc == 'sqroot', specfunc == 'power', specfunc == 'fact',specfunc == 'pi']):  # Square Root and Power are special
                self.txt = self.evalspecialfunctions(specfunc)

            self.refreshtext()

    def displayinvalid(self):
        self.e.delete(0, END)
        self.e.insert(0, 'Invalid Input!')

    def refreshtext(self):  # Delete current contents of textbox and replace with our completed evaluatioin
        self.e.delete(0, END)
        self.e.insert(0, self.txt)

    def evalspecialfunctions(self, specfunc):  # Calculate square root and power if specfunc is sqroot or power
        if specfunc == 'sqroot':
            return math.sqrt(float(self.txt))
        elif specfunc == 'power':
            return math.pow(float(self.txt), 2)
        elif specfunc == 'fact' :
            return math.factorial(float(self.txt))
        elif specfunc == 'pi':
            return math.pi

    def clearall(self): # AC button pressed on form or 'esc" pressed on keyboard
        self.e.delete(0, END)
        self.e.insert(0, '0')

    def clear1(self):
        # C button press on form or backspace press on keyboard event defined on keyboard press
        self.txt = self.e.get()[:-1]

#        if event is None:
#            self.txt = self.e.get()[:-1]  # Form backspace done by hand
#        else:
#            self.txt = self.getvalue()  # No need to manually delete when done from keyboard

#            self.refreshtext()


    def action(self, argi: object):  # Number or operator button pressed on form and passed in as argi
        self.txt = self.getvalue()

        self.stripfirstchar()

        self.e.insert(END, argi)

    def keyaction(self, event=None):  # Key pressed on keyboard which defines event
        self.txt = self.getvalue()

        if event.char.isdigit():
            self.stripfirstchar()
        elif event.char in '/*-+%().':
            self.stripfirstchar()
        elif event.char == '\x08':
            self.clear1(event)
        elif event.char == '\x1b':
            self.clearall()
        elif event.char == '\r':
            self.evaluation('eq')
        else:
            self.displayinvalid()
            return 'break'

    def stripfirstchar(self):  # Strips leading 0 from text box with first key or button is pressed
        if self.txt[0] == '0':
            self.e.delete(0, 1)

    def getvalue(self):  # Returns value of the text box
        return self.e.get()

    def __init__(self, master):  # Constructor method
        self.txt = 'o'  # Global var to work with text box contents
        master.title('Calulator')
        master.geometry()
        self.e = Entry(master)
        self.e.grid(row=0, column=0, columnspan=6, rowspan=1,ipadx=120,ipady=30)
        self.e.insert(0, '0')
        self.e.focus_set()  # Sets focus on the text box text area

        # Generating Buttons
        Button(master, text="=", width=20, height=5 ,font=('arial black', 10,'bold'),bg='orange', command=lambda: self.evaluation('eq')).grid(row=8, column=4, columnspan=2)
        Button(master, text='AC', width=10, height=5,font=('arial black', 10,'bold'),bg='light pink', command=lambda: self.clearall()).grid(row=5, column=4)
        Button(master, text='C', width=10, height=5 ,font=('arial black', 10,'bold'),bg='light pink', command=lambda : self.clearall()).grid(row=5, column=5)
        Button(master, text="+", width=10, height=5 ,font=('arial black', 10,'bold'),bg='red', command=lambda: self.action('+')).grid(row=8, column=3)
        Button(master, text="x", width=10, height=5 ,font=('arial black', 10,'bold'),bg='red', command=lambda: self.action('x')).grid(row=6, column=3)
        Button(master, text="-", width=10, height=5 ,font=('arial black', 10,'bold'),bg='red', command=lambda: self.action('-')).grid(row=7, column=3)
        Button(master, text="÷", width=10, height=5 ,font=('arial black', 10,'bold'),bg='red', command=lambda: self.action('÷')).grid(row=5, column=3)
        Button(master, text="%", width=10, height=5 ,font=('arial black', 10,'bold'),bg='green', command=lambda: self.action('%')).grid(row=8, column=2)
        Button(master, text="7", width=10, height=5 ,font=('arial black', 10,'bold'), command=lambda: self.action('7')).grid(row=5, column=0)
        Button(master, text="8", width=10, height=5 ,font=('arial black', 10,'bold'), command=lambda: self.action('8')).grid(row=5, column=1)
        Button(master, text="9", width=10, height=5 ,font=('arial black', 10,'bold'), command=lambda: self.action('9')).grid(row=5, column=2)
        Button(master, text="4", width=10, height=5 ,font=('arial black', 10,'bold'), command=lambda: self.action('4')).grid(row=6, column=0)
        Button(master, text="5", width=10, height=5 ,font=('arial black', 10,'bold'), command=lambda: self.action('5')).grid(row=6, column=1)
        Button(master, text="6", width=10, height=5 ,font=('arial black', 10,'bold'), command=lambda: self.action('6')).grid(row=6, column=2)
        Button(master, text="1", width=10, height=5 ,font=('arial black', 10,'bold'), command=lambda: self.action('1')).grid(row=7, column=0)
        Button(master, text="2", width=10, height=5 ,font=('arial black', 10,'bold'), command=lambda: self.action('2')).grid(row=7, column=1)
        Button(master, text="3", width=10, height=5 ,font=('arial black', 10,'bold'), command=lambda: self.action('3')).grid(row=7, column=2)
        Button(master, text="0", width=10, height=5 ,font=('arial black', 10,'bold'), command=lambda: self.action('0')).grid(row=8, column=0)
        Button(master, text=".", width=10, height=5 ,font=('arial black', 10,'bold'),bg='magenta', command=lambda: self.action('.')).grid(row=8, column=1)
        Button(master, text="√", width=10, height=5 ,font=('arial black', 10,'bold'),bg='green', command=lambda: self.evaluation('sqroot')).grid(row=6, column=4)
        Button(master, text="x²", width=10, height=5 ,font=('arial black', 10,'bold'),bg='green',command=lambda: self.evaluation('power')).grid(row=6, column=5)
        Button(master, text="!", width=10, height=5 ,font=('arial black', 10,'bold'),bg='green', command=lambda: self.evaluation('fact')).grid(row=7, column=5)
        Button(master, text="𝝅", width=10, height=5 ,font=('arial black', 10,'bold'),bg='green', command=lambda: self.evaluation('pi')).grid(row=7, column=4)

        # bind key strokes
        self.e.bind('<Key>', lambda evt: self.keyaction(evt))


# Main
root = Tk()
obj = Calc(root)  # object instantiated
root.mainloop()