from flask import Flask, render_template, request, jsonify


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/send", methods=["POST"])
def send():
    data = request.get_json()
    data = (data.get('data'))
    print(data)
    return "1"

if __name__ == "__main__":
    app.run(debug=True)