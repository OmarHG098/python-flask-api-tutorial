from flask import Flask, jsonify, request
app = Flask(__name__)

todos =[
    {"label": "My first task", "done": False},
    {"label": "My second task", "done": False}
]
class Todo:
    def __init__(self, label, done):
        self.label = label
        self.done = done
    def serialize(self):
        return {
            "label": self.label,
            "done": self.done
        }


@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos)
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.get_json(force=True)
    label = request_body.get("label", None) 
    done = request_body.get("done", None)

    if label is None:
        return jsonify({"error": "Label is required"}), 400
    if done is None:
        return jsonify({"error": "Done is required"}), 400

    todo = Todo(label, done)
    todos.append(todo.serialize())
    return todos
    
    print("Incoming request with the following body", request_body)
    return 'Response for the POST todo'

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    todos.pop(position)
    return jsonify(todos)

    print("This is the position to delete:", position)
    return 'something'
    

if __name__=='__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)