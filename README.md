[![Build Status](https://travis-ci.com/elBroom/md5_light.svg?branch=master)](https://travis-ci.com/elBroom/md5_light)

MD5 light
============
Веб-сервис, позволяющий посчитать MD5-хеш от файла, расположенного в интернете

Установка
============
Для установки необходимо:
* [docker](https://docs.docker.com/install/)
* [docker-compose](https://docs.docker.com/compose/install/)


docker должен запускатся от [non-root пользователя](https://docs.docker.com/install/linux/linux-postinstall/#manage-docker-as-a-non-root-user)

Установка сервиса:
```sh
git clone https://github.com/elBroom/md5_light.git
cd md5_light
docker-compose build
```

Запуск
============
Запуск сервиса:
```sh
docker-compose up -d
```

Перезапуск сервиса:
```sh
docker-compose restart
```

Остановка сервиса:
```sh
docker-compose stop
```

Тесты прогоняются только при запущенном сервисе (`docker-compose up -d`)

Запуск тестов:
```sh
docker exec -it md5_light_app py.test
```

Помощь
============
Пример использования сервиса:
```sh
>>> curl -X POST -d "email=user@example.com&url=http://site.com/file.txt" http://localhost:8000/submit
{"id":"0e4fac17-f367-4807-8c28-8a059a2f82ac"}

>>> curl -X GET http://localhost:8000/check?id=0e4fac17-f367-4807-8c28-8a059a2f82ac
{"md5":"f4afe93ad799484b1d512cc20e93efd1","status":"done","url":"http://site.com/file.txt"}
```

