from flask import Flask, render_template
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


if __name__ == '__main__':
    app.run(debug=True)
