
import api
from functools import partial
from tkinter import *

lista = api.start()

window = Tk()

Label(window, text="Wyniki porównując średnią z ostatnich 6 miesięcy:").pack()
i=0

for element in lista:
    i=i+1

    tekst =str(i)+". "+element['coin'] 
    color = "black"
    if element['mark']>0:
        tekst = tekst+" +"
        color = "green"
    if element['mark']<0:
      
        color = "red"
    
    tekst = tekst+str(element['mark'])+"%"

    Button(window, width=15, text=tekst, bg=color, fg="white", command= partial(api.get_data,element['coin'] )).pack(padx=1, pady=1)



window.mainloop()