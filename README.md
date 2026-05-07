# Naslov projekta: PisniPreiskusi
## Namen projekta: Pregled in urejanje pisnih preizkusov na FMF
```
 Funkcionalnosti: dodajanje in pregled pisnih preizkusov
 Opis baze:
 ER slika
 Navodila:
 1. ukaz za vzpostavitev baze podatkov:
 python -m stvaritev_baze.naredi_bazo

 2. ukaz za zagon tekstovnega vmesnika:
 python -m tekstovni_vmesnik
-prvi del: "Upravljanje pisnih preizkusov" povsem deluje:
--pregled vseh pisnih preizkusov
--dodajanje novih pisnih preizkusov
--pregledd preizkusov po:
datumu
letniku
predmetu
--brisanje preizkusov
-drugi del: "Upravljanje podatkov" je pa ZELO okrnjen

 3. ukaz za zagon spletnega vmesnika:
 python -m spletni_vmesnik
-vnešena uporabniška računa:
--ime: admin | email:admin@fmf.si | geslo: 123
--ime: upor | email: upor@bnik.si | geslo: abnik
funkcionalnosti spletnega vmesnika:
-vsi lahko vidijo kateri pisni preizusi so vnešeni
-uporabniki lahko dodajajo preizkuse
-admin lahko dodaja in briše preizkuse
```