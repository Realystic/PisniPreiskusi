import csv
import sqlite3



pov = sqlite3.connect("izpiti.sqlite")
pov.execute("PRAGMA foreign_keys = ON;")
kaz = pov.cursor()


#Uvozi letnike iz CSV datoteke in jih vstavi v bazo
with open("CSV_podatki/letniki.csv", encoding="utf-8") as dat:
    bralec = csv.DictReader(dat)
    for vrstica in bralec:
        letnik = vrstica["letnik"]
        kaz.execute("INSERT INTO letniki (letnik) VALUES (?)", (letnik,))


#Uvozi predmete iz CSV datoteke in jih vstavi v bazo
with open("CSV_podatki/predmeti.csv", encoding="utf-8") as dat:
    bralec = csv.DictReader(dat)
    for vrstica in bralec:
        ime_predmeta = vrstica["ime"]
        id_letnik = vrstica["id_letnik"]
        kaz.execute(
            "INSERT INTO predmeti (ime, id_letnik) VALUES (?, ?)",
            (ime_predmeta, id_letnik)
        )


#Uvozi teme iz CSV datoteke in jih vstavi v bazo
with open("CSV_podatki/teme.csv", encoding="utf-8") as dat:
    bralec = csv.DictReader(dat)
    for vrstica in bralec:
        tema = vrstica["tema"]
        id_predmet = vrstica["id_predmet"]
        kaz.execute(
            "INSERT INTO teme (tema, id_predmet) VALUES (?, ?)",
            (tema, id_predmet)
        )


#Uvozi predavalnice iz CSV datoteke in jih vstavi v bazo
with open("CSV_podatki/predavalnice.csv", encoding="utf-8") as dat:
    bralec = csv.DictReader(dat)
    for vrstica in bralec:
        predavalnica = vrstica["ime"]
        kaz.execute(
            "INSERT INTO predavalnice (ime) VALUES (?)",
            (predavalnica,)
        )


#Uvozi tipe testov iz CSV datoteke in jih vstavi v bazo
with open("CSV_podatki/tipi_testov.csv", encoding="utf-8") as dat:
    bralec = csv.DictReader(dat)
    for vrstica in bralec:
        tip = vrstica["tip"]
        kaz.execute(
            "INSERT INTO tipi_testov (tip) VALUES (?)",
            (tip,)
        )

pov.commit()
pov.close()
