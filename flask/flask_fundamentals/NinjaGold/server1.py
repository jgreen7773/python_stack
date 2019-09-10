from flask import Flask, render_template, request, redirect, session
import random
from datetime import datetime
app = Flask(__name__)
app.secret_key = 'There are infinities within the mind of the ninja.'

@app.route('/')
def home():
    if not 'amount_gold' in session:
        session['amount_gold'] = 0
    if not 'activities' in session:
        session['activity_log'] = []
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process_money():
    date_time = datetime.now()
    date_time = ['%B, %d, %Y, %H:%M']
    if request.form['building'] == 'farm':
        place = 'farm'
        gold = random.randint(10,20)
        session['amount_gold'] += int(gold)
        session['activity_log'] = print("You have visited {place} and gained {gold} gold! {date_time}")
        return redirect('/')
    if request.form['building'] == 'cave':
        place = 'cave'
        gold = random.randint(5,10)
        session['amount_gold'] += int(gold)
        session['activity_log'] = print("You have visited {place} and gained {gold} gold! {date_time}")
        return redirect('/')
    if request.form['building'] == 'house':
        place = 'house'
        gold = random.randint(2,5)
        session['amount_gold'] += int(gold)
        session['activity_log'] = print("You have visited {place} and gained {gold} gold! {date_time}")
        return redirect('/')
    if request.form['building'] == 'casino':
        place = 'casino'
        gold = random.randint(-50,50)
        session['amount_gold'] += int(gold)
        session['activity_log'] = print("You have visited {place} gained {gold} gold! {date_time}")
        return redirect('/')

@app.route('/play_again')
def play_again():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)