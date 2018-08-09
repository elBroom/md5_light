import hashlib
import os
import requests
import shutil
import smtplib
import uuid


class DownloadFileException(Exception):
    pass


def dowanload_file(url):
    try:
        r = requests.get(url, stream=True, timeout=60 * 2)
    except Exception:
        raise DownloadFileException

    if r.status_code == 200:
        path = os.path.join('/tmp', 'dowanload_file_' + str(uuid.uuid4()))
        with open(path, 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)
        return path
    raise DownloadFileException


def remove_file(path):
    if os.path.isfile(path):
        os.remove(path)


def calculate_hash_by_file(path):
    if not os.path.isfile(path):
        return

    md5 = hashlib.md5()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(1 << 12), b''):
            md5.update(chunk)
    return md5.hexdigest()


def send_email(host, subject, to_addr, from_addr, body_text):
    BODY = '\r\n'.join((
        'From: {}'.format(from_addr),
        'To: {}'.format(to_addr),
        'Subject: {}'.format(subject),
        '',
        body_text
    ))
    server = smtplib.SMTP(host)
    server.sendmail(from_addr, [to_addr], BODY)
    server.quit()
