from flask import Flask, request, render_template, redirect
import requests

app = Flask(__name__)


@app.route('/')
def index():
    try:
        url = 'https://netzwelt-devtest.azurewebsites.net/Territories/All'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
        else:
            response.raise_for_status()

    except requests.RequestException as error:
        return render_template("index.html", error=error)

    territories = data['data']

    return render_template("index.html", territories=territories)


@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == "POST":
        try:
            url = 'https://netzwelt-devtest.azurewebsites.net/Account/SignIn'

            username = request.form.get("username")
            password = request.form.get("password")
            headers = {'Content-Type': 'application/json'}

            data = {
                "username": username,
                "password": password
            }

            response = requests.post(url, json=data, headers=headers)

            if response.status_code == 200:
                data = response
                return redirect("/")
            else:
                error_json = response.json()
                error = error_json["message"]
                return render_template("login.html", error=error)

        except Exception as error:
            return render_template("login.html", error=error)

    if request.method == 'GET':
        return render_template("login.html")


if __name__ == '__main__':
    app.run(debug=True)
