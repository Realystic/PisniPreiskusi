import csv
import sqlite3
import os

pov = sqlite3.connect("izpiti.sqlite")
pov.execute("PRAGMA foreign_keys = ON;")

# Pot do poddirektorija
POT = "CSV_podatki"

def uvozi_csv(vrstica, tabela, stolpci):
    kaz = pov.cursor()
    placeholders = ",".join(["?"] * len(stolpci))
    sql = f"INSERT INTO {tabela} ({','.join(stolpci)}) VALUES ({placeholders})"
    kaz.execute(sql, [vrstica[s] for s in stolpci])


# 1) letniki
with open(os.path.join(POT, "letniki.csv"), encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        uvozi_csv(row, "letniki", ["ime"])

# 2) predmeti
with open(os.path.join(POT, "predmeti.csv"), encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        uvozi_csv(row, "predmeti", ["ime", "id_letnik"])

# 3) teme
with open(os.path.join(POT, "teme.csv"), encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        uvozi_csv(row, "teme", ["tema", "id_predmet"])

# 4) predavalnice
with open(os.path.join(POT, "predavalnice.csv"), encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        uvozi_csv(row, "predavalnice", ["ime"])

# 5) tipi_testov
with open(os.path.join(POT, "tipi_testov.csv"), encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        uvozi_csv(row, "tipi_testov", ["tip"])

pov.commit()
pov.close()