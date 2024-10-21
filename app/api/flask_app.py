from flask import Flask, request, render_template
from flask_cors import CORS

from database.queues.create_database_tables import create_database_tables
from database.queues.get_tasks import get_tasks
from database.queues.post_task import post_task
from database.queues.put_task import put_task
from database.queues.delete_task import delete_task


app = Flask(__name__, template_folder='/app/templates', static_folder='/app/static')
CORS(app)


@app.route('/')
def serve_homepage():
    return render_template('index.html')


@app.route('/tasks', methods=['GET'])
def get_tasks_api():
    try:
        tasks = get_tasks()

        return {'tasks': tasks}
    except Exception as e:
        return {'error': str(e)}


@app.route('/tasks', methods=['POST'])
def post_task_api():
    try:
        title = request.json['title']
        description = request.json['description']

        post_task(title, description)

        return '', 204
    except Exception as e:
        return {'error': str(e)}


@app.route('/tasks/<int:id>', methods=['PUT'])
def put_task_api(id):
    try:
        title = request.json['title']
        description = request.json['description']

        put_task(id, title, description)

        return '', 204
    except Exception as e:
        return {'error': str(e)}


@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task_api(id):
    try:
        delete_task(id)

        return '', 204
    except Exception as e:
        return {'error': str(e)}


if __name__ == '__main__':
    create_database_tables()
    app.run(debug=True, host='0.0.0.0', port=5000)