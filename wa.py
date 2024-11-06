import tkinter

root = tkinter.Tk()
root.title("Stop watch")
root.geometry("500x700")

global seconds, minutes, hours, state
seconds=0
minutes=0
hours=0
state=0
stopwatch = tkinter.Label(root,text='00:00:00',font=("Arial",30),justify=("center"),width =15,height=10)
stopwatch.pack()

def start(state,seconds):
      global x, minutes, hours
      pause_button.config(state=tkinter.NORMAL)
      if state==1:
         root.after_cancel(x)
         pause_button.config(state=tkinter.DISABLED) 
      start_button.config(state=tkinter.DISABLED)   
      old_data = stopwatch.cget('text')
      new_data  = old_data.split(':')
      minutes = int(new_data[1])
      hours = int(new_data[0])
      seconds +=1
      if seconds == 60:
         seconds =0
         minutes +=1
      if minutes ==60:
         minutes =0
         hours +=1
      global s
      s= seconds
      global result_data 
      result_data=[str(hours),str(minutes),str(seconds)]
      stopwatch.config(text=':'.join(result_data))
      if state==2:
         start_button.config(state=tkinter.NORMAL)
         root.after_cancel(x)
         stopwatch.config(text='00:00:00')        
      if state==0:
         x=root.after(1000,start,state,seconds)
      return seconds

start_button= tkinter.Button(root,text=f"Start",command= lambda state = 0 : start(state,seconds),font=("Arial",10),width=5,height=3)
start_button.pack()

pause_button= tkinter.Button(root,text=f"Pause",command =lambda state = 1 : start(state,seconds=s), font=("Arial",10),width=5,height=3)
pause_button.pack()
   
reset_button = tkinter.Button(root,text=f"Reset",command= lambda state = 2 : start(state,seconds),font=("Arial",10),width=5,height=3)
reset_button.pack()
print(seconds)
root.mainloop()