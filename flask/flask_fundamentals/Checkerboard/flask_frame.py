from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')



@app.route('/4')
def half_board():
    return render_template('index2.html')



@app.route('/<int:x>/<int:y>')
def custom_board(x, y):
    return render_template('index3.html', x=x, y=y)



if __name__ == "__main__":
    app.run(debug=True)