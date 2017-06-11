from collections import namedtuple

Request = namedtuple('Request', 'req_method data')


class HTTPhandler:

    def handler(self, request):
        method = 'do_' + request.req_method
        getattr(self, method)(request)

    def do_GET(self, request):
        print('response GET with ', request.data)

    def do_POST(self, request):
        print('response POST with ', request.data)

req = Request(req_method='PUT', data={'cherry': 1})
# HTTPhandler().handler(req)


class HTTP(HTTPhandler):
    def do_PUT(self, request):
        print('response PUT with ', request.data)

HTTP().handler(req)
