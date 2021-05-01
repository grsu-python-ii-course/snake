from random import randint

from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return f'Blank Page'


@app.route('/game', methods=['POST'])
def game():
    req = request.get_json(silent=True)
    print(req)
    # YOU CODE HERE FOR SELECT NEXT SHOOT | USE req DATA
    return jsonify({"x": randint(0, 15), "y": randint(0, 15)})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
