from flask import Flask, render_template, request, redirect
import json

app = Flask(__name__)

def load_tasks():
    with open("tasks.json", "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open("tasks.json", "w") as f:
        json.dump(tasks, f, indent=4)

@app.route("/")
def index():
    tasks = load_tasks()
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add():
    task = request.form.get("task")
    if task:
        tasks = load_tasks()
        tasks.append({"task": task, "done": False})
        save_tasks(tasks)
    return redirect("/")

@app.route("/done/<int:index>")
def done(index):
    tasks = load_tasks()
    tasks[index]["done"] = not tasks[index]["done"]
    save_tasks(tasks)
    return redirect("/")

@app.route("/delete/<int:index>")
def delete(index):
    tasks = load_tasks()
    tasks.pop(index)
    save_tasks(tasks)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
