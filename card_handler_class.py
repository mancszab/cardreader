import os
import logging

'''
    Osztály definíció
'''
class card_handler:
    def __init__(self, file_name = './cards.txt'):
        """Konstruktor

            Paraméterek:
            File neve amiben a kártya számok vannak eltárolva

            Visszaadott értékek:
            Semmit nem ad vissza
        """
        self.file_name = file_name + ".txt"
        self.card_list = []
        self._cached_stamp = 0
        logging.basicConfig( level = logging.INFO, filename = file_name + '.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')
        logging.info("--- Program started ---")


    
    def read_card_file(self):
        """Megnézi, hogy van e változás a fileban, és csak akkor tölti újra, ha az időbélyegzőben talál eltérést

            Paraméterek:
            nincs bemenő paramétere

            Visszaadott értékek:
            Semmit nem ad vissza, csak a card_list osztály attribútumot befrissíti, ha szükséges
        """
        stamp = os.stat(self.file_name).st_mtime
        if stamp != self._cached_stamp:
            print(stamp)
            self._cached_stamp = stamp
            file = open(self.file_name, 'r')
            self.card_list.clear
            while True:
                line = file.readline().strip()
                if not line:
                    break
                # print(line)
                self.card_list.append(line)
            # print(self.card_list)
    

    def check_card(self, cardString):
        """ 1. megnézi, hogy van-e változás a kártyalista fileban. Ha talál, akkor újra betölti frissítve ezzel a card_list attributumot
            2. Megnézi, hogy az aktuális listában szerepel e a paraméterként kapott string

            Paraméterek:
            a keresett kártya száma stringben

            Visszaadott értékek:
            True: Talált ilyen számú kártyát
            False: Nem talált ilyen számú kártyát
        """
        self.read_card_file()
        ret_bool = False
        log_string = "Failed"
        for i in self.card_list:
            if cardString == i:
                ret_bool = True
                log_string = 'Passed'
        
        logging.info("Cardid = " + cardString + " | result = " + log_string)

        return ret_bool
    