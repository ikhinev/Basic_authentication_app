from flask import Flask, render_template, request

app = Flask(__name__)

regdetails = {}
@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template('register.html')
    else:
        data = request.form
        fullname = data.get("fullname")
        username = data.get("username")
        password = data.get("password")

        regdetails["fullname"] = fullname
        regdetails["username"] = username
        regdetails["password"] = password

        return render_template('login.html')


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template('login.html')
    else:
        data = request.form
        username = data.get("username")
        password = data.get("password")

        if regdetails.get("username") == username and regdetails.get("password") == password:
            return "welcome to your account"
        else:
            return "wrong details"

app.run(debug=True)        