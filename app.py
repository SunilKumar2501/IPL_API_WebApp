from flask import Flask, render_template,request
import requests
app = Flask(__name__)

@app.route('/')
def home():
    response = requests.get('http://127.0.0.1:5000/api/teams')
    teams = response.json()["teams"]
    # print(teams)
    return render_template("index.html",teams = sorted(teams))
@app.route("/teamvteam")
def team_vs_team():
    response = requests.get('http://127.0.0.1:5000/api/teams')
    teams = response.json()["teams"]
    team1 = request.args.get("team1")
    team2 = request.args.get("team2")
    response1 = requests.get('http://127.0.0.1:5000/api/teamvteam?team1={}&team2={}'.format(team1,team2))
    response1 =  response1.json()
    return render_template("index.html",result = response1,teams = sorted(teams))
app.run(debug = True,port = 8000)
