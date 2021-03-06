SQLALCHEMY_DATABASE_URI = 'mysql://root:1234@mysql:3306/md5_light'
SQLALCHEMY_DATABASE_URI_TEST = 'sqlite:////tmp/test.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False

CELERY_BROKER_URL = 'amqp://user:password@rabbit:5672/'
CELERY_RESULT_BACKEND = CELERY_BROKER_URL
CELERY_IMPORTS = ('md5_light.tasks',)

# Email
EMAIL_ENABLED = False
EMAIL_HOST = 'elbroom.ru'
EMAIL_FROM_ADDR = 'info@elbroom.ru'
