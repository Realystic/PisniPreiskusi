from .letniki import Letnik
from .predmeti import Predmet
from .teme import Tema
from .predavalnice import Predavalnica
from .tipi_testov import TipTesta
from .pisni_preizkusi import PisniPreizkus

from .funkcije import (
    ustvari_povezavo,
    dodaj_temo_preizkusu,
    ustvari_preizkus,
    opis_preizkusa
)

__all__ = [
    "Letnik",
    "Predmet",
    "Tema",
    "Predavalnica",
    "TipTesta",
    "PisniPreizkus",
    "ustvari_povezavo",
    "dodaj_temo_preizkusu",
    "ustvari_preizkus",
    "opis_preizkusa",
]