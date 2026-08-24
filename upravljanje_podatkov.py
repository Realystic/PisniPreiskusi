from db import (
    Letnik,
    Predmet,
    Tema,
    Predavalnica,
    TipTesta,
    ustvari_povezavo
)

def meni_podatki(pov):
    """Prikaže meni za upravljanje osnovnih podatkov (letniki, predmeti, teme...)."""
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
            print("ne-implementirano")
            #meni_teme(pov)
        elif izbira == "4":
            print("ne-implementirano")
            #meni_predavalnice(pov)
        elif izbira == "5":
            print("ne-implementirano")
            #meni_tipi_testov(pov)
        elif izbira == "6":
            break
        else:
            print("Neveljavna izbira.")

# MENI LETNIKI in ukazi
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
    
def izbrisi_letnik_ui(pov):
    """UI za Brisanje letnikov."""
    print("\n--- Izbrisi letnik ---\n")

    #izpis letnikov
    tab = Letnik.vsi(pov) # nima nizov letnikov
    letniki = sorted(list(map(str, tab))) # spremeni v nize in jih sortira po id
    for l in letniki:
        print(l)
    
    letnik_id = input("Vnesi id letnika (prekini z -1): ").strip()
    if not letnik_id:
        print("ID ne sme biti prazen.")
        return
    if not letnik_id.lstrip('-').isdigit():
        print("Neveljaven vnos.")
        return
    letnik_id = int(letnik_id)
    if letnik_id == -1:
        print("Prekinjamo....")
        return
    
    # zanka za potrditev brisanja
    potrditev = ""
    while(potrditev not in {"Y", "N"}):
        potrditev = input(f"\nPotrdite brisanje letkina z ID '{letnik_id}' (Y/N):").strip()
        if potrditev in {"Y", "N"}:
            break
        
        print("Neveljaven ukaz.")
    
    if potrditev == "N":
        print("Brisanje prekinjeno.")
        return
    # Uporaba razredov iz db:
    brisi = Letnik("", letnik_id)
    brisi.izbrisi(pov)
    print(f"Letnik z ID {letnik_id} uspešno izbrisan.")

def pregled_letnikov_ui(pov):
    """UI za Pregled letnikov."""
    print("\n--- Pregled letnikov (po abecedi)---\n")
    
    # Uporaba razredov iz db:
    tab = Letnik.vsi(pov)
    for l in tab:
        print(l)

    print(f"Letniki uspešno prikazani.")




# Meni PREDMETI in ukazi
def meni_predmeti(pov):
    while True:
        print("\n--- Predmeti ---\n")
        print("1) Preglej vse predmete")
        print("2) Dodaj predmet")
        print("3) Izbriši predmet")
        print("4) Nazaj")

        izbira = input("Izberi možnost: ")

        match izbira: # python verzija switch case-a
            case "1":
                print("ne-implementirano")
                #pregled_predmetov_ui(pov)
            case "2":
                print("ne-implementirano")
                #dodaj_premet_ui(pov)
            case "3":
                print("ne-implementirano")
                #izbrisi_predmet_ui(pov)
            case "4":
                break
            case _: 
                print("Neveljavna izbira.")