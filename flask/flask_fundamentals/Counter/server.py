from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'I\'ll buy it at a high price, stranger.'

@app.route('/')
def counter():
    if 'counter' in session:
        session['counter'] += 1
    else:
        session['counter'] = 1
    return render_template('index.html')



@app.route('/counter2')
def counter_2():
    session['counter'] += 1
    return redirect('/')



@app.route('/destroy_session')
def clear_session():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)