from bottle import Bottle, template, request, redirect, TEMPLATE_PATH
import os

app = Bottle()

SECRET = "TOP_SECRET_1984"

# Naj Bottle najde views mapo
TEMPLATE_PATH.insert(0, os.path.join(os.path.dirname(__file__), 'views'))

@app.get('/')
def index():
    return template('index')

def get_user():
    return request.get_cookie("user", secret=SECRET)

@app.get('/prijava')
def prijava_get():
    return template('prijava')

@app.post('/prijava')
def prijava_post():
    uporabnik = request.forms.get('uporabnik')
    geslo = request.forms.get('geslo')

    if uporabnik == "admin" and geslo == "1234":
        response.set_cookie("user", uporabnik, secret=SECRET)
        return redirect('/podatki')
    else:
        return "<h2>Napačno uporabniško ime ali geslo.</h2>"

@app.get('/odjava')
def odjava():
    response.delete_cookie("user")
    return redirect('/')


@app.get('/podatki')
def podatki():
    user = get_user()
    if not user:
        return redirect('/prijava')
    return f"<h2>Pozdravljen, {user}!</h2><p>To je zaščitena stran.</p>"