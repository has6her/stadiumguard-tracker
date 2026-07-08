from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage for issues
issues = []
next_id = 1

@app.route('/')
def home():
    return jsonify({"message": "StadiumGuard Issue Tracker API is running!"})

@app.route('/issues', methods=['POST'])
def create_issue():
    global next_id
    data = request.get_json()

    # Basic validation
    if not data or 'title' not in data or 'description' not in data:
        return jsonify({"error": "Title and description are required"}), 400

    new_issue = {
        "id": next_id,
        "title": data['title'],
        "description": data['description'],
        "severity": data.get('severity', 'Medium'),
        "status": data.get('status', 'Open'),
        "reported_by": data.get('reported_by', 'Unknown')
    }

    issues.append(new_issue)
    next_id += 1

    return jsonify(new_issue), 201

if __name__ == '__main__':
    app.run(debug=True)