import csv
import os
from db.funkcije import ustvari_povezavo

def napolni_bazo():
    """Funkcija, ki napolni bazo s podatki iz CSV datotek. Najprej pobriše obstoječe podatke!"""
    pov = ustvari_povezavo()

    pov.execute("PRAGMA foreign_keys = ON;")
    kaz = pov.cursor()

    # Pobriše vse obstoječe podatke iz tabel
    kaz.execute("DELETE FROM povezovalna_teme_testi;")
    kaz.execute("DELETE FROM pisni_preizkusi;")
    kaz.execute("DELETE FROM teme;")
    kaz.execute("DELETE FROM predmeti;")
    kaz.execute("DELETE FROM predavalnice;")
    kaz.execute("DELETE FROM tipi_testov;")
    kaz.execute("DELETE FROM letniki;")
    pov.commit()

    # Relativna pot do CSV map
    CSV_DIR = os.path.join(os.path.dirname(__file__), "CSV_podatki")
    

    # Uvozi letnike
    with open(os.path.join(CSV_DIR, "letniki.csv"), encoding="utf-8") as dat:
        bralec = csv.DictReader(dat)
        for vrstica in bralec:
            kaz.execute(
                "INSERT INTO letniki (id, letnik) VALUES (?, ?)",
                (vrstica["id"], vrstica["letnik"])
            )

    # Uvozi predmete
    with open(os.path.join(CSV_DIR, "predmeti.csv"), encoding="utf-8") as dat:
        bralec = csv.DictReader(dat)
        for vrstica in bralec:
            kaz.execute(
                "INSERT INTO predmeti (id, ime, id_letnik) VALUES (?, ?, ?)",
                (vrstica["id"], vrstica["ime"], vrstica["id_letnik"])
            )

    # Uvozi teme
    with open(os.path.join(CSV_DIR, "teme.csv"), encoding="utf-8") as dat:
        bralec = csv.DictReader(dat)
        for vrstica in bralec:
            kaz.execute(
                "INSERT INTO teme (id, tema, id_predmet) VALUES (?, ?, ?)",
                (vrstica["id"], vrstica["tema"], vrstica["id_predmet"])
            )

    # Uvozi predavalnice
    with open(os.path.join(CSV_DIR, "predavalnice.csv"), encoding="utf-8") as dat:
        bralec = csv.DictReader(dat)
        for vrstica in bralec:
            kaz.execute(
                "INSERT INTO predavalnice (id, ime) VALUES (?, ?)",
                (vrstica["id"], vrstica["ime"])
            )

    # Uvozi tipe testov
    with open(os.path.join(CSV_DIR, "tipi_testov.csv"), encoding="utf-8") as dat:
        bralec = csv.DictReader(dat)
        for vrstica in bralec:
            kaz.execute(
                "INSERT INTO tipi_testov (id, tip) VALUES (?, ?)",
                (vrstica["id"], vrstica["tip"])
            )

    # Uvozi pisne preizkuse
    with open(os.path.join(CSV_DIR, "pisni_preizkusi.csv"), encoding="utf-8") as dat:
        bralec = csv.DictReader(dat)
        for vrstica in bralec:
            kaz.execute(
                """INSERT INTO pisni_preizkusi
                   (id, datum, ura, id_predavalnica, id_letnik, id_predmet, id_tip)
                   VALUES (?, ?, ?, ?, ?, ?, ?)""",
                (
                    vrstica["id"],
                    vrstica["datum"],
                    vrstica["ura"],
                    vrstica["id_predavalnica"],
                    vrstica["id_letnik"],
                    vrstica["id_predmet"],
                    vrstica["id_tip"]
                )
            )

    # Uvozi povezovalno tabelo
    with open(os.path.join(CSV_DIR, "povezovalna_teme_testi.csv"), encoding="utf-8") as dat:
        bralec = csv.DictReader(dat)
        for vrstica in bralec:
            kaz.execute(
                "INSERT INTO povezovalna_teme_testi (id_teme, id_test) VALUES (?, ?)",
                (vrstica["id_teme"], vrstica["id_test"])
            )

    pov.commit()
    pov.close()

    print("Baza napolnjena s CSV podatki!")
