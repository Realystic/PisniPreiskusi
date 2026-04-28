import sqlite3
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from upravljanje_podatkov import *
from db import (
    Letnik,
    Predmet,
    PisniPreizkus,
    Tema,
    Predavalnica,
    TipTesta,
    ustvari_povezavo,
    ustvari_preizkus,
    opis_preizkusa
)



def glavni_meni():
    """Prikaže glavni meni za upravljanje podatkov in pisnih preizkusov."""
    pov = ustvari_povezavo()

    while True:
        print("\n=== GLAVNI MENI ===\n")
        print("1) Upravljanje podatkov")
        print("2) Upravljanje pisnih preizkusov")
        print("3) Izhod")

        izbira = input("Izberi možnost: ")

        if izbira == "1":
            meni_podatki(pov)
        elif izbira == "2":
            meni_preizkusi(pov)
        elif izbira == "3":
            print("Izhod iz programa.")
            break
        else:
            print("Neveljavna izbira.")


def meni_preizkusi(pov):
    """Prikaže meni za upravljanje pisnih preizkusov (dodajanje, pregled, brisanje)."""
    while True:
        print("\n--- Upravljanje pisnih preizkusov ---\n")
        print("1) Dodaj pisni preizkus")
        print("2) Preglej vse preizkuse")
        print("3) Preglej preizkuse po datumu")
        print("4) Preglej preizkuse po predmetu")
        print("5) Preglej preizkuse po letniku")
        print("6) Izbriši preizkus")
        print("7) Nazaj")

        izbira = input("Izberi možnost: ")

        if izbira == "1":
            dodaj_preizkus_ui(pov)
        elif izbira == "2":
            pregled_vseh_ui(pov)
        elif izbira == "3":
            pregled_po_datumu_ui(pov)
        elif izbira == "4":
            pregled_po_predmetu_ui(pov)
        elif izbira == "5":
            pregled_po_letniku_ui(pov)
        elif izbira == "6":
            izbrisi_preizkus_ui(pov)
        elif izbira == "7":
            break
        else:
            print("Neveljavna izbira.")


def dodaj_preizkus_ui(pov):
    """Prikaže vmesnik za dodajanje novega pisnega preizkusa."""
    print("\n--- Dodaj pisni preizkus ---\n")

    # Izbira predavalnice
    print("\nPredavalnice:")
    predavalnice = Predavalnica.vse(pov)
    for p in predavalnice:
        print(p)
    id_predavalnica = input("Izberi ID predavalnice: ")

    # Izbira letnika
    print("\nLetniki:")
    letniki = Letnik.vsi(pov)
    for l in letniki:
        print(l)
    id_letnik = input("Izberi ID letnika: ")

    # Izbira predmeta
    print("\nPredmeti:")
    predmeti = Predmet.za_letnik(pov, id_letnik)
    for p in predmeti:
        print(p)
    id_predmet = input("Izberi ID predmeta: ")

    # Izbira tipa testa
    print("\nTipi testov:")
    tipi = TipTesta.vsi(pov)
    for t in tipi:
        print(t)
    id_tip = input("Izberi ID tipa testa: ")

    # Izbira tem
    print("\nTeme:")
    teme = Tema.za_predmet(pov, id_predmet)
    for t in teme:
        print(t)

    seznam_tem = input("Vnesi ID-ji tem, ločene z vejico (npr. 1,3,5): ")
    seznam_tem = [int(x.strip()) for x in seznam_tem.split(",")]

    # Vnos datuma in ure
    datum = input("Vnesi datum (YYYY-MM-DD): ")
    ura = input("Vnesi uro (HH:MM): ")

    # Ustvari preizkus
    preizkus = ustvari_preizkus(
        pov, datum, ura, id_predavalnica, id_letnik, id_predmet, id_tip, seznam_tem
    )

    print("\nPreizkus uspešno dodan:")
    print(opis_preizkusa(pov, preizkus))

def pregled_vseh_ui(pov):
    """Prikaže vmesnik za pregled vseh pisnih preizkusov."""
    preizkusi = PisniPreizkus.vsi(pov)

    print("\n--- Vsi pisni preizkusi ---")
    if not preizkusi:
        print("Ni preizkusov.")
    else:
        for p in preizkusi:
            print(opis_preizkusa(pov, p))

def pregled_po_datumu_ui(pov):
    """Prikaže vmesnik za pregled pisnih preizkusov na določen datum."""
    datum = input("Vnesi datum (YYYY-MM-DD): ")
    preizkusi = PisniPreizkus.na_dan(pov, datum)

    print(f"\n--- Preizkusi na dan {datum} ---")
    if not preizkusi:
        print("Ni preizkusov.")
    else:
        for p in preizkusi:
            print(opis_preizkusa(pov, p))

def pregled_po_predmetu_ui(pov):
    """Prikaže vmesnik za pregled pisnih preizkusov za določen predmet."""
    print("\nPredmeti:")
    for p in Predmet.vsi(pov):
        print(p)

    id_predmet = input("Izberi ID predmeta: ")
    predmet = Predmet.najdi(pov, id_predmet)
    preizkusi = PisniPreizkus.za_predmet(pov, id_predmet)

    print(f"\n--- Preizkusi za predmet {predmet.ime} ---")
    if not preizkusi:
        print("Ni preizkusov.")
    else:
        for p in preizkusi:
            print(opis_preizkusa(pov, p))

def pregled_po_letniku_ui(pov):
    """Prikaže vmesnik za pregled pisnih preizkusov za določen letnik."""
    print("\nLetniki:")
    for l in Letnik.vsi(pov):
        print(l)

    id_letnik = input("Izberi ID letnika: ")
    letnik = Letnik.najdi(pov, id_letnik)
    preizkusi = PisniPreizkus.za_letnik(pov, id_letnik)

    print(f"\n--- Preizkusi za letnik {letnik.letnik} ---")
    if not preizkusi:
        print("Ni preizkusov.")
    else:
        for p in preizkusi:
            print(opis_preizkusa(pov, p))

def izbrisi_preizkus_ui(pov):
    """Prikaže vmesnik za brisanje pisnega preizkusa glede na ID."""
    print("\nVsi preizkusi:")
    for p in PisniPreizkus.vsi(pov):
        print(opis_preizkusa(pov, p))

    id_preizkus = input("Vnesi ID preizkusa za izbris: ")

    preizkus = PisniPreizkus.najdi(pov, id_preizkus)
    if preizkus:
        preizkus.izbrisi(pov)
        print("Preizkus izbrisan.")
    else:
        print("Preizkus ne obstaja.")