from flask import Flask, jsonify

api = Flask(__name__)

if __name__ == "__main__":
    api.run(debug=True)

@api.route('/api')
def ola_mundo():
    return jsonify({'text': 'Olá Todo Mundo'})

@api.route('/api/hello_world')
def hello_world():
    return jsonify({'text': 'Hello World'})
