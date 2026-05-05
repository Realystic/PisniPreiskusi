Razredi:
Letnik (Letnik n faksu, npr APM2)
    Atributi
    - id: primarni ključ
    - letnik: ime letnika (npr. "1. letnik")
    Metode
    - shrani(pov): ustvari ali posodobi letnik
    - izbrisi(pov): izbriše letnik
    - najdi(pov, id): vrne en letnik ali None
    - vsi(pov): vrne seznam vseh letnikov

Predmet (Predmet, ki pripada določenemu letniku, npr PB1)
    Atributi
    - id
    - ime
    - id_letnik: FK na Letnik
    Metode
    - shrani(pov)
    - izbrisi(pov)
    - najdi(pov, id)
    - za_letnik(pov, id_letnik)
    - vsi(pov)

Tema (Učna tema, ki pripada predmetu (npr. SQL).)
    Atributi
    - id
    - tema
    - id_predmet — FK na Predmet
    Metode
    - shrani(pov)
    - izbrisi(pov)
    - najdi(pov, id)
    - za_predmet(pov, id_predmet) — vrne teme določenega predmeta
    - za_preizkus(pov, id_test) — vrne teme povezane s preizkusom
    - vse(pov)


Predavalnica (Učilnica, kjer se izvaja pisni preizkus, npr 3.10)
    Atributi
    - id
    - ime
    Metode
    - shrani(pov)
    - izbrisi(pov)
    - najdi(pov, id)
    - vse(pov)

TipTesta (Tip pisnega preizkusa, kolokvij/izpit).
    Atributi
    - id
    - tip
    Metode
    - shrani(pov)
    - izbrisi(pov)
    - najdi(pov, id)
    - vsi(pov)

PisniPreizkus (pisni preizkus, ki je povezan z letnikom, predmetom, predavalnico, tipom testa in seznamom tem.)
    Atributi
    - id
    - datum
    - ura
    - id_predavalnica
    - id_letnik
    - id_predmet
    - id_tip
    Metode
    - shrani(pov): ustvari ali posodobi preizkus
    - izbrisi(pov)
    - najdi(pov, id)
    - vsi(pov)
    - na_dan(pov, datum)
    - za_predmet(pov, id_predmet)
    - za_letnik(pov, id_letnik)
    - za_predavalnico(pov, id_predavalnica)
    - v_obdobju(pov, datum_od, datum_do)


Uporabnik (Registrirani uporabnik spletnega vmesnika)
    Atributi
    - id
    - ime
    - email
    - geslo_hash
    - vloga (privzeto student)
    Metode
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
