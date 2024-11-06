import tkinter

root = tkinter.Tk()
root.title("Calculator")
root.geometry("500x700")

numbers = tkinter.Label(root,text='',font=("Arial",30),anchor="e",width =20,height=3,bg="white")
numbers.grid(row=0,columnspan=5)

operators = ['+','-','*','/','.','%']

def button_pressed(x):
    old_label_data = numbers.cget('text')
    if str(x) in operators:
        oldl_data_last_ele = old_label_data[-1]
        if oldl_data_last_ele in operators:
            new_data = list(old_label_data)
            new_data[-1] = x
            numbers.config(text=''.join(new_data))
            return True 

    new_data = str(old_label_data) + str(x)
    numbers.config(text=new_data)

def clear(x):
    if x=='C':
        numbers.config(text='')
    

def result(x):
    if x=='=':
        answer=eval(numbers.cget('text'))
        numbers.config(text=answer)

buttonlist={}    
btn = 1
for i in range(1,4): 
    for j in range(3): 
        tkinter.Button(root,text=f"{btn}",command=lambda x = btn : button_pressed(x),font=("Arial",10),width=5,height=3,bg="yellow").grid(row=i,column=j)
        btn = btn + 1 
btn = 0
for i in range(3,5):
    for j in range(1,4): 
        tkinter.Button(root,text=f"{operators[btn]}",command=lambda x = operators[btn] : button_pressed(x),font=("Arial",10),width=5,height=3,bg="yellow").grid(column=i,row=j)
        btn = btn + 1  
btn=0
last_row = ['(','0',')']

for j in range(0,3):
    tkinter.Button(root,text=f"{last_row[btn]}",command= lambda x=last_row[btn] : button_pressed(x),width=5,height=3,bg="yellow").grid(row=4,column=j)
    btn=btn +1

tkinter.Button(root,text='C',command= lambda x='C' :clear(x), width=5,height=3,bg="red").grid(row=4,column=3)
tkinter.Button(root,text='=',command= lambda x='=' :result(x), width=5,height=3,bg="green").grid(row=4,column=4)

root.mainloop()