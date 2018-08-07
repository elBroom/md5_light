from celery import Celery
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config.from_envvar('FLASK_CONFIG')

# docker run -p 3306:3306 -v $(pwd):/docker-entrypoint-initdb.d
#    -e MYSQL_ROOT_PASSWORD=1234 -e MYSQL_DATABASE=md5_light -d mysql:5.6

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)
db = SQLAlchemy(app)
ma = Marshmallow(app)
