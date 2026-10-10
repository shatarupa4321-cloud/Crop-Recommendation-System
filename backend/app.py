from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import pandas as pd

app = Flask(__name__)
CORS(app)

# Load model
with open("classifier.pkl", "rb") as f:
    model = pickle.load(f)

label_map = {
    0:'apple',1:'banana',2:'blackgram',3:'chickpea',4:'coconut',
    5:'coffee',6:'cotton',7:'grapes',8:'jute',9:'kidneybeans',
    10:'lentil',11:'maize',12:'mango',13:'mothbeans',14:'mungbean',
    15:'muskmelon',16:'orange',17:'papaya',18:'pigeonpeas',
    19:'pomegranate',20:'rice',21:'watermelon'
}

@app.route("/")
def home():
    return "API Running ✅"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json
        features = pd.DataFrame([[ 
            data["N"],
            data["P"],
            data["K"],
            data["temperature"],
            data["humidity"],
            data["ph"],
            data["rainfall"]
        ]], columns=['N','P','K','temperature','humidity','ph','rainfall'])

        probs = model.predict_proba(features)[0]
        classes = model.classes_

        results = [
            {
                "name": label_map.get(int(classes[i]), str(classes[i])).capitalize(),
                "confidence": round(float(p * 100), 2)
            }
            for i, p in enumerate(probs)
        ]

        # Sort top 5
        results = sorted(results, key=lambda x: x["confidence"], reverse=True)[:5]

        return jsonify(results)

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)