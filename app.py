# app.py
from bottle import Bottle, request, response, run
from models import Task, SessionLocal
import json
from datetime import datetime

app = Bottle()


def json_response(data, status=200):
    response.content_type = 'application/json'
    response.status = status
    return json.dumps(data)


@app.route('/tasks', method='GET')
def get_tasks():
    session = SessionLocal()
    try:
        tasks = session.query(Task).all()
        result = [task.to_dict() for task in tasks]
        return json_response(result)
    finally:
        session.close()


@app.route('/tasks/<task_id:int>', method='GET')
def get_task(task_id):
    session = SessionLocal()
    try:
        task = session.query(Task).filter(Task.id == task_id).first()
        if task:
            result = task.to_dict()
            return json_response(result)
        else:
            return json_response({"error": "Task not found"}, 404)
    finally:
        session.close()


@app.route('/tasks', method='POST')
def create_task():
    data = request.json
    if not data or 'taskDescription' not in data:
        return json_response({"error": "taskDescription is required"}, 400)

    session = SessionLocal()
    try:
        new_task = Task(
            description=data['taskDescription'], is_completed=False)
        session.add(new_task)
        session.commit()
        return json_response({"message": "Task created successfully", "task": new_task.to_dict()}, 201)
    finally:
        session.close()


@app.route('/tasks/<task_id:int>', method='PUT')
def update_task(task_id):
    data = request.json
    session = SessionLocal()
    try:
        task = session.query(Task).filter(Task.id == task_id).first()
        if not task:
            return json_response({"error": "Task not found"}, 404)

        # Update fields
        task.description = data.get(
            'taskDescription', task.description)
        task.is_completed = data.get('isCompleted', task.is_completed)
        task.updated_at = datetime.now()

        session.commit()
        return json_response({"message": "Task updated", "task": task.to_dict()})
    finally:
        session.close()


@app.route('/tasks/<task_id:int>', method='DELETE')
def delete_task(task_id):
    session = SessionLocal()
    try:
        task = session.query(Task).filter(Task.id == task_id).first()
        if not task:
            return json_response({"error": "Task not found"}, 404)

        session.delete(task)
        session.commit()
        return json_response({"message": f"Task with ID {task_id} is deleted"})
    finally:
        session.close()


# Run the Bottle app
run(app, host='localhost', port=8080, debug=True)
