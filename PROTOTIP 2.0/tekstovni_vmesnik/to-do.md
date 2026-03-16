# upravljanje_podatkov.py

## Namen datoteke
Datoteka `upravljanje_podatkov.py` vsebuje **tekstovni uporabniški vmesnik (CLI)** za upravljanje osnovnih podatkov v bazi, kot so letniki, predmeti, teme, predavalnice in tipi testov.  
Ta modul **ne vsebuje SQL kode** – namesto tega uporablja objekte (razrede iz db)
Naloga datoteke je samo:
- prikaz menijev,
- branje uporabniškega vnosa,
- klicanje metod objektov (shrani, izbriši, najdi, vsi).

---

## TO‑DO seznam

### Letniki (primer že narejen)
dodaj_letnik_ui(pov) -> je že
pregled_letnikov_ui(pov)
izbrisi_letnik_ui(pov)

### Predmeti
meni_predmeti(pov)
dodaj_predmet_ui(pov)
pregled_predmetov_ui(pov)
izbrisi_predmet_ui(pov)

### Teme
meni_teme(pov)
dodaj_temo_ui(pov)
pregled_tem_ui(pov)
izbrisi_temo_ui(pov)

### Predavalnice
meni_predavalnice(pov)
dodaj_predavalnico_ui(pov)
pregled_predavalnic_ui(pov)
izbrisi_predavalnico_ui(pov)

### Tipi testov
meni_tipi_testov(pov)
dodaj_tip_testa_ui(pov)
pregled_tipov_testov_ui(pov)
izbrisi_tip_testa_ui(pov)

---

## Navodilo za implementacijo
Vsaka UI funkcija naj sledi istemu vzorcu kot pri letnikih:
1. izpiši meni ali vprašanje,
2. preberi uporabnikov vnos,
3. ustvari objekt (npr. `Predmet(...)`),
4. pokliči `.shrani(pov)` ali `.izbrisi(pov)`,
5. izpiši rezultat.

delaj prosim samo z razredi, ne z sql stavki, če kak razred ne dela, spreminjaj db