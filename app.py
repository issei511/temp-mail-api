#from flask import Flask, render_template
from flask import *
import requests as r
app = Flask(__name__)
@app.route('/')
def index():
	return render_template("index.html")
@app.route('/request',methods=['POST'])
def req():
	res = r.get(request.form['url'])
	return res.text



if __name__ == '__main__':
	app.run(debug = True)