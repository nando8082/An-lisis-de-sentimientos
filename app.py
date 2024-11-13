# app.py

from flask import Flask, jsonify, request
from services.twitter_service import get_twitter_metrics
from services.sentiment_analysis import analyze_sentiment

app = Flask(__name__)

# Endpoint para obtener las métricas de Twitter


@app.route('/api/twitter/<username>', methods=['GET'])
def twitter_metrics(username):
    data = get_twitter_metrics(username)
    return jsonify(data)

# Endpoint para analizar el sentimiento de un texto


@app.route('/api/sentiment', methods=['POST'])
def sentiment_analysis():
    content = request.json.get("content")
    sentiment = analyze_sentiment(content)
    return jsonify({"sentiment": sentiment})


if __name__ == '__main__':
    app.run(debug=True)
