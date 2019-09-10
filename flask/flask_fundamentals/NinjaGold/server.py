from flask import Flask, render_template, request, redirect, session
import random
from datetime import datetime
app = Flask(__name__)
app.secret_key = 'There are infinities within the mind of the ninja.'

@app.route('/')
def home():
    if 'amount_gold' not in session:
        session['amount_gold'] = 0
    if 'activities' not in session:
        session['activities'] = []
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process_money():
    now = datetime.now()
    date_time = now.strftime("%B, %d, %Y at %H:%M")
    # if request.form['building'] == 'reset':
    #     session.clear()
    #     return redirect('/')
    if request.form['building'] == 'cave':
        place = 'farm'
        gold = random.randint(10,20)
        session['amount_gold'] += gold
    if request.form['building'] == 'house':
        place = 'cave'
        gold = random.randint(5,10)
        session['amount_gold'] += gold
    if request.form['building'] == 'casino':
        place = 'casino'
        gold = random.randint(-50,50)
        session['amount_gold'] = gold

if __name__ == "__main__":
    app.run(debug=True)