from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def main_page_and_boxes():
    return render_template('play.html')


@app.route('/play/<int:times>')
def repeatingboxes(times):
    return render_template('play.html', times=times)


@app.route('/play/<int:times>/<color>')
def numberofboxes(times, color):
    return render_template('play.html', times=times, color=color)


if __name__ == "__main__":
    app.run(debug=True)