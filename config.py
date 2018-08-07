SQLALCHEMY_DATABASE_URI = 'mysql://root:1234@127.0.0.1:3306/md5_checker'
SQLALCHEMY_DATABASE_URI_TEST = 'sqlite:////tmp/test.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False

CELERY_BROKER_URL = 'amqp://user:password@127.0.0.1:5672/'
CELERY_RESULT_BACKEND = CELERY_BROKER_URL
CELERY_IMPORTS = ('md5_checker.tasks',)

# Email
EMAIL_ENABLED = False
EMAIL_HOST = 'elbroom.ru'
EMAIL_FROM_ADDR = 'info@elbroom.ru'
