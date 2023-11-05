""" Kartyak jogosultsaganak ellenorzese, es loggolas """
""" V1.2 vegtelen ciklussal, tranzisztoros bemenet inditassal felugro ablakokkal """

from datetime import datetime   #meghivja a hasznalt fuggvenyeket
from gpiozero import LED, Button, OutputDevice
from gpiozero.tools import booleanized, all_values
import time

import card_handler_class


# from time import sleep
# from signal import pause
# import automationhat
# from tkinter import Tk, simpledialog,messagebox
# from Tkinter import Tk
# import tkinter

#automationhat.output.one.off()
#automationhat.output.two.off()

def card_check ():
        with open('cards.txt') as kartyak:  # megnyitja a cards txt-t
            for sor in kartyak:
                sor = sor.rstrip('\n')
                kartya[sor]=sor
            
def logging (card):
        with open('log.txt','a') as f:
            f.write ('\n' + card + '/' + date_time)  # logolja a kartyaszamot datummal


ch = card_handler_class('./cards.txt')

while True:
    
    dt = datetime.now ()
    date_time = dt.strftime("%Y-%m-%d, %H:%M:%S")   # datumot, idot atkonvertalja magyarra
    
    if automationhat.input.one.is_on():
     
  #      root=Tk()       # albakot hoz letre

        olvasott_kartya = input ('Kerem a Kartyat')
        
  #      root.withdraw() # eltunteti az ablakot
          
        kartya={}       # a valtozoba beleteszi az engedelyezett kartyaszamokat

        card_check()    # megnyitja a kartyaellenorzo fuggvenyt

        
     #   olvasott_kartya = simpledialog.askstring('sor','Kerem a Kartyat')

   
        if olvasott_kartya in kartya:
            # messagebox.showinfo('Kartya OK',
            #                   'Kartya elfogadva')
            logging(olvasott_kartya)       # megnyitja a kartyalogolo fuggvenyt
            #automationhat.output.one.on()
            time.sleep(5)
            #automationhat.output.one.off()
            
        
        else: 
            # print('Kartya elutasitva')
            #automationhat.output.two.on()
            time.sleep(5)
            #automationhat.output.two.off()
                   

