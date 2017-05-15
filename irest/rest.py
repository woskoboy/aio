import time

from irest.dispatcher import Dispatcher
from wsgiref.simple_server import make_server

hello_html = """
<html><head><title>Hello {name}</title></head>
<body>Hello {name}!!!</body></html>
"""
time_xml = """
<?xml version="1.0"?>
<time>
    <year>{t.tm_year}</year>
    <month>{t.tm_mon}</month>
    <day>{t.tm_mday}</day>
    <hour>{t.tm_hour}</hour>
    <minute>{t.tm_min}</minute>
    <second>{t.tm_sec}</second>
</time>
"""


def hello_word(environ, start_response):
    start_response('200 OK', [('Content-type', 'text/html')])

    params = environ['params']
    resp = hello_html.format(name=params.get('name'))
    yield resp.encode('utf-8')


def local_time(environ, start_response):
    start_response('200 OK', [('Content-type', 'application/xml')])

    resp = time_xml.format(t=time.localtime())
    yield resp.encode('utf-8')

if __name__ == '__main__':

    dp = Dispatcher()
    dp.register('GET', '/hello', hello_word)
    dp.register('GET', '/time', local_time)

    httpd = make_server('', 9090, dp)
    print('Serving on port 9090')
    httpd.serve_forever()
