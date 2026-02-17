import sqlite3

#SQL ukazi za ustvarjanje tabel
"""spremenjeno od 1.0: 
odstranjen je bil stolpec nosilec iz tabele predmeti in pa kapaciteta iz predavalnic - to se zdita manj pomembna podatka v kontekstu projktne naloge.
Prav tako je bil odstranjen stolpec teme iz tabele pisniPreiskusi, ker se teme povezujejo s testi preko povezovalne
tabele p, kar omogoča več tem na en test. 
Dodal CASCADE na vse tuje ključe, da se ob brisanju ali posodabljanju vrednosti v primarni tabeli, 
ustrezno posodobijo ali izbrišejo povezane vrstice v odvisnih tabelah."""

letniki = """
CREATE TABLE IF NOT EXISTS letniki (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    letnik TEXT NOT NULL UNIQUE
);
"""

predmeti = """
CREATE TABLE IF NOT EXISTS predmeti (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ime TEXT NOT NULL,
    id_letnik INTEGER NOT NULL,
    FOREIGN KEY (id_letnik) REFERENCES letniki(id)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);
"""

teme = """
CREATE TABLE IF NOT EXISTS teme (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tema TEXT NOT NULL UNIQUE,
    id_predmet INTEGER NOT NULL,
    FOREIGN KEY (id_predmet) REFERENCES predmeti(id)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);
"""

predavalnice= """
CREATE TABLE IF NOT EXISTS predavalnice (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ime TEXT NOT NULL,
    kapaciteta INTEGER
);
"""

tipi = """
CREATE TABLE IF NOT EXISTS tip_testa (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tip TEXT UNIQUE NOT NULL
);
"""

pisniPreiskusi = """
CREATE TABLE IF NOT EXISTS pisniPreiskus (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    datum DATETIME,
    id_predavalnica INTEGER,
    id_letnik INTEGER,
    id_predmet INTEGER,
    id_tip INTEGER,
    FOREIGN KEY (id_predavalnica) REFERENCES predavalnice(id)
        ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (id_letnik) REFERENCES letniki(id)
        ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (id_predmet) REFERENCES predmeti(id)
        ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (id_tip) REFERENCES tip_testa(id)
        ON UPDATE CASCADE ON DELETE CASCADE
);
"""

povezvovalna = """
CREATE TABLE IF NOT EXISTS povezovalna_teme_testi (
    id_teme INTEGER NOT NULL,
    id_test INTEGER NOT NULL,
    PRIMARY KEY (id_teme, id_test),
    FOREIGN KEY (id_teme) REFERENCES teme(id) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (id_test) REFERENCES pisniPreiskus(id) ON UPDATE CASCADE ON DELETE CASCADE
);
"""

def ustvariTabelo(pot, sql_ukaz):
    """Funkcija, ki izvrši sql ukaz za dano pot do baze."""
    with sqlite3.connect(pot) as pov:
        pov.execute("PRAGMA foreign_keys = ON;")
        kaz = pov.cursor()
        kaz.execute(sql_ukaz)

pot = "izpiti.sqlite"

sql_ukazi = [
    letniki,
    predmeti,
    teme,
    predavalnice,
    tipi,
    pisniPreiskusi,
    povezvovalna
]

for ukaz in sql_ukazi:
    ustvariTabelo(pot, ukaz)