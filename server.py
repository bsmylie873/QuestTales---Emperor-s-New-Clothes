from flask import Flask,render_template, request,jsonify,Response

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def home():
    return '<h1> Hello World </h1><p>My name is Brandon</p>'

if __name__ == '__main__':
    app.run(host ='0.0.0.0', port = 6789, debug = True)