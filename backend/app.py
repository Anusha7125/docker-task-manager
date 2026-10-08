from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Task Manager Backend is running!"


@app.route("/tasks")
def tasks():
    return {
        "tasks": [
            {"id": 1, "title": "Learn Docker"},
            {"id": 2, "title": "Learn Docker Compose"}
        ]
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)