from flask import Flask, jsonify

app = Flask(__name__)
# In-memory storage for issues
issues = []
next_id = 1

@app.route('/')
def home():
    return jsonify({"message": "StadiumGuard Issue Tracker API is running!"})

if __name__ == '__main__':
    app.run(debug=True)