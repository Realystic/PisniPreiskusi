from db import *

def glavni_meni():
    """Prikaže glavni meni za upravljanje ..."""
    while True:
        print("\n--- Glavni meni ---\n")
        print("1) Upravljanje letnikov")
        print("2) Upravljanje predmetov")
        print("3) Upravljanje predavalnic")
        print("4) Upravljanje tipov testov")
        print("5) Upravljanje tem")
        print("6) Izhod")

        izbira = input("Izberi možnost: ")

        if izbira == "1":
            meni_letniki()
        elif izbira == "2":
            meni_predmeti()
        elif izbira == "3":
            meni_predavalnice()
        elif izbira == "4":
            meni_tip_testa()
        elif izbira == "5":
            meni_teme()
        elif izbira == "6":
            print("Izhod iz programa.")
            break
        else:
            print("Neveljavna izbira.")
#################################################################
def meni_letniki():
    """Prikaže meni za upravljanje letnikov. (dodajanje, brisanje, pregled)"""
    while True:
        print("\n--- Upravljanje letnikov ---\n")
        prikazi_letnike_ui()
        print("\n-----------------------")
        print("1) Dodaj letnik")
        print("2) Izbrisi letnik")
        print("3) Nazaj")

        izbira = input("Izberi možnost: ")

        if izbira == "1":
            dodaj_letnik_ui()
        elif izbira == "2":
            izbrisi_letnike_ui()
        elif izbira == "3":
            break
        else:
            print("Neveljavna izbira.")


def dodaj_letnik_ui():
    letnik = input("Vnesi naziv letnika (npr. APM2): ")
    dodaj_letnik(letnik.upper())
    print("Letnik dodan.")

def prikazi_letnike_ui():
    letniki = prikazi_letnike()
    print("\n--- Seznam letnikov ---")
    for id_, naziv in letniki:
        print(f"{id_}: {naziv}")

def izbrisi_letnike_ui():
    id_letnik = input("Vnesi id letnika za izbris: ")
    izbrisi_letnik(id_letnik)
    print(f"{id_letnik} izbrisan.")
###############################################################
def meni_predmeti():
    """Prikaže meni za upravljanje predmetov. (dodajanje, brisanje, pregled)"""
    while True:
        print("\n--- Upravljanje predmetov ---\n")
        prikazi_predmete_ui()
        print("\n-----------------------")
        print("1) Dodaj predmet")
        print("2) Izbrisi predmet")
        print("3) Nazaj")

        izbira = input("Izberi možnost: ")

        if izbira == "1":
            dodaj_predmet_ui()
        elif izbira == "2":
            izbrisi_predmet_ui()
        elif izbira == "3":
            break
        else:
            print("Neveljavna izbira.")

def dodaj_predmet_ui():
    predmet = input("Vnesi predmet: ")
    nosilec = input("Vnesi nosilca (neobvezno): ")
    if nosilec.strip() == "":
        nosilec = None
    dodaj_predmet(predmet, nosilec)
    print("Predmet dodan.")

def prikazi_predmete_ui():
    predmeti = prikazi_predmete()
    print("\n--- Seznam predmetov ---")
    for id_, naziv, nosilec in predmeti:
        print(f"{id_}: {naziv} ({nosilec})" if nosilec else f"{id_}: {naziv}")

def izbrisi_predmet_ui():
    id_predmet = input("Kateri predmet želiš izbrisati (ID): ")
    izbrisi_predmet(id_predmet)
    print(f"{id_predmet} izbrisan.")
################################################################
def meni_predavalnice():
    """Prikaže meni za upravljanje predavalnic. (dodajanje, brisanje, pregled)"""
    while True:
        print("\n--- Upravljanje predavalnic ---\n")
        prikazi_predavalnice_ui()
        print("\n-----------------------")
        print("1) Dodaj predavalnico")
        print("2) Izbrisi predavalnico")
        print("3) Nazaj")

        izbira = input("Izberi možnost: ")

        if izbira == "1":
            dodaj_predavalnico_ui()
        elif izbira == "2":
            izbrisi_predavalnico_ui()
        elif izbira == "3":
            break
        else:
            print("Neveljavna izbira.")
def dodaj_predavalnico_ui():
    ime = input("Vnesi ime predavalnice: ")
    kapaciteta = input("Vnesi kapaciteto (neobvezno): ")
    if kapaciteta.strip() == "":
        kapaciteta = None
    else:
        kapaciteta = int(kapaciteta)
    dodaj_predavalnico(ime, kapaciteta)
    print("Predavalnica dodana.")

def prikazi_predavalnice_ui():
    predavalnice = prikazi_predavalnice()
    print("\n--- Seznam predavalnic ---")
    for id_, ime, kapaciteta in predavalnice:
        print(f"{id_}: {ime} (Kapaciteta: {kapaciteta})" if kapaciteta else f"{id_}: {ime}")

def izbrisi_predavalnico_ui():
    id_predavalnica = input("Katero predavalnico želiš izbrisati (ID): ")
    izbrisi_predavalnico(id_predavalnica)
    print(f"{id_predavalnica} izbrisan.")

#################################################################
def meni_tip_testa():
    """Prikaže meni za upravljanje tipov testov. (dodajanje, brisanje, pregled)"""
    while True:
        print("\n--- Upravljanje tipov testov ---\n")
        prikazi_tipe_testov_ui()
        print("\n-----------------------")
        print("1) Dodaj tip testa")
        print("2) Izbrisi tip testa")
        print("3) Nazaj")

        izbira = input("Izberi možnost: ")

        if izbira == "1":
            dodaj_tip_testa_ui()
        elif izbira == "2":
            izbrisi_tip_testa_ui()
        elif izbira == "3":
            break
        else:
            print("Neveljavna izbira.")

def dodaj_tip_testa_ui():
    tip = input("Vnesi tip testa: ")
    dodaj_tip_testa(tip)
    print("Tip testa dodan.")

def prikazi_tipe_testov_ui():
    tipi = prikazi_tipe_testov()
    print("\n--- Seznam tipov testov ---")
    for id_, tip in tipi:
        print(f"{id_}: {tip}")

def izbrisi_tip_testa_ui():
    id_tip = input("Kateri tip testa želiš izbrisati (ID): ")
    izbrisi_tip_testa(id_tip)
    print(f"{id_tip} izbrisan.")

################################################################
def meni_teme():
    """Prikaže meni za upravljanje tem in testov. (dodajanje, brisanje, pregled)"""
    while True:
        print("\n--- Upravljanje tem ---\n")
        prikazi_teme_ui()
        print("\n-----------------------")
        print("1) Dodaj temo")
        print("2) Izbrisi temo")
        print("3) Nazaj")

        izbira = input("Izberi možnost: ")

        if izbira == "1":
            dodaj_temo_ui()
        elif izbira == "2":
            izbrisi_temo_ui()
        elif izbira == "3":
            break
        else:
            print("Neveljavna izbira.")

def dodaj_temo_ui():
    tema = input("Vnesi temo: ")
    dodaj_temo(tema)
    print("Tema dodana.")

def prikazi_teme_ui():
    teme = prikazi_teme()
    print("\n--- Seznam tem ---")
    for id_, tema in teme:
        print(f"{id_}: {tema}")

def izbrisi_temo_ui():
    id_tema = input("Katero temo želiš izbrisati (ID): ")
    izbrisi_temo(id_tema)
    print(f"{id_tema} izbrisana.")