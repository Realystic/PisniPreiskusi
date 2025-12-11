import sqlite3 as dbapi

pov = dbapi.connect('test.dblite')

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
    pov.commit()
    cur.close()


def dodajanje(pov, tabela, stolpci, podatki): 
        '''
        Sprejeme ime tabele, stolpcev in vrstico podatkov
        in doda podatke v tabelo
        '''
        cur = pov.cursor()
        cur.execute("""
                    INSERT INTO ?(?)
                    VALUES (?);
                    """, (tabela, stolpci, podatki))
        pov.commit()
        cur.close()



ss = {'id' : "integer PRIMARY KEY",
      'ime' : 'text NOT NULL'}


