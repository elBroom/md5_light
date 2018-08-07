from flask import request, jsonify

from md5_light import app, db
from md5_light.models import Task, StatusType
from md5_light.schema import task_schema
from md5_light.tasks import calculate_hash_by_url_task


@app.route('/submit', methods=['POST'])
def submit_task():
    task, errors = task_schema.load(request.form)
    if errors:
        return jsonify({'errors': errors}), 400

    db.session.add(Task(**task))
    db.session.commit()

    calculate_hash_by_url_task.delay(task['id'])
    return jsonify({'id': task['id']})


@app.route('/check', methods=['GET'])
def check_task():
    task = None
    if request.args.get('id'):
        task = Task.query.filter_by(id=request.args.get('id')).first()
    if not task:
        return jsonify({'status': 'not found'}), 404

    responce = {'status': task.status}
    if task.status == StatusType.DONE:
        responce['url'] = task.url
        responce['md5'] = task.md5

    return jsonify(**responce)
