from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def root_index():
    return render_template('index.html')



@app.route('/checkout', methods=['POST'])
def checkout_index():
    qone = request.form['qone']
    qtwo = request.form['qtwo']
    qthree = request.form['qthree']
    name = request.form['username']
    student_id = request.form['student_id']
    total = int(qone)+int(qtwo)+int(qthree)
    return render_template('checkout.html', qone_post=qone, qtwo_post=qtwo, qthree_post=qthree, name_post=name, student_id_post=student_id, total_quantity=total)



@app.route('/fruits')
def fruits_index():
    return render_template('fruits.html')

if __name__ == "__main__":
    app.run(debug=True)