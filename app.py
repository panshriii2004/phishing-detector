from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))

def extract_features(url):
    return [
        len(url),
        url.count('.'),
        1 if "https" in url else 0
    ]

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    if request.method == "POST":
        url = request.form["url"]
        features = [extract_features(url)]
        prediction = model.predict(features)[0]

        if prediction == 1:
            result = "🔴 Phishing Website Detected"
        else:
            result = "🟢 Safe Website"

    return render_template("index.html", result=result)

app.run(debug=True)