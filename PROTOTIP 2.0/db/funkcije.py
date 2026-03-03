import sqlite3

from .pisni_preizkusi import PisniPreizkus
from .predmeti import Predmet
from .letniki import Letnik
from .predavalnice import Predavalnica
from .tipi_testov import TipTesta
from .teme import Tema

def ustvari_povezavo():
    """Ustvari povezavo z bazo podatkov in omogoči uporabo tujih ključev."""
    pov = sqlite3.connect("izpiti.sqlite")
    pov.execute("PRAGMA foreign_keys = ON;")
    return pov


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

def opis_preizkusa(pov, preizkus):
    """Vrne lep opis pisnega preizkusa z imeni namesto ID-jev."""

    predmet = Predmet.najdi(pov, preizkus.id_predmet)
    letnik = Letnik.najdi(pov, preizkus.id_letnik)
    predavalnica = Predavalnica.najdi(pov, preizkus.id_predavalnica)
    tip = TipTesta.najdi(pov, preizkus.id_tip)
    teme = Tema.za_preizkus(pov, preizkus.id)

    seznam_tem = ", ".join(t.tema for t in teme)

    return (
        f"  ID: {preizkus.id}\n"
        f"  Termin: {preizkus.datum} ob {preizkus.ura}\n"
        f"  Letnik: {letnik.letnik}\n"
        f"  Predmet: {predmet.ime}\n"
        f"  Predavalnica: {predavalnica.ime}\n"
        f"  Tip testa: {tip.tip}\n"
        f"  Teme: {seznam_tem}\n"
    )