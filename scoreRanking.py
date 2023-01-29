from flask import Flask, jsonify, request
import json

# create the app
app = Flask(__name__)


@app.route("/read", methods=['GET'])
def read():
    json_data = open('data/scoreranking.json', 'r')
    json_load = json.load(json_data)

    return jsonify(json_load)

@app.route("/write", methods=['POST'])
def write():
    team = request.form.get("Team")
    ranking = request.form.get("Ranking")
    win = request.form.get("Win")
    new_data = {
        "Team": team,
        "Ranking": ranking,
        "Win": win
    }
    json_data = open('data/scoreranking.json', 'r')
    json_load = json.load(json_data)
    for i in json_load:
        if (i["Team"] == team):
            pass
        else:    
            json_load.append(new_data)

    file = open('data/scoreranking.json', 'w')
    new_score_data = json.dump(json_load,file, indent=3)
    
    return jsonify(json_load)

@app.route("/update", methods=['POST'])
def update():
    old_team = request.form.get("OldTeam")
    new_team = request.form.get("NewTeam")
    ranking = request.form.get("Ranking")
    win = request.form.get("Win")

    json_data = open('data/scoreranking.json', 'r')
    json_load = json.load(json_data)
    for i in json_load:
        if (i["Team"] == old_team):
            i["Team"] = new_team
            i["Ranking"] = int(ranking)
            i["Win"] = int(win)

    file = open('data/scoreranking.json', 'w')
    json.dump(json_load,file, indent=3)

    return jsonify(json_load)

@app.route("/delete", methods=['POST'])
def delete():
    team = request.form.get("Team")
    json_data = open('data/scoreranking.json', 'r')
    json_load = json.load(json_data)

    for i in json_load:
        if (i["Team"] == team):
            json_load.remove(i)

    file = open('data/scoreranking.json', 'w')
    json.dump(json_load,file, indent=3)

    return jsonify(json_load)

