import os
from time import time

import requests
import sys

BASE_URL = 'http://flupy.org/data/flags'
DIR = 'downloads/'
url_img = '{}/{cc}/{cc}.gif'

CC = 'CN IN US ID BR PK NG BD RU JP MX PH VN ET EG DE IR TR CD FR'.lower().split()


def show(code):
    print(code, end=' ')
    sys.stdout.flush()


def request_img(code):
    url = url_img.format(BASE_URL, cc=code)
    resp = requests.get(url)
    return resp.content


def save_img(img, filename):
    path = os.path.join(DIR, '{}.gif'.format(filename))
    with open(path, 'wb') as f:
        f.write(img)


def download(cc):
    for code in sorted(cc):
        img = request_img(code)
        show(code)
        save_img(img, code)
    return len(cc)


def main(func, cc=CC):
    t0 = time()
    count = func(cc)
    offset = time() - t0
    msg = '{} flags downloaded in {:.2f}s'.format(count, offset)
    print(msg)

if __name__ == '__main__':
    main(download)

