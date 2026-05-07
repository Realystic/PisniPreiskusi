import os
import sqlite3
from datetime import datetime

from .pisni_preizkusi import PisniPreizkus
from .predmeti import Predmet
from .letniki import Letnik
from .predavalnice import Predavalnica
from .tipi_testov import TipTesta
from .teme import Tema


def ustvari_povezavo():
    pot = os.path.join(os.path.dirname(__file__), "baza.sqlite")
    pot = os.path.abspath(pot)
    return sqlite3.connect(pot)


def dodaj_temo_preizkusu(pov, id_teme, id_test):
    """Poveže temo s pisnim preizkusom v tabeli povezovalna_teme_testi."""
    kaz = pov.cursor()
    kaz.execute("""
        INSERT INTO povezovalna_teme_testi (id_teme, id_test)
        VALUES (?, ?)
    """, (id_teme, id_test))
    pov.commit()


def ustvari_preizkus(pov, datum, ura, id_predavalnica, id_letnik, id_predmet, id_tip, seznam_tem):
    """Ustvari nov pisni preizkus in ga poveže z izbranimi temami."""
    # 1) ustvari preizkus
    preizkus = PisniPreizkus(datum, ura, id_predavalnica, id_letnik, id_predmet, id_tip)
    preizkus.shrani(pov)

    # 2) poveže izbrane teme
    for id_teme in seznam_tem:
        dodaj_temo_preizkusu(pov, id_teme, preizkus.id)

    return preizkus


def normalen_datum(datum):
    d = datetime.strptime(datum, "%Y-%m-%d")
    return d.strftime("%d.%m.%Y")


def opis_preizkusa(pov, preizkus):
    """Vrne podatke o preizkusu kot slovar z imeni namesto ID-jev."""

    predmet = Predmet.najdi(pov, preizkus.id_predmet)
    letnik = Letnik.najdi(pov, preizkus.id_letnik)
    predavalnica = Predavalnica.najdi(pov, preizkus.id_predavalnica)
    tip = TipTesta.najdi(pov, preizkus.id_tip)
    teme = Tema.za_preizkus(pov, preizkus.id)


    return {
    "id": preizkus.id,
    "datum_iso": preizkus.datum,               # YYYY-MM-DD (za sortiranje)
    "datum": normalen_datum(preizkus.datum), # DD.MM.YYYY (za prikaz)
    "ura": preizkus.ura,
    "letnik": letnik.letnik,
    "predmet": predmet.ime,
    "predavalnica": predavalnica.ime,
    "tip": tip.tip,
    "teme": ", ".join(t.tema for t in teme)
}

def opis_preizkusa_cli(pov, preizkus):
    """Vrne lep večvrstični opis preizkusa za CLI izpis."""
    d = opis_preizkusa(pov, preizkus)

    return (
        f"ID: {d['id']}\n"
        f"{d['datum']} ob {d['ura']}\n"
        f"Letnik:       {d['letnik']}\n"
        f"Predmet:      {d['predmet']}\n"
        f"Predavalnica: {d['predavalnica']}\n"
        f"Tip testa:    {d['tip']}\n"
        f"Teme:         {d['teme']}\n"
    )
