import csv
import sqlite3



pov = sqlite3.connect("izpiti.sqlite")
pov.execute("PRAGMA foreign_keys = ON;")
kaz = pov.cursor()

#Pobriše vse obstoječe podatke iz tabel, da se prepreči podvajanje pri ponovnem zagonu skripte #66
kaz.execute("DELETE FROM povezovalna_teme_testi;")
kaz.execute("DELETE FROM pisni_preizkusi;")
kaz.execute("DELETE FROM teme;")
kaz.execute("DELETE FROM predmeti;")
kaz.execute("DELETE FROM predavalnice;")
kaz.execute("DELETE FROM tipi_testov;")
kaz.execute("DELETE FROM letniki;")
pov.commit()

#Uvozi letnike iz CSV datoteke in jih vstavi v bazo
with open("CSV_podatki/letniki.csv", encoding="utf-8") as dat:
    bralec = csv.DictReader(dat)
    for vrstica in bralec:
        id_ = vrstica["id"]
        letnik = vrstica["letnik"]
        kaz.execute(
            "INSERT INTO letniki (id, letnik) VALUES (?, ?)",
            (id_, letnik)
        )



#Uvozi predmete iz CSV datoteke in jih vstavi v bazo
with open("CSV_podatki/predmeti.csv", encoding="utf-8") as dat:
    bralec = csv.DictReader(dat)
    for vrstica in bralec:
        id_ = vrstica["id"]
        ime = vrstica["ime"]
        id_letnik = vrstica["id_letnik"]
        kaz.execute(
            "INSERT INTO predmeti (id, ime, id_letnik) VALUES (?, ?, ?)",
            (id_, ime, id_letnik)
        )



#Uvozi teme iz CSV datoteke in jih vstavi v bazo
with open("CSV_podatki/teme.csv", encoding="utf-8") as dat:
    bralec = csv.DictReader(dat)
    for vrstica in bralec:
        id_ = vrstica["id"]
        tema = vrstica["tema"]
        id_predmet = vrstica["id_predmet"]
        kaz.execute(
            "INSERT INTO teme (id, tema, id_predmet) VALUES (?, ?, ?)",
            (id_, tema, id_predmet)
        )



#Uvozi predavalnice iz CSV datoteke in jih vstavi v bazo
with open("CSV_podatki/predavalnice.csv", encoding="utf-8") as dat:
    bralec = csv.DictReader(dat)
    for vrstica in bralec:
        id_ = vrstica["id"]
        ime = vrstica["ime"]
        kaz.execute(
            "INSERT INTO predavalnice (id, ime) VALUES (?, ?)",
            (id_, ime)
        )



#Uvozi tipe testov iz CSV datoteke in jih vstavi v bazo
with open("CSV_podatki/tipi_testov.csv", encoding="utf-8") as dat:
    bralec = csv.DictReader(dat)
    for vrstica in bralec:
        id_ = vrstica["id"]
        tip = vrstica["tip"]
        kaz.execute(
            "INSERT INTO tipi_testov (id, tip) VALUES (?, ?)",
            (id_, tip)
        )


#Uvozi pisne preizkuse iz CSV datoteke in jih vstavi v bazo
with open("CSV_podatki/pisni_preizkusi.csv", encoding="utf-8") as dat:
    bralec = csv.DictReader(dat)
    for vrstica in bralec:
        id_ = vrstica["id"]
        datum = vrstica["datum"]
        ura = vrstica["ura"]
        id_predavalnica = vrstica["id_predavalnica"]
        id_letnik = vrstica["id_letnik"]
        id_predmet = vrstica["id_predmet"]
        id_tip = vrstica["id_tip"]

        kaz.execute(
            """INSERT INTO pisni_preizkusi
               (id, datum, ura, id_predavalnica, id_letnik, id_predmet, id_tip)
               VALUES (?, ?, ?, ?, ?, ?, ?)""",
            (id_, datum, ura, id_predavalnica, id_letnik, id_predmet, id_tip)
        )


#Uvozi povezovalno tabelo teme_testi iz CSV datoteke in jih vstavi v bazo
with open("CSV_podatki/povezovalna_teme_testi.csv", encoding="utf-8") as dat:
    bralec = csv.DictReader(dat)
    for vrstica in bralec:
        id_teme = vrstica["id_teme"]
        id_test = vrstica["id_test"]

        kaz.execute(
            "INSERT INTO povezovalna_teme_testi (id_teme, id_test) VALUES (?, ?)",
            (id_teme, id_test)
        )

pov.commit()
pov.close()
