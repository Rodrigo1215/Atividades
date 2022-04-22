import os
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/request')
def index2():
    return render_template('request.html')


@app.route('/json')
def index5():
    return render_template('json.html')


@app.route('/api/request', methods=['POST'])
def request_user():
    nome = request.form['nome']
    email = request.form['email']
    print(nome)
    print(email)
    return jsonify(nome=nome, email=email)


@app.route('/api/json', methods=['POST'])
def json_user():

    json = request.get_json()
    nome = json['nome']
    email = json['email']
    return jsonify(nome=nome, email=email)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True)
