from db import (
    Letnik,
    Predmet,
    Tema,
    Predavalnica,
    TipTesta,
    ustvari_povezavo
)

#pov = ustvari_povezavo()
def meni_podatki(pov):
    """Prikaže meni za upravljanje osnovnih podatkov (letniki, predmeti, teme...)."""
    pov = ustvari_povezavo()
    while True:
        print("\n--- Upravljanje podatkov ---\n")
        print("1) Upravljanje letnikov")
        print("2) Upravljanje predmetov")
        print("3) Upravljanje tem")
        print("4) Upravljanje predavalnic")
        print("5) Upravljanje tipov testov")
        print("6) Nazaj")

        izbira = input("Izberi možnost: ")

        if izbira == "1":
            meni_letniki(pov)
        elif izbira == "2":
            meni_predmeti(pov)
        elif izbira == "3":
            meni_teme(pov)
        elif izbira == "4":
            meni_predavalnice(pov)
        elif izbira == "5":
            meni_tipi_testov(pov)
        elif izbira == "6":
            break
        else:
            print("Neveljavna izbira.")

def meni_letniki(pov):
    while True:
        print("\n--- Letniki ---\n")
        print("1) Dodaj letnik")
        print("2) Preglej vse letnike")
        print("3) Izbriši letnik")
        print("4) Nazaj")

        izbira = input("Izberi možnost: ")

        if izbira == "1":
            dodaj_letnik_ui(pov)
        elif izbira == "2":
            pregled_letnikov_ui(pov)
        elif izbira == "3":
            izbrisi_letnik_ui(pov)
        elif izbira == "4":
            break
        else:
            print("Neveljavna izbira.")

def dodaj_letnik_ui(pov):
    """UI za dodajanje novega letnika."""
    print("\n--- Dodaj letnik ---\n")

    letnik = input("Vnesi ime letnika (npr. APM2): ").strip()

    if not letnik:
        print("Letnik ne sme biti prazen.")
        return

    # Uporaba razredov iz db:
    nov = Letnik(letnik)
    nov.shrani(pov)

    print(f"Letnik '{letnik}' uspešno dodan.")

#meni_letniki(pov)