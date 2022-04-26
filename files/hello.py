from bottle import Bottle, run

app = Bottle()

@app.route('/hello')
def hello():
    return "<h1>Hello World!</h1>"

run(app, reloader=True, host='localhost', port=8080)