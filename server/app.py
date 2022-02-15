from flask import Flask, send_from_directory, request, jsonify
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.debug = True

@app.route('/')
def index():
    return send_from_directory(".","base.html", as_attachment=False)

@app.route('/<path:filename>')
def socket_file(filename):
    return send_from_directory("..", filename, as_attachment=False)

@app.after_request
def add_header(response):
  response.headers['Access-Control-Allow-Origin'] = "*"
  response.headers['Access-Control-Allow-Headers'] = "*"

  return response

@app.teardown_appcontext
def shutdown_session(exception=None):
    pass

if __name__ == '__main__':
    app.run()