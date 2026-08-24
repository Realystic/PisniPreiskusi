import os
from db.funkcije import ustvari_povezavo
from db.uporabniki import Uporabnik
from stvaritev_baze.geneza_razpredelnic import ustvari_bazo
from stvaritev_baze.csv_bralec import napolni_bazo

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
POT = os.path.join(PROJECT_ROOT, "db", "baza.sqlite")

if os.path.exists(POT):
    os.remove(POT)

ustvari_bazo()
napolni_bazo()

pov = ustvari_povezavo()

Uporabnik.ustvari(pov, "Admin", "admin@fmf.si", "123", vloga="admin")
Uporabnik.ustvari(pov, "Upor", "upor@bnik.si", "abnik", vloga="student")

pov.close()

print("Baza ustvarjena in napolnjena. Admin in Uporabnik dodana.")