from bottle import Bottle, run, template, request, redirect, TEMPLATE_PATH, response
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from db.funkcije import ustvari_povezavo
from db.uporabniki import Uporabnik
from db.geslo import sifriraj_geslo, preveri_geslo


app = Bottle()

SECRET = "TOP_SECRET_1984"

# Naj Bottle najde views mapo
TEMPLATE_PATH.insert(0, os.path.join(os.path.dirname(__file__), 'views'))

@app.get('/')
def index():
    return template('index')

def get_user():
    user_id = request.get_cookie("user_id", secret=SECRET)
    if not user_id:
        return None

    pov = ustvari_povezavo()
    return Uporabnik.najdi(pov, user_id)

@app.get('/prijava')
def prijava_get():
    return template('prijava', napaka=None)

@app.post('/prijava')
def prijava_post():
    email = request.forms.get('uporabnik')
    geslo = request.forms.get('geslo')

    pov = ustvari_povezavo()
    user = Uporabnik.najdi_po_emailu(pov, email)

    if user and preveri_geslo(geslo, user.geslo_hash, user.sol):
        response.set_cookie("user_id", user.id, secret=SECRET)
        response.set_cookie("vloga", user.vloga, secret=SECRET)
        return redirect('/podatki')

    return template('prijava', napaka="Napačen email ali geslo.")

@app.get('/odjava')
def odjava():
    response.delete_cookie("user_id")
    response.delete_cookie("vloga")
    return redirect('/')


@app.get('/podatki')
def podatki():
    user = get_user()
    if not user:
        return redirect('/prijava')
    return f"<h2>Pozdravljen, {user.ime}!</h2><p>To je zaščitena stran.</p>"

if __name__ == "__main__":
    run(app, host='localhost', port=8080, debug=True, reloader=True)