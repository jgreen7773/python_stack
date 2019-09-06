# import and 1st route creation
from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World!'

# 2nd route created
@app.route('/success')
def success():
    return "success"


# 3rd route and adding variable rules to routes
@app.route('/hello/<name>') # for any route format: '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def hello(name):
    print(name)
    return "Hello, " + name


# We can add as many of these routes as we need, giving each variable a different name:
@app.route('/users/<username>/<id>') # for any route format: '/users/____/____', two parameters in the url get passed as username and id
def show_user_profile(username, id):
    print(username)
    print(id)
    return "username: " + username + ", id: " + id
# The "('/users/<username>/<id>')" part of the @app.route method just tells which FUNCTION is invoked below.
# Notice the "username", and "id", in the "def show_user_profile()" function?


@app.route('/lists')
def render_lists():
    # Soon enough, we'll get data from a database, but for now, we're hard coding data
    student_info = [
        {'name' : 'Michael', 'age' : 35},
        {'name' : 'John', 'age' : 30},
        {'name' : 'Mark', 'age' : 25},
        {'name' : 'KB', 'age' : 27}
    ]
    return render_template("lists.html", random_numbers = [3,1,5], students = student_info)

if __name__=="__main__":
    app.run(debug=True)

