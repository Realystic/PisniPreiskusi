pov —  povezava (SQLite connection), do baze, ki ga funkcije uporabljajo za izvajanje SQL poizvedb  
## Razredi:
### Letnik
#### letnik na faksu, npr APM2
    Atributi:
    - id: primarni ključ
    - letnik: ime letnika (npr. "1. letnik")  

    Metode:
    - shrani(pov): shrani nov objekt ali posodobi obstoječega iz istim id
    - izbrisi(pov): izbriše letnik
    - najdi(pov, id): vrne en letnik ali None
    - vsi(pov): vrne seznam vseh letnikov

### Predmet
#### predmet, ki pripada določenemu letniku, npr PB1
    Atributi:
    - id
    - ime
    - id_letnik — tuj ključ na tabelo letniki, ki povezuje letnik in predmet 

    Metode:  
    - shrani(pov): shrani nov objekt ali posodobi obstoječega iz istim id
    - izbrisi(pov)
    - najdi(pov, id): vrne ime letnika z id-jem id; vrne None, če ni letnika s tem id-jem
    - za_letnik(pov, id_letnik): vrne predmete za letnik z id-jem id_letnik
    - vsi(pov): vrne seznam vseh predmetov

### Tema 
#### učna tema, ki pripada predmetu (npr. SQL)
    Atributi:
    - id
    - tema
    - id_predmet — FK na Predmet  

    Metode:
    - shrani(pov): shrani nov objekt ali posodobi obstoječega iz istim id
    - izbrisi(pov)
    - najdi(pov, id) - vrne ime teme z id-jem id; vrne None, če ni id-ja v bazi
    - za_predmet(pov, id_predmet) - vrne teme določenega predmeta z id-jem id_predmet
    - za_preizkus(pov, id_test) - vrne teme povezane s preizkusom z id-jem id_test
    - vse(pov) - vrne seznam vseh tem


### Predavalnica 
#### učilnica, kjer se izvaja pisni preizkus, npr 3.10
    Atributi:
    - id
    - ime  

    Metode:
    - shrani(pov): shrani nov objekt ali posodobi obstoječega iz istim id
    - izbrisi(pov)
    - najdi(pov, id): vrne predavalnico z id-jem id; vrne None, če id-ja ni
    - vse(pov): vrne seznam vseh objektov

### TipTesta 
#### tip pisnega preizkusa: kolokvij/izpit
    Atributi:
    - id
    - tip
    Metode:
    - shrani(pov): shrani nov objekt ali posodobi obstoječega iz istim id
    - izbrisi(pov)
    - najdi(pov, id): vrne tip testa z id-jem id; vrne None, če id-ja ni
    - vsi(pov): vrne seznam vseh tipov testa 

### PisniPreizkus 
#### pisni preizkus, ki je povezan z letnikom, predmetom, predavalnico, tipom testa - s temami pa je povezan s funkcijo Tema.zaPreizkus() 
    Atributi:
    - id
    - datum
    - ura
    - id_predavalnica - FK na Predavalnica
    - id_letnik - FK na Letnik
    - id_predmet - FK na Predmet
    - id_tip - FK na tip
    Metode:
    - shrani(pov): ustvari ali posodobi preizkus
    - izbrisi(pov)
    - najdi(pov, id): vrne objekt PisniPreizkus z id-jem id
    - vsi(pov): vrne seznam vseh pisnih preizkusov, urejenih po datumu in uri
    - na_dan(pov, datum)
    - za_predmet(pov, id_predmet)
    - za_letnik(pov, id_letnik)
    - za_predavalnico(pov, id_predavalnica)


### Uporabnik
#### Registrirani uporabnik spletnega vmesnika
    Atributi:
    - id
    - ime
    - email
    - zgostitev
    - vloga (privzeto student)
    Metode:
    - shrani(pov) — ustvari novega uporabnika ali posodobi obstoječega
    - izbrisi(pov) — izbriše uporabnika iz baze
    - najdi(pov, id) — poišče uporabnika po ID-ju
    - najdi_po_emailu(pov, email) — poišče uporabnika po e‑pošti
    - vsi(pov) — vrne seznam vseh uporabnikov
    - ustvari(pov, ime, email, geslo, vloga="student") — zgošči geslo, ustvari sol, nastavi vlogo in shrani novega uporabnika v bazo



Pomožne funkcije (funkcije.py):
-ustvari_povezavo()
        Ustvari SQLite povezavo in omogoči tuje ključe.
-dodaj_temo_preizkusu(pov, id_teme, id_test)
        Doda zapis v povezovalno tabelo povezovalna_teme_testi.
-ustvari_preizkus(pov, datum, ura, id_predavalnica, id_letnik, id_predmet, id_tip, seznam_tem)
    Ustvari nov pisni preizkus in ga poveže s seznamom tem.
-opis_preizkusa(pov, preizkus)
    Vrne lep opis preizkusa z imeni (ne ID-ji):
    - predmet
    - letnik
    - predavalnica
    - tip testa
    - seznam tem
