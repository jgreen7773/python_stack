from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = '8JFj3fAJF"P#INf8!&*@&$*^@#*8fH!#HF*#F'

@app.route('/')
def index():
    return render_template("index.html")



@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    session['name_from_form'] = request.form['name']
    session['email_from_form'] = request.form['email']
    session['password_from_form'] = request.form['password']
    session['confirm_password_from_form'] = request.form['password']
    session['file_upload_from_form'] = request.form['user_upload']
    return redirect("/show")



@app.route('/show')
def show_user():
    print("Showing the User Info From the Form")
    print(request.form)
    return render_template("show.html", name_on_template=session['name_from_form'], email_on_template=session['email_from_form'], password_on_template=session['password_from_form'], confirm_password_on_template=session['confirm_password_from_form'], file_on_template=session['file_upload_from_form'])

if __name__ == "__main__":
    app.run(debug=True)