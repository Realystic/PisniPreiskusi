from bottle import Bottle, template

app = Bottle()

@app.get('/')
def index():
    return "<h1>Deluje!</h1>"