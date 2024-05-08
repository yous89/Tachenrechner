import tkinter as tk

calculations = 'Addition'
def callback (selection):
    global calculations
    calculations = selection

def calculte ():
    global calculations
    val1 = 0 if not entry1.get() else float(entry1.get())
    val2= 0 if not entry2.get() else float(entry2.get())

    if calculations == "Addition" :
        output.config (text = val1+val2)
    elif calculations == "Subtraktion" :
        output.config(text= val1 - val2)
    elif calculations == "Multiplikation" :
        output.config(text= val1 * val2)
    elif calculations == "Division" :
        try:
            output.config(text=val1 / val2)
        except ZeroDivisionError :
            output.config (text='kann nicht durch Null teilen ')




window= tk.Tk()
window.geometry("800x500")

optionlist = ["Addition","Subtraktion","Multiplikation","Division"]

variable = tk.StringVar(window)
variable.set(optionlist[0])

opt = tk.OptionMenu (window,variable,*optionlist,command=callback)
opt.config(font=('Helvetica' , 12 ))
opt.grid(row=0,column=0)

entry1=tk.Entry(window)
entry1.grid(row=0,column=1)


entry2=tk.Entry(window)
entry2.grid(row=0,column=2)

button = tk.Button(window, text="berechnen", command=calculte)
button.grid(row=1,column=0)

output=tk.Label(window)
output.grid(row=2)

window.mainloop()


