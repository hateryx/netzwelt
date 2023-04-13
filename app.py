from flask import Flask, request, render_template, redirect, session
import requests
from helpers import login_required, territory_tree

app = Flask(__name__)
app.secret_key = "netzweltchallenge"


@app.route('/')
@login_required
def index():

    current_user = session["user_id"]
    user_displayName = session['displayName']
    user_role = session['roles']

    try:
        url = 'https://netzwelt-devtest.azurewebsites.net/Territories/All'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
        else:
            response.raise_for_status()

    except requests.RequestException as error:
        return render_template("index.html", error=error)

    territories_list = data['data']

    territories = territory_tree(territories_list)

    return render_template("index.html", territories=territories, user=user_displayName)


@app.route('/login', methods=['GET', 'POST'])
def login():

    session.clear()

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
                data = response.json()

                session["user_id"] = data['username']
                session["displayName"] = data["displayName"]
                session["roles"] = data["roles"]
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
    app.run()
