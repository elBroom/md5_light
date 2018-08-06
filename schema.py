import uuid

from marshmallow import fields, post_load

from md5_checker import ma


class TaskSchema(ma.Schema):
    id = fields.UUID(dump_only=True)
    url = fields.Url(required=True)
    email = fields.Email()

    @post_load
    def create_task(self, data):
        data['id'] = uuid.uuid4()
        return data

task_schema = TaskSchema()
