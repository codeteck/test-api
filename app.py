from flask import Flask, jsonify, make_response

app = Flask(__name__)


@app.route('/')
def index():
    return make_response(jsonify({
        'message': 'Hello World'
    }))


if __name__ == '__main__':
    app.run(debug=True)





