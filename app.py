# importing modules from flask library
from flask import Flask, render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)


# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():
    name = "me"  # write your name
    age = "17"  # write your age

    return render_template("index.html", me="none", name=name, age=age)


# define the route to father webpage


@app.route("/father")
def father():
    name = "father"  # write your name
    age = "100"  # write your age

    return render_template("father.html", name=name, age=age)


# define the route to mother webpage
@app.route("/mother")
def mother():
    name = "mother"  # write your name
    age = "100"  # write your age

    return render_template("mother.html", name=name, age=age)


# define the route to friends webpage
@app.route("/friends")
def friends():
    name = "friends"  # write your name
    age = "0"  # write your age

    return render_template("friend.html", name=name, age=age)


# add other routes, if you want
@app.route("/monster")
def me():
    name = "monster"  # write your name
    age = "99999+"  # write your age

    return render_template("index.html", me="none", name=name, age=age)


# run the file
if __name__ == "__main__":
    app.run(debug=True)
