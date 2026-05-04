from flask import Flask, jsonify
from flask import request
import requests


app = Flask(__name__)

@app.route("/hello")
def hello():
    return 'API is live'

@app.route("/pokemon/<endpoint>")
def pokemon(endpoint):
    url =  f"https://pokeapi.co/api/v2/pokemon/{endpoint}"
    response = requests.get(url)

    return jsonify(response.json()) if response.status_code == 200 else "Failed to get data"


if __name__ == '__main__':
    app.run(debug=True, port=8080, host="0.0.0.0")
