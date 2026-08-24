from datetime import date

from bottle import Bottle, run, template, request, redirect, response
from db import *

app = Bottle()

SECRET = "TOP_SECRET_1984"

@app.get('/')
def index():
    pov = ustvari_povezavo()
    preizkusi = PisniPreizkus.vsi(pov)

    podatki = [opis_preizkusa(pov, p) for p in preizkusi]
    user = get_user()

    # sortiranje po datumu (najbolj zgodnji na vrhu)
    # če uporabnik ni admin, prikažemo samo preizkuse, ki so danes ali v prihodnosti
    
    if user and user.vloga == "admin":
        podatki = sorted(podatki, key=lambda p: p["datum_iso"])
    else:
        podatki = [p for p in podatki if p["datum_iso"] >= date.today().isoformat()]

    pov.close()
    return template('index', podatki=podatki, user=user, title="Domov")


def get_user():
    user_id = request.get_cookie("user_id", secret=SECRET)
    if not user_id:
        return None

    pov = ustvari_povezavo()
    user = Uporabnik.najdi(pov, int(user_id))
    pov.close()
    return user


@app.get('/prijava')
def prijava_get():
    return template('prijava', napaka=None, title="Prijava", user=None)


@app.post('/prijava')
def prijava_post():
    email = request.forms.get('email')
    geslo = request.forms.get('geslo')

    pov = ustvari_povezavo()
    user = Uporabnik.najdi_po_emailu(pov, email)


    if user and preveri_geslo(geslo, user.zgostitev, user.sol):
        pov.close()
        return prijavi_uporabnika(user)

    pov.close()
    return template('prijava', napaka="Napačen email ali geslo.", title="Prijava", user=None)


def zahtevaj_prijavo():
    if not get_user():
        return redirect('/prijava')


def prijavi_uporabnika(user):
    response.set_cookie("user_id", str(user.id), secret=SECRET)
    response.set_cookie("vloga", user.vloga, secret=SECRET)
    return redirect('/')


@app.get('/odjava')
def odjava():
    response.delete_cookie("user_id")
    response.delete_cookie("vloga")
    return redirect('/')


@app.get('/registracija')
def registracija_get():
    return template('registracija', napaka=None, title="Registracija", ime="", email="", user=None)


@app.post('/registracija')
def registracija_post():
    ime = request.forms.get('ime')
    email = request.forms.get('email')
    geslo = request.forms.get('geslo')

    pov = ustvari_povezavo()

    if Uporabnik.najdi_po_emailu(pov, email):
        pov.close()
        return template('registracija',
                        napaka="Ta email je že v uporabi.",
                        title="Registracija",
                        ime=ime,
                        email=email,
                        user=None)

    if not ime or not email or not geslo:
        pov.close()
        return template('registracija',
                        napaka="Vsa polja morajo biti izpolnjena.",
                        title="Registracija",
                        ime=ime,
                        email=email,
                        user=None)

    user = Uporabnik.ustvari(pov, ime, email, geslo)


    response.set_cookie("user_id", str(user.id), secret=SECRET)
    response.set_cookie("vloga", user.vloga, secret=SECRET)
    pov.close()

    return redirect('/')


@app.get('/dodaj-preizkus')
def dodaj_preizkus_get():
    user = get_user()
    if not user:
        return redirect('/prijava')

    pov = ustvari_povezavo()
    predmeti = Predmet.vsi(pov)
    letniki = Letnik.vsi(pov)
    predavalnice = Predavalnica.vsi(pov)
    tipi = TipTesta.vsi(pov)
    teme = Tema.vsi(pov)
    predmeti_dict = {p.id: p.ime for p in predmeti}


    pov.close()
    return template(
        'dodaj_preizkus',
        predmeti=predmeti,
        letniki=letniki,
        predavalnice=predavalnice,
        tipi=tipi,
        napaka=None,
        datum=None,
        ura=None,
        user=user,
        title="Dodaj pisni preizkus",
        teme=teme,
        predmeti_dict=predmeti_dict)

def _napaka_dodaj_preizkus(pov, user, napaka, datum=None, ura=None):
    """Znova pridobi vse podatke za obrazec 'dodaj_preizkus' in prikaže sporočilo o napaki."""
    predmeti = Predmet.vsi(pov)
    letniki = Letnik.vsi(pov)
    predavalnice = Predavalnica.vsi(pov)
    tipi = TipTesta.vsi(pov)
    teme = Tema.vsi(pov)
    predmeti_dict = {p.id: p.ime for p in predmeti}
    pov.close()
    return template(
        'dodaj_preizkus',
        predmeti=predmeti,
        letniki=letniki,
        predavalnice=predavalnice,
        tipi=tipi,
        teme=teme,
        predmeti_dict=predmeti_dict,
        napaka=napaka,
        datum=datum,
        ura=ura,
        user=user,
        title="Dodaj pisni preizkus"
    )

@app.post('/dodaj-preizkus')
def dodaj_preizkus_post():
    user = get_user()
    if not user:
        return redirect('/prijava')

    pov = ustvari_povezavo()

    datum = request.forms.get('datum')
    ura = request.forms.get('ura')
    id_predmet = request.forms.get('predmet')
    id_letnik = request.forms.get('letnik')
    id_predavalnica = request.forms.get('predavalnica')
    id_tip = request.forms.get('tip')

    seznam_tem = request.forms.getall('teme')
    seznam_tem = [int(t) for t in seznam_tem if t.isdigit()]

    # Preverimo, ali so vsi potrebni podatki prisotni
    if not (datum and ura and id_predmet and id_letnik and id_predavalnica and id_tip):
        return _napaka_dodaj_preizkus(pov, user, "Manjkajo podatki.", datum=datum, ura=ura)

    try:
        if date.fromisoformat(datum) < date.today():
            return _napaka_dodaj_preizkus(pov, user, "Datum preizkusa ne more biti v preteklosti.", datum=datum, ura=ura)
    except ValueError:
        return _napaka_dodaj_preizkus(pov, user, "Neveljavna oblika datuma.", datum=datum, ura=ura)

    predmet_obj = Predmet.najdi(pov, int(id_predmet))
    if predmet_obj is None or predmet_obj.id_letnik != int(id_letnik):
        return _napaka_dodaj_preizkus(pov, user, "Izbrani predmet ne pripada izbranemu letniku.", datum=datum, ura=ura)

    veljavne_teme = {t.id for t in Tema.za_predmet(pov, int(id_predmet))}
    if not all(id_teme in veljavne_teme for id_teme in seznam_tem):
        return _napaka_dodaj_preizkus(pov, user, "Izbrane teme ne pripadajo izbranemu predmetu.", datum=datum, ura=ura)

    ustvari_preizkus(
        pov, datum, ura, id_predavalnica, id_letnik, id_predmet, id_tip, seznam_tem
    )
    pov.close()

    return redirect('/')


@app.get('/izbrisi/<id:int>')
def izbrisi_preizkus(id):
    user = get_user()
    if not user or user.vloga != "admin":
        return redirect('/prijava')

    pov = ustvari_povezavo()
    preizkus = PisniPreizkus.najdi(pov, id)
    if preizkus:
        preizkus.izbrisi(pov)
    pov.close()

    return redirect('/')


run(app, debug=True, reloader=True)