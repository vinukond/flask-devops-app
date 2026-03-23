from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory "database"
tasks = []

@app.route('/')
def home():
    return "Flask DevOps App is running!"

# CREATE
@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    tasks.append(data)
    return jsonify({"message": "Task added", "tasks": tasks})

# READ
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

# UPDATE
@app.route('/tasks/<int:index>', methods=['PUT'])
def update_task(index):
    data = request.get_json()
    if index < len(tasks):
        tasks[index] = data
        return jsonify({"message": "Task updated", "tasks": tasks})
    return jsonify({"error": "Task not found"}), 404

# DELETE
@app.route('/tasks/<int:index>', methods=['DELETE'])
def delete_task(index):
    if index < len(tasks):
        tasks.pop(index)
        return jsonify({"message": "Task deleted", "tasks": tasks})
    return jsonify({"error": "Task not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)