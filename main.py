import tkinter as tk
from tkinter.constants import CENTER
from tkinter.font import Font
#from typing import Collection

expression = ""
input_pertama = True

def input_number(number,equation):
    global expression
    global input_pertama

    strnumber = str(number)
    if strnumber != "" :
        #Stlh evaluate, kalau input angka maka hasil sebelumnya dihapus
        varangka = '0123456789.'
        if (input_pertama) and (varangka.find(strnumber) >= 0):
            expression = ""
                
    expression += strnumber
    equation.set(expression)
    if expression != '' : input_pertama = False

def clear_input(equation):
    global expression
    global input_pertama

    expression = ""
    equation.set("0")
    input_pertama = True

def evaluate(equation):
    global expression
    global input_pertama

    try:
        result=str(eval(expression))
        equation.set(result)
        expression=result
    except:
        expression=""
        equation.set("Error !!!")
    input_pertama = True

def main():
    def display_btninput(vteks, vnumber, vcol, vrow):
        btn = tk.Button(window, text=vteks, fg='white',bg='purple',bd=1,command=lambda:input_number(vnumber,equation),height=2,width=7)
        btn.grid(column=vcol, row=vrow, padx=1, pady=1)
        
    def cekKey(event):
        global expression
        #print(event)
        vkey = event.char
        allowchar = "0123456789.+-x:%^"
        if (vkey != "") and (allowchar.find(vkey) >= 0) :
            if vkey == ':':
                vkey = '/'
            elif vkey == 'x':
                vkey = '*'
            elif vkey == '%':
                vkey = '/100'
            elif vkey == '^':
                vkey = '**'           
            input_number(vkey, equation) 
        elif vkey == '\r': #Enter
            evaluate(equation)   
        elif vkey == '\x08': #Backspace
            if len(expression) <= 1:
                expression = ""
                equation.set("0")
            else:
                expression = expression[0 : len(expression)-1] 
                equation.set(expression)



    window = tk.Tk()
    window.title("Calculator")
    window.geometry("240x240")
    window.resizable(False, False)
    window.bind('<Key>', cekKey)
    equation = tk.StringVar()

    input_field= tk.Entry(window, textvariable=equation,bg='yellow',font=("comic sans",10,"bold"), width=32)
#    input_field.place()
    input_field.grid(column=0, columnspan=4, ipadx=5, ipady=5, padx=1, pady=1)
    equation.set("0")
    
       
#    n0=tkinter.Button(window,text='0',fg='white',bg='purple',bd=1,command=lambda:input_number(0,equation),height=2,width=7)
#    n0.grid(row=5,column=0, padx=1, pady=1)  
#    n1=tkinter.Button(window,text='1',fg='white',bg='purple',bd=1,command=lambda:input_number(1,equation),height=2,width=7)
#    n1.grid(row=4,column=0, padx=1, pady=1)
#    n2=tkinter.Button(window,text='2',fg='white',bg='purple',bd=1,command=lambda:input_number(2,equation),height=2,width=7)
#    n2.grid(row=4,column=1, padx=1, pady=1)
#    n3=tkinter.Button(window,text='3',fg='white',bg='purple',bd=1,command=lambda:input_number(3,equation),height=2,width=7)
#    n3.grid(row=4,column=2, padx=1, pady=1)
#    n4=tkinter.Button(window,text='4',fg='white',bg='purple',bd=1,command=lambda:input_number(4,equation),height=2,width=7)
#    n4.grid(row=3,column=0, padx=1, pady=1)
#    n5=tkinter.Button(window,text='5',fg='white',bg='purple',bd=1,command=lambda:input_number(5,equation),height=2,width=7)
#    n5.grid(row=3,column=1, padx=1, pady=1)
#    n6=tkinter.Button(window,text='6',fg='white',bg='purple',bd=1,command=lambda:input_number(6,equation),height=2,width=7)
#    n6.grid(row=3,column=2, padx=1, pady=1)
#    n7=tkinter.Button(window,text='7',fg='white',bg='purple',bd=1,command=lambda:input_number(7,equation),height=2,width=7)
#    n7.grid(row=2,column=0, padx=1, pady=1)
#    n8=tkinter.Button(window,text='8',fg='white',bg='purple',bd=1,command=lambda:input_number(8,equation),height=2,width=7)
#    n8.grid(row=2,column=1, padx=1, pady=1)
#    n9=tkinter.Button(window,text='9',fg='white',bg='purple',bd=1,command=lambda:input_number(9,equation),height=2,width=7)
#    n9.grid(row=2,column=2, padx=1, pady=1)

    display_btninput('0', 0, 0, 5)
    display_btninput('1', 1, 0, 4)
    display_btninput('2', 2, 1, 4)
    display_btninput('3', 3, 2, 4)
    display_btninput('4', 4, 0, 3)
    display_btninput('5', 5, 1, 3)
    display_btninput('6', 6, 2, 3)
    display_btninput('7', 7, 0, 2)
    display_btninput('8', 8, 1, 2)
    display_btninput('9', 9, 2, 2)

#    dot=tkinter.Button(window,text='.',fg='white',bg='purple',bd=1,command=lambda:input_number('.',equation),height=2,width=7)
#    dot.grid(row=5,column=1, padx=1, pady=1)
#    plus=tkinter.Button(window,text='+',fg='white',bg='purple',bd=1,command=lambda:input_number('+',equation),height=2,width=7)
#    plus.grid(row=2,column=3, padx=1, pady=1)
#    minus=tkinter.Button(window,text='-',fg='white',bg='purple',bd=1,command=lambda:input_number('-',equation),height=2,width=7)
#    minus.grid(row=3,column=3, padx=1, pady=1)
#    multiply=tkinter.Button(window,text='x',fg='white',bg='purple',bd=1,command=lambda:input_number('*',equation),height=2,width=7)
#    multiply.grid(row=4,column=3, padx=1, pady=1)
#    devide=tkinter.Button(window,text='/',fg='white',bg='purple',bd=1,command=lambda:input_number('/',equation),height=2,width=7)
#    devide.grid(row=5,column=3, padx=1, pady=1)
#    percent=tkinter.Button(window,text='%',fg='white',bg='purple',bd=1,command=lambda:input_number('/100*',equation),height=2,width=7)
#    percent.grid(row=6,column=0, padx=1, pady=1)
#    power=tkinter.Button(window,text='^',fg='white',bg='purple',bd=1,command=lambda:input_number('**',equation),height=2,width=7)
#    power.grid(row=6,column=3, padx=1, pady=1)

    display_btninput('.', '.', 1, 5)
    display_btninput('+', '+', 3, 2)
    display_btninput('-', '-', 3, 3)
    display_btninput('x', '*', 3, 4)
    display_btninput(':', '/', 3, 5)
    display_btninput('%', '/100', 0, 6)
    display_btninput('^', '**', 3, 6)


    clear=tk.Button(window,text='Clear',fg='white',bg='purple',bd=1,command=lambda:clear_input(equation),height=2,width=7)
    clear.grid(row=5,column=2, padx=1, pady=1)

    equal=tk.Button(window,text='=',fg='white',bg='purple',bd=1,command=lambda:evaluate(equation),height=2,width=15)
    equal.grid(row=6,columnspan=4, padx=1, pady=1)

    window.mainloop()

if __name__=='__main__':
    main()
