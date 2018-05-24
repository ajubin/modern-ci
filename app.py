import os
import signal

from flask import Flask, request
from model.factorial import factorial

if not os.environ['FLASK_ENV']:
    os.environ['FLASK_ENV'] = 'development'

app = Flask(__name__)

signal.signal(signal.SIGINT, lambda s, f: os._exit(0))

@app.route("/", methods=['GET', 'POST'])
def index():
    number = request.args.get("n")
    if number:
        number = int(number)
        return "factorial({}) = {}".format(number, factorial(number))
    return 'post a number'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
