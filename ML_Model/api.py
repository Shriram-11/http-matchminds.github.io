from flask import Flask, request, jsonify
import pandas as pd
import joblib

app = Flask(__name__)

@app.route('/bowlers_form', methods=['POST'])
def submit_form1():
    try:
        if request.method == 'POST':
            loaded_model = joblib.load('bowlers_prediction.pkl')
            new_data = pd.DataFrame({
                'name': [request.form.get('name')],
                'team_played_against': [request.form.get('team_played_against')],
                'overs_bowled': [request.form.get('overs_bowled')],
                'team_batting_first_or_second': [request.form.get('team_batting_first_or_second')],
                'stadium': [request.form.get('stadium')],
                'weather_conditions': [request.form.get('weather_conditions')],
                'league': [request.form.get('league')],
                'type': [request.form.get('type')],
            })
            predictions = loaded_model.predict(new_data)
            predicted_runs = int(predictions[0, 0])
            predicted_wickets = int(predictions[0, 1])

            result = {'predicted_runs': predicted_runs,
                      'predicted_wickets': predicted_wickets}
            return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/batters_form', methods=['POST'])
def submit_form2():
    try:
        if request.method == 'POST':
            loaded_model = joblib.load('batters_prediction.pkl')
            new_data = pd.DataFrame({
                'name': [request.form.get('name')],
                'team_played_against': [request.form.get('team_played_against')],
                'balls': [request.form.get('balls')],
                'team_batting_first_or_second': [request.form.get('team_batting_first_or_second')],
                'stadium': [request.form.get('stadium')],
                'weather_conditions': [request.form.get('weather_conditions')],
                'league': [request.form.get('league')],
                'type': [request.form.get('type')],
            })
            predictions = loaded_model.predict(new_data)
            predicted_runs = int(predictions[0, 0])
            predicted_boundaries = int(predictions[0, 1])

            result = {'predicted_runs': predicted_runs,
                      'predicted_boundaries': predicted_boundaries}

            return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
