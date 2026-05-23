from flask import Flask, request, jsonify, render_template
import pandas as pd
import joblib

app = Flask(__name__)

model = joblib.load('spotify_model_sklearn.pkl')
scaler = joblib.load('scaler.pkl')
feature_columns = joblib.load('feature_columns.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    sample = pd.DataFrame([{
        'danceability':     float(data['danceability']),
        'energy':           float(data['energy']),
        'key':              5,
        'loudness':         float(data['loudness']),
        'mode':             1,
        'speechiness':      float(data['speechiness']),
        'acousticness':     float(data['acousticness']),
        'instrumentalness': float(data['instrumentalness']),
        'liveness':         float(data['liveness']),
        'valence':          float(data['valence']),
        'tempo':            float(data['tempo']),
        'duration_ms':      200000,
        'explicit':         0,
        'time_signature':   4
    }])

    for col in feature_columns:
        if col not in sample.columns:
            sample[col] = 0

    sample = sample[feature_columns]
    scaled = scaler.transform(sample)
    prob = model.predict_proba(scaled)[0][1] 

    return jsonify({
        'probability': round(prob * 100, 1),
        'prediction': 'Hit' if prob >= 0.5 else 'Not a Hit'
    })

if __name__ == '__main__':
    app.run(debug=False)
