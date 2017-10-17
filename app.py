from bottle import get,run,Bottle

app = Bottle()

@app.get('/')
def welcome():
    return "Hello, welcome to knowurcoding! This is automatically deployed. Attemp 1. Attemp 2."


