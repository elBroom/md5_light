import uuid

from marshmallow import fields, post_load

from md5_light import ma


def get_task_id():
    return str(uuid.uuid4())


class TaskSchema(ma.Schema):
    id = fields.String(dump_only=True)
    url = fields.Url(required=True)
    email = fields.Email()

    @post_load
    def create_task(self, data):
        data['id'] = get_task_id()
        return data


task_schema = TaskSchema()
