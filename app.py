from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "App is working"

@app.route("/search")
def search():
    q = request.args.get("q")
    return f"You searched for {q}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

