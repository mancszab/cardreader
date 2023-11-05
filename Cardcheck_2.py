""" Kartyak jogosultsaganak ellenorzese, es loggolas """
""" V1.2 vegtelen ciklussal, tranzisztoros bemenet inditassal felugro ablakokkal """

from datetime import datetime   #meghivja a hasznalt fuggvenyeket
from gpiozero import LED, Button, OutputDevice
from gpiozero.tools import booleanized, all_values
import time

from card_handler_class import card_handler
# from time import sleep
# from signal import pause
# import automationhat
# from tkinter import Tk, simpledialog,messagebox
# from Tkinter import Tk
# import tkinter

#automationhat.output.one.off()
#automationhat.output.two.off()

cardList = []

ch = card_handler('./cards.txt')

def logging (card):
        with open('log.txt','a') as f:
            f.write ('\n' + card + '/' + date_time)  # logolja a kartyaszamot datummal

while True:
    
    date_time = datetime.now().strftime("%Y-%m-%d, %H:%M:%S")   # datumot, idot atkonvertalja magyarra

    
    olvasott_kartya = input ('Kerem a Kartyat')
    print('*' + olvasott_kartya + '*')

    print(ch.check_card(olvasott_kartya))


        
                   

