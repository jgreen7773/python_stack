from flask import Flask, flash, redirect, render_template, \
    request, url_for
app = Flask (__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def helloWorld():
    return 'Hello World!'

@app.route('/dojo')
def helloDojo():
    return 'Dojo!'

@app.route('/say/<name>')
def helloFlask(name):
    return "Hi, " + str(name)

@app.route('/say/<name>')
def helloMichael(name):
    return 'Hi ' + str(name)

@app.route('/say/<john>')
def helloJohn(john):
    return 'Hi ' + str(john)

@app.route('/repeat/<hello>/<amount>')
def hello(hello, amount):
    # print("{}".format(hello) * int(amount))
    return hello * int(amount)

@app.route('/repeat/80/bye')
def bye():
    return 'bye'*80

@app.route('/repeat/99/dogs')
def dogs():
    return 'dogs'*99


if __name__ == "__main__":
    app.run(debug=True)