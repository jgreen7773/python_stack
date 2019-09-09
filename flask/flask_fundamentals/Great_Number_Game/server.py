from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'The master squishes us.'

@app.route('/')
def GNG():
    if not 'randint' in session:
        session['randint'] = random.randint(1, 100)
    return render_template('index.html')

@app.route('/guess', methods=['post'])
def redirect_session():
    option1 = "You're too high!"
    option2 = "Wow, I didn't actually think you would guess it...."
    option3 = "Hahaha! You're too low!"
    if int(request.form['guess']) > session['randint']:
        session['reply'] = option1
    elif int(request.form['guess']) == session['randint']:
        session['reply'] = option2
        session['realnumber'] = session['randint']
    else:
        session['reply'] = option3
    return redirect('/')

@app.route('/refresh')
def play_again():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)