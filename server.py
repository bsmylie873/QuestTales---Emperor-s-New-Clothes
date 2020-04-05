from flask import Flask,render_template, request,jsonify,Response

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(host ='0.0.0.0', port = 6789, debug = True)