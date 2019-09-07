from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")



@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    name_from_form = request.form['name']
    email_from_form = request.form['email']
    password_from_form = request.form['password']
    confirm_password_from_form = request.form['password']
    file_upload_from_form = request.form['user_upload']
    date_created_from_form = request.form['date_created']
    return render_template("show.html", name_on_template=name_from_form, email_on_template=email_from_form, password_on_template=password_from_form, confirm_password_on_template=confirm_password_from_form, file_on_template=file_upload_from_form, date_on_template=date_created_from_form)





if __name__ == "__main__":
    app.run(debug=True)