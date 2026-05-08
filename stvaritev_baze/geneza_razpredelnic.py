import os
import sqlite3

#SQL ukazi za ustvarjanje tabel (inicializacija baze)
"""spremenjeno od 1.0: 
odstranjen je bil stolpec nosilec iz tabele predmeti in pa kapaciteta iz predavalnic - to se zdita manj pomembna podatka v kontekstu projktne naloge.
Prav tako je bil odstranjen stolpec teme iz tabele pisni_preizkusi, ker se teme povezujejo s testi preko povezovalne
tabele p, kar omogoča več tem na en test. 
Dodal CASCADE na vse tuje ključe, da se ob brisanju ali posodabljanju vrednosti v primarni tabeli, 
ustrezno posodobijo ali izbrišejo povezane vrstice v odvisnih tabelah."""

# Tabela letniki:
# Hrani seznam letnikov (MAT1, APM2, FIZ3, ...).
# Vsak letnik ima unikatno ime.
# Predmeti se sklicujejo na letnik preko id_letnik.
letniki = """
CREATE TABLE IF NOT EXISTS letniki (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    letnik TEXT NOT NULL UNIQUE
);
"""

# Tabela predmeti:
# Hrani predmete, ki pripadajo posameznemu letniku.
# Vsak predmet ima ime in tuji ključ id_letnik.
# Ob brisanju letnika se izbrišejo tudi vsi njegovi predmeti (CASCADE).
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

# Tabela teme:
# Hrani teme, ki pripadajo posameznemu predmetu.
# Tema ima unikatno ime in FK id_predmet.
# Ob brisanju predmeta se izbrišejo tudi njegove teme (CASCADE).
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

# Tabela predavalnice:
# Hrani seznam predavalnic, kjer se izvajajo pisni preizkusi.
# Trenutno vsebuje samo ime predavalnice. (lahko se doda kapaciteta, če bo pomembna)
predavalnice= """
CREATE TABLE IF NOT EXISTS predavalnice (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ime TEXT NOT NULL UNIQUE
);
"""

# Tabela tipi_testov:
# Hrani tipe testov (npr. kolokvij, izpit).
# Ime tipa je unikatno.
tipi_testov = """
CREATE TABLE IF NOT EXISTS tipi_testov (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tip TEXT UNIQUE NOT NULL
);
"""

# Tabela pisni_preizkusi:
# Hrani vse pisne preizkuse (kolokvije, izpite).
# Vsebuje datum, uro, predavalnico, letnik, predmet in tip testa.
# Vsi tuji ključi imajo CASCADE, da se ob brisanju povezanih entitet
# ustrezno izbrišejo tudi preizkusi.
pisni_preizkusi = """
CREATE TABLE IF NOT EXISTS pisni_preizkusi (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    datum DATE NOT NULL,
    ura TIME NOT NULL,
    id_predavalnica INTEGER NOT NULL,
    id_letnik INTEGER NOT NULL,
    id_predmet INTEGER NOT NULL,
    id_tip INTEGER NOT NULL,
    FOREIGN KEY (id_predavalnica) REFERENCES predavalnice(id)
        ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (id_letnik) REFERENCES letniki(id)
        ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (id_predmet) REFERENCES predmeti(id)
        ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (id_tip) REFERENCES tipi_testov(id)
        ON UPDATE CASCADE ON DELETE CASCADE
);
"""

# Tabela povezovalna_teme_testi:
# Povezovalna tabela za many-to-many odnos med temami in pisnimi preizkusi.
# Omogoča, da ima en preizkus več tem in ena tema več preizkusov.
# Sestavljen primarni ključ (id_teme, id_test) preprečuje podvajanje.
# CASCADE poskrbi za čiščenje povezav ob brisanju tem ali preizkusov.
povezovalna_teme_testi = """
CREATE TABLE IF NOT EXISTS povezovalna_teme_testi (
    id_teme INTEGER NOT NULL,
    id_test INTEGER NOT NULL,
    PRIMARY KEY (id_teme, id_test),
    FOREIGN KEY (id_teme) REFERENCES teme(id) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (id_test) REFERENCES pisni_preizkusi(id) ON UPDATE CASCADE ON DELETE CASCADE
);
"""


# Tabela uporabniki:
# Hrani registrirane uporabnike spletnega vmesnika.
# Vsak uporabnik ima ime, e‑pošto, hash gesla in vlogo.
# E‑pošta mora biti unikatna (UNIQUE), da se uporabnik ne more registrirati dvakrat.
# Gesla se NE shranjujejo v navadnem tekstu, temveč kot hash (npr. SHA‑256 ali bcrypt).
uporabniki = """
CREATE TABLE IF NOT EXISTS uporabniki (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ime TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    zgostitev TEXT NOT NULL,
    sol TEXT NOT NULL,
    vloga TEXT NOT NULL DEFAULT 'student'
);
"""

def ustvari_tabelo(pot, sql_ukaz):
    """Funkcija, ki izvrši sql ukaz za dano pot do baze."""
    with sqlite3.connect(pot) as pov:
        pov.execute("PRAGMA foreign_keys = ON;")
        kaz = pov.cursor()
        kaz.execute(sql_ukaz)

def ustvari_bazo():
    PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))
    pot = os.path.join(PROJECT_ROOT, "db", "baza.sqlite")

    sql_ukazi = [
        letniki,
        predmeti,
        teme,
        predavalnice,
        tipi_testov,
        pisni_preizkusi,
        povezovalna_teme_testi,
        uporabniki
    ]

    for ukaz in sql_ukazi:
        ustvari_tabelo(pot, ukaz)

    print("Baza ustvarjena!")

ustvari_bazo