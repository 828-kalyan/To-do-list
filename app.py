from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form.get('task')
    if task:
        tasks.append(task)
        save_data()
    return jsonify({'status': 'success'})

@app.route('/delete/<int:index>')
def delete_task(index):
    if 0 <= index < len(tasks):
        del tasks[index]
        save_data()
    return jsonify({'status': 'success'})

def save_data():
    with open('tasks.txt', 'w') as file:
        for task in tasks:
            file.write(task + '\n')

def load_data():
    try:
        with open('tasks.txt', 'r') as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

if __name__ == '__main__':
    tasks = load_data()
    app.run(debug=True)

