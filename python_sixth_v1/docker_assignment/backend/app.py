from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/api", methods=["POST"])
def api():
    data = request.get_json()   # <-- JSON instead of form
    username = data.get("username")
    email = data.get("email")
    age = data.get("age")
    return jsonify({
        "message": f"Hi {username}, Your Email is {email} and Your age is {age}"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
