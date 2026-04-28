from db.funkcije import ustvari_povezavo
from stvaritev_baze.geneza_razpredelnic import ustvari_bazo
from stvaritev_baze.csv_bralec import napolni_bazo
from db.uporabniki import Uporabnik

def ustvari_admina(pov):
    Uporabnik.ustvari(pov, "Admin", "admin@fmf.si", "1234", vloga="admin")

if __name__ == "__main__":
    ustvari_bazo()
    napolni_bazo()

    pov = ustvari_povezavo()

    ustvari_admina(pov)
    Uporabnik.ustvari(pov, "Franc", "franc@fmf.si", "geslo123", vloga="student")

    pov.close()

    print("Vse pripravljeno.")
