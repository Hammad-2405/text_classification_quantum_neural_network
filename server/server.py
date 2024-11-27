from flask import Flask, jsonify, request
from flask_cors import CORS
from textblob import TextBlob

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def main_page():
    return jsonify({
        "message": "Main Page"
    })

@app.route("/api/classify-text", methods=["POST"])
def classify_text():
    """
    Classify the input text as happy, sad, or neutral based on sentiment.
    """
    data = request.get_json()  # Get JSON data from request
    if not data or "sentence" not in data:
        return jsonify({"error": "Invalid request, 'sentence' is required"}), 400
    
    sentence = data["sentence"]
    analysis = TextBlob(sentence).sentiment.polarity  # Get sentiment polarity
    
    # Classify based on polarity
    if analysis > 0.1:
        emotion = "happy"
    elif analysis < -0.1:
        emotion = "sad"
    else:
        emotion = "neutral"
    
    return jsonify({"emotion": emotion})

if __name__ == "__main__":
    app.run(debug=True, port=8080)
