from django.shortcuts import render, redirect, HttpResponse
import random
from datetime import datetime

def index(request):
    if request.method == 'GET':
        if 'amount_gold' not in request.session:
            request.session['amount_gold'] = 0
        if 'activity_log' not in request.session:
            request.session['activity_log'] = []
        if 'counter' not in request.session:
            request.session['counter'] = 0
        if request.session['counter'] == 15:
            request.session['fail'] = "You failed! Please try again...."
        return render(request, 'ninja_gold_app/index.html')

def process_money(request):
    date_time = datetime.now()
    if request.method == 'POST':
        if request.POST['building'] == 'farm':
            place = 'farm'
            gold = random.randint(10,20)
            request.session['amount_gold'] += int(gold)
            request.session['counter'] += 1
            message = f"You have visited {place} and gained {gold} gold! {date_time}"
            request.session['activity_log'].insert(0, message)
            return redirect('/')
        if request.POST['building'] == 'cave':
            place = 'cave'
            gold = random.randint(5,10)
            request.session['amount_gold'] += int(gold)
            request.session['counter'] += 1
            message = f"You have visited {place} and gained {gold} gold! {date_time}"
            request.session['activity_log'].insert(0, message)
            return redirect('/')
        if request.POST['building'] == 'house':
            place = 'house'
            gold = random.randint(2,5)
            request.session['amount_gold'] += int(gold)
            request.session['counter'] += 1
            message = f"You have visited {place} and gained {gold} gold! {date_time}"
            request.session['activity_log'].insert(0, message)
            return redirect('/')
        if request.POST['building'] == 'casino':
            place = 'casino'
            gold = random.randint(-50,50)
            request.session['amount_gold'] += int(gold)
            request.session['counter'] += 1
            message = f"You have visited {place} and gained {gold} gold! {date_time}"
            request.session['activity_log'].insert(0, message)
            return redirect('/')
    return redirect('/')

def reset(request):
    if request.method == "POST":
        request.session.clear()
    return redirect('/')