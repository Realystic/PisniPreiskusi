import sqlite3 as dbapi

conn = dbapi.connect('pisnipreizkus.sqlite')
cur = conn.cursor()


class BazaPP():

    def __init__():
        '''Inicializira bazo'''
        return

    # Pisni Preizkus
    
    # letnik
    # teme
    # predmeti
    # predavalnice
    # tip testa
    # povezovalna tema-testi

class Tabela:
    """Osnovni template Tabele na katero bodo navezane druge
     tabele v projektu (bodo podrazredi razreda Tabela)"""
    
    ime = None
    podatki = None

    def __init__(self, conn):
        '''Konstruktor razreda'''
        self.conn = conn

#    @classmethod
#    def ustvari(self):
    
    @classmethod
    def izbrisi(self):
        '''Izbriše tabelo'''
        self.conn.execute(f"DROP TABLE IF EXISTS {self.ime};")
    
#    @classmethod
#    def uvozi(self):

    @classmethod
    def izprazni(self):
        '''Pobriše podatke iz tabele'''
        self.conn.execute(f'DELETE FROM {self.ime};')
    
    @classmethod
    def dodajanje(self, podatki): 
        '''
        Sprejeme podatke in jih doda v tabelo,
        v obliki sezama
        '''
        self.conn.execute("""
                          INSERT INTO ? ()
                          VALUES ()
                          """, (self.ime))
        




def ustvariTab(pov, imeTab, slovStolp):
    cur = pov.cursor()
    niz = ''

    # razpakiramo slovar stoplcev v niz
    for ime, pogoji in slovStolp.items():
        niz += f'{ime} {pogoji},'
    niz = niz.rstrip(',')
        

    cur.execute("""
                CREATE TABLE ? (
                ?);
                """, (imeTab, niz))


def dodajanje(tabela, stolpci, podatki, povezava): 
        '''
        Sprejeme ime tabele, stolpcev in vrstico podatkov
        in doda podatke v tabelo
        '''
        cur = povezava.cursor()
        cur.execute("""
                    INSERT INTO ?(?)
                    VALUES (?);
                    """, (tabela, stolpci, podatki))
        povezava.commit()
        cur.close()
