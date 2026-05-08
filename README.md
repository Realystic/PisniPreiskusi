# Naslov projekta: Pisni Preiskusi
## Namen projekta: Pregled in urejanje pisnih preizkusov na FMF

### Predstavitev baze:
![ER diagram podatkovne baze](docs\ER.png)

## Funkcionalnosti:
### Tekstovni vmesnik:
Prvi del: "Upravljanje pisnih preizkusov" povsem deluje:
- pregled vseh pisnih preizkusov
- dodajanje novih pisnih preizkusov
- pregled preizkusov po:
  - datumu
  - letniku
  - predmetu
- brisanje preizkusov  

Drugi del: "Upravljanje podatkov" je pa (še) ZELO okrnjen

### Spletni vmesnik:
- vsi lahko vidijo kateri pisni preizusi so vnešeni
- registracija novega uporabnika (z emailom, ki ga še ni v bazi)
- uporabniki lahko dodajajo preizkuse
- admin lahko dodaja in briše preizkuse  
- že vnešena uporabniška računa:
  - ime: admin | email:admin@fmf.si | geslo: 123
  - ime: upor | email: upor@bnik.si | geslo: abnik
## Navodila za uporabo:
1. ukaz za vzpostavitev baze podatkov: 
```bash 
python -m stvaritev_baze.naredi_bazo
```

2. ukaz za zagon tekstovnega vmesnika: 
```bash 
python -m tekstovni_vmesnik 
```

3. ukaz za zagon spletnega vmesnika: 
```bash 
python -m spletni_vmesnik
```

### Avtorja: 
Štefan Ilja & Franc Križanič