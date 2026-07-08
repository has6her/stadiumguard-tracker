from flask import Flask, jsonify, request

app = Flask(__name__)

issues = []
next_id = 1

@app.route('/')
def home():
    return jsonify({"message": "StadiumGuard Issue Tracker API is running!"})

@app.route('/issues', methods=['POST'])
def create_issue():
    global next_id
    data = request.get_json()

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

@app.route('/issues', methods=['GET'])
def get_issues():
    return jsonify(issues), 200

@app.route('/issues/<int:issue_id>', methods=['GET'])
def get_issue(issue_id):
    issue = next((i for i in issues if i['id'] == issue_id), None)
    if issue is None:
        return jsonify({"error": "Issue not found"}), 404
    return jsonify(issue), 200

@app.route('/issues/<int:issue_id>', methods=['PUT'])
def update_issue(issue_id):
    issue = next((i for i in issues if i['id'] == issue_id), None)
    if issue is None:
        return jsonify({"error": "Issue not found"}), 404

    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400

    issue['title'] = data.get('title', issue['title'])
    issue['description'] = data.get('description', issue['description'])
    issue['severity'] = data.get('severity', issue['severity'])
    issue['status'] = data.get('status', issue['status'])
    issue['reported_by'] = data.get('reported_by', issue['reported_by'])

    return jsonify(issue), 200

@app.route('/issues/<int:issue_id>', methods=['DELETE'])
def delete_issue(issue_id):
    issue = next((i for i in issues if i['id'] == issue_id), None)
    if issue is None:
        return jsonify({"error": "Issue not found"}), 404

    issues.remove(issue)
    return jsonify({"message": f"Issue {issue_id} deleted successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)