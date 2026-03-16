import sys
import os

# Dodamo pot do glavne mape projekta
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from db.funkcije import ustvari_povezavo
from db.uporabniki import Uporabnik
from db.geslo import sifriraj_geslo


# Ustvarimo povezavo
pov = ustvari_povezavo()

# Geslo admina
geslo = "1234"
hash_gesla, sol = sifriraj_geslo(geslo)

# Ustvarimo admina
u = Uporabnik(
    ime="Admin",
    email="admin@fmf.si",
    geslo_hash=hash_gesla,
    sol=sol,
    vloga="admin"
)

u.shrani(pov)
print("Admin ustvarjen!")