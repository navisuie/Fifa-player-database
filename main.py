from flask import Flask, render_template, request, jsonify
import csv

main = Flask(__name__)

def load_player_data():
    player_data = []
    with open('male_players.csv', 'r', encoding= 'utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            player_data.append(row)
        return player_data

@main.route('/')
def index():
    player_data = load_player_data()
    return render_template('index.html', player_data = player_data)

@main.route('/api/rankings', methods = ['GET'])
def get_rankings():
    player_data = load_player_data()
    return jsonify(player_data)

@main.route('/player/<short_name>')
def player_detail(short_name):
    player_data = load_player_data()
    selected_player = next((player for player in player_data if player['short_name'] == short_name),None)
    return render_template('player_detail.html', player = selected_player)


if __name__ == '__main__':
    main.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
