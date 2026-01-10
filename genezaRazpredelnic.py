import sqlite3

#SQL ukazi za ustvarjanje tabel
letnik = """
CREATE TABLE IF NOT EXISTS letnik (
    id INTEGER PRIMARY KEY AUTOINCREMENT
);
"""

predmeti = """
CREATE TABLE IF NOT EXISTS predmeti (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ime TEXT NOT NULL,
    nosilec TEXT
);
"""

teme = """
CREATE TABLE IF NOT EXISTS teme (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tema TEXT NOT NULL
    );
"""

predavalnice= """
CREATE TABLE IF NOT EXISTS predavalnice (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ime TEXT,
    kapaciteta INTEGER
);
"""

tip = """
CREATE TABLE IF NOT EXISTS tip_testa (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tip TEXT
);
"""

pisniPreiskus = """
CREATE TABLE IF NOT EXISTS pisniPreiskus (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    datum DATETIME,
    teme INTEGER,
    predavalnica INTEGER,
    smer INTEGER,
    predmet INTEGER,
    tip INTEGER,
    FOREIGN KEY (teme) REFERENCES teme(id) ON UPDATE NO ACTION ON DELETE NO ACTION,
    FOREIGN KEY (predavalnica) REFERENCES predavalnice(id) ON UPDATE NO ACTION ON DELETE NO ACTION,
    FOREIGN KEY (smer) REFERENCES letnik(id) ON UPDATE NO ACTION ON DELETE NO ACTION,
    FOREIGN KEY (predmet) REFERENCES predmeti(id) ON UPDATE NO ACTION ON DELETE NO ACTION,
    FOREIGN KEY (tip) REFERENCES tip_testa(id) ON UPDATE NO ACTION ON DELETE NO ACTION
);
"""

povezvovalna = """
CREATE TABLE IF NOT EXISTS povezovalna_teme_testi (
    id_teme INTEGER NOT NULL,
    id_test INTEGER NOT NULL,
    PRIMARY KEY (id_teme, id_test),
    FOREIGN KEY (id_teme) REFERENCES teme(id) ON UPDATE NO ACTION ON DELETE NO ACTION,
    FOREIGN KEY (id_test) REFERENCES pisniPreiskus(id) ON UPDATE NO ACTION ON DELETE NO ACTION
);
"""

def ustvariTabelo(pot, sql_ukaz):
    """Funkcija, ki izvrši sql ukaz za dano pot do baze."""
    with sqlite3.connect(pot) as pov:
        pov.execute("PRAGMA foreign_keys = ON;")
        kaz = pov.cursor()
        kaz.execute(sql_ukaz)

sql_ukazi = [
    letnik,
    predmeti,
    teme,
    predavalnice,
    tip,
    pisniPreiskus,
    povezvovalna
]

pot = "izpiti.sqlite"


for ukaz in sql_ukazi:
    ustvariTabelo(pot, ukaz)

