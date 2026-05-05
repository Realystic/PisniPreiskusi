from bottle import Bottle, run, template, request, redirect, TEMPLATE_PATH, response
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from db.pisni_preizkusi import PisniPreizkus
from db.predmeti import Predmet
from db.letniki import Letnik
from db.predavalnice import Predavalnica
from db.tipi_testov import TipTesta
from db.funkcije import ustvari_povezavo, opis_preizkusa
from db.uporabniki import Uporabnik
from db.geslo import preveri_geslo


app = Bottle()

SECRET = "TOP_SECRET_1984"

# Da Bottle najde views
TEMPLATE_PATH.insert(0, os.path.join(os.path.dirname(__file__), 'views'))

@app.get('/')
def index():
    pov = ustvari_povezavo()
    preizkusi = PisniPreizkus.vsi(pov)

    podatki = [opis_preizkusa(pov, p) for p in preizkusi]

    # sortiranje po datumu (najbolj zgodnji na vrhu)
    podatki = sorted(podatki, key=lambda p: p["datum_iso"])

    user = get_user()
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


    if user and preveri_geslo(geslo, user.geslo_hash, user.sol):
        pov.close()
        return prijavi_uporabnika(user)

    pov.close()
    return template('prijava', napaka="Napačen email ali geslo.", title="Prijava", user=None)



def zahtevaj_prijavo():
    if not get_user():
        redirect('/prijava')

def prijavi_uporabnika(user):
    response.set_cookie("user_id", str(user.id), secret=SECRET)
    response.set_cookie("vloga", user.vloga, secret=SECRET)
    redirect('/')


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
        return template('registracija',
                        napaka="Ta email je že v uporabi.",
                        title="Registracija",
                        ime=ime,
                        email=email,
                        user=None)

    if not ime or not email or not geslo:
        return template('registracija',
                        napaka="Vsa polja morajo biti izpolnjena.",
                        title="Registracija",
                        ime=ime,
                        email=email,
                        user=None)

    user = Uporabnik.ustvari(pov, ime, email, geslo)


    response.set_cookie("user_id", str(user.id), secret=SECRET)
    response.set_cookie("vloga", user.vloga, secret=SECRET)

    return redirect('/')

@app.get('/dodaj-preizkus')
def dodaj_preizkus_get():
    user = get_user()
    if not user:
        redirect('/prijava')

    pov = ustvari_povezavo()
    predmeti = Predmet.vsi(pov)
    letniki = Letnik.vsi(pov)
    predavalnice = Predavalnica.vse(pov)
    tipi = TipTesta.vsi(pov)

    return template(
        'dodaj_preizkus',
        predmeti=predmeti,
        letniki=letniki,
        predavalnice=predavalnice,
        tipi=tipi,
        napaka=None,
        user=user,
        title="Dodaj pisni preizkus"
    )



@app.post('/dodaj-preizkus')
def dodaj_preizkus_post():
    user = get_user()
    if not user:
        redirect('/prijava')

    pov = ustvari_povezavo()

    datum = request.forms.get('datum')
    ura = request.forms.get('ura')
    id_predmet = request.forms.get('predmet')
    id_letnik = request.forms.get('letnik')
    id_predavalnica = request.forms.get('predavalnica')
    id_tip = request.forms.get('tip')

    if not (datum and ura and id_predmet and id_letnik and id_predavalnica and id_tip):
        return template('dodaj_preizkus', napaka="Manjkajo podatki.", user=user, title="Dodaj pisni preizkus")

    p = PisniPreizkus(
        datum=datum,
        ura=ura,
        id_predavalnica=id_predavalnica,
        id_letnik=id_letnik,
        id_predmet=id_predmet,
        id_tip=id_tip
    )

    p.shrani(pov)
    redirect('/')

@app.get('/izbrisi/<id:int>')
def izbrisi_preizkus(id):
    user = get_user()
    if not user or user.vloga != "admin":
        redirect('/prijava')

    pov = ustvari_povezavo()
    preizkus = PisniPreizkus.najdi(pov, id)
    if preizkus:
        preizkus.izbrisi(pov)


    redirect('/')




if __name__ == "__main__":
    run(app, host='localhost', port=8080, debug=True, reloader=True)