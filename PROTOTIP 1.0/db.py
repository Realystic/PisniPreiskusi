import sqlite3

POT = "PROTOTIP 1.0\\izpiti.sqlite"

def povezava():
    pov = sqlite3.connect(POT)
    pov.execute("PRAGMA foreign_keys = ON;")
    return pov

#funkcije za dodajanje, brisanje in pregled letnikov
def dodaj_letnik(letnik):
    """Doda argument v tabelo letnik (z velikmi črkamoi)."""
    with povezava() as pov:
        kaz = pov.cursor()
        kaz.execute("""
            INSERT INTO letniki (letnik)
            VALUES (?)
        """, (letnik,))

def prikazi_letnike():
    """Prikaže letnike v tabeli letniki, urejene po abecedi."""
    with povezava() as pov:
        kaz = pov.cursor()
        kaz.execute("""
            SELECT id, letnik
            FROM letniki
            ORDER BY letnik ASC
        """)
        podatki = kaz.fetchall()
    return podatki

def izbrisi_letnik(id_letnik):
    """Izbriše letnik iz tabele letniki glede na id letnika."""
    with povezava() as pov:
        kaz = pov.cursor()
        kaz.execute("""
            DELETE FROM letniki
            WHERE id = ?
        """, (id_letnik,))

#funkcije za dodajanje, brisanje in pregled predmetov
def dodaj_predmet(predmet, nosilec=None):
    """Doda argument v tabelo predmet."""
    with povezava() as pov:
        kaz = pov.cursor()
        kaz.execute("""
            INSERT INTO predmeti (ime, nosilec)
            VALUES (?, ?)
        """, (predmet, nosilec))

def prikazi_predmete():
    """Prikaže predmete v tabeli predmet, urejene po abecedi."""
    with povezava() as pov:
        kaz = pov.cursor()
        kaz.execute("""
            SELECT id, ime, nosilec
            FROM predmeti
            ORDER BY ime ASC
        """)
        podatki = kaz.fetchall()
    return podatki

def izbrisi_predmet(id_predmet):
    """Izbriše predmet iz tabele predmeti glede na ID."""
    with povezava() as pov:
        kaz = pov.cursor()
        kaz.execute("""
            DELETE FROM predmeti
            WHERE id = ?
        """, (id_predmet,))


#funkcije za dodajanje, brisanje in pregled predavalnic
def dodaj_predavalnico(ime, kapaciteta = None): 
    """Doda argument v tabelo predavalnice."""
    with povezava() as pov:
        kaz = pov.cursor()
        kaz.execute("""
            INSERT INTO predavalnice (ime, kapaciteta)
            VALUES (?, ?)
        """, (ime, kapaciteta))

def prikazi_predavalnice():
    """Prikaže predavalnice v tabeli predavalnice, urejene po abecedi."""
    with povezava() as pov:
        kaz = pov.cursor()
        kaz.execute("""
            SELECT id, ime, kapaciteta
            FROM predavalnice
            ORDER BY ime ASC
        """)
        podatki = kaz.fetchall()
    return podatki

def izbrisi_predavalnico(id_predavalnica):
    """Izbriše predavalnico iz tabele predavalnice glede na id predavalnice."""
    with povezava() as pov:
        kaz = pov.cursor()
        kaz.execute("""
            DELETE FROM predavalnice
            WHERE id = ?
        """, (id_predavalnica,))

#Funkcije za dodajanje, brisanje in pregled tipov testov
def dodaj_tip_testa(tip):
    """Doda argument v tabelo tip_testa."""
    with povezava() as pov:
        kaz = pov.cursor()
        kaz.execute("""
            INSERT INTO tip_testa (tip)
            VALUES (?)
        """, (tip,))

def prikazi_tipe_testov():
    """Prikaže tipe testov v tabeli tip_testa, urejene po abecedi."""
    with povezava() as pov:
        kaz = pov.cursor()
        kaz.execute("""
            SELECT id, tip
            FROM tip_testa
            ORDER BY tip ASC
        """)
        podatki = kaz.fetchall()
    return podatki

def izbrisi_tip_testa(id_tip):
    """Izbriše tip testa iz tabele tip_testa glede na id tipa."""
    with povezava() as pov:
        kaz = pov.cursor()
        kaz.execute("""
            DELETE FROM tip_testa
            WHERE id = ?
        """, (id_tip,))


#funkcije za dodajanje, brisanje in pregled tem
def dodaj_temo(tema):
    """Doda argument v tabelo teme."""
    with povezava() as pov:
        kaz = pov.cursor()
        kaz.execute("""
            INSERT INTO teme (tema)
            VALUES (?)
        """, (tema,))

def prikazi_teme():
    """Prikaže teme v tabeli teme, urejene po abecedi."""
    with povezava() as pov:
        kaz = pov.cursor()
        kaz.execute("""
            SELECT id, tema
            FROM teme
            ORDER BY tema ASC
        """)
        podatki = kaz.fetchall()
    return podatki

def izbrisi_temo(id_tema):
    """Izbriše temo iz tabele teme glede na id teme."""
    with povezava() as pov:
        kaz = pov.cursor()
        kaz.execute("""
            DELETE FROM teme
            WHERE id = ?
        """, (id_tema,))