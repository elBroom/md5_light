from enum import Enum

from sqlalchemy.sql import func

from md5_checker import db


class StatusType(str, Enum):
    CREATED = "created"
    RUNNING = "running"
    DONE = "done"
    FAIL = "fail"


class Task(db.Model):
    id = db.Column(db.String(50), primary_key=True)
    created_at = db.Column(db.DateTime, server_default=func.now())
    started_at = db.Column(db.DateTime)
    finished_at = db.Column(db.DateTime)

    url = db.Column(db.String(1 << 15), nullable=False)
    email = db.Column(db.String(120))
    status = db.Column(db.Enum(StatusType), default=StatusType.CREATED, nullable=False)
    md5 = db.Column(db.String(32))

    def __repr__(self):
        return '<Task %r>' % self.id
