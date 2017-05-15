"""Вы хотите иметь возможность контролировать вашу программу или общаться
   с ней удалённо, по сети, используя простой REST-интерфейс.
   Однако вы не хотите делать это путём установки полноценного веб-фреймворка.

   Важный момент использования WSGI заключается в том, что ничто
   в этой реализации не специфично для конкретного веб-сервера.
   Это и есть главная идея — поскольку стандарт нейтрален по отношению
   к серверам и фреймворкам, вы сможете прикрутить ваше приложение
   к практически любому серверу"""

import cgi


def notfound_404(environ, start_response):
    start_response('404 Not Found', [('Content-type', 'text/plain')])
    return [b'Not Found']


class Dispatcher:
    """Диспетчер ничего не делает, кроме как управляет отображением
       пар словаря (method, path) в функции-обработчики.
       Когда приходит запрос, метод и путь извлекаются
       и используются для диспетчеризации на обработчик.
       Также любые переменные запроса парсятся и помещаются в
       словарь, который сохраняется как environ['params']"""

    def __init__(self):
        self.patchmap = {}

    def register(self, method, path, func):
        self.patchmap[method.lower(), path] = func
        return func

    """ при поступлении запроса сервер вызывает __call__
    нашего обработчика"""
    def __call__(self, environ, start_response):
        """ environ -
            словарь значений CGI-интерфейса Веб-сервера

           start_response -
           ф-я, кот. д.б. вызвана, чтобы иницировать ответ.
           1-ый её арг: HTTP-статус
           2-ой её арг: список кортежей(name, value)-HTTP-заголовки ответа."""

        ''' извлекаем запрашиваемый путь '''
        path = environ['PATH_INFO']

        '''извлекаем тип запроса GET/POST/HEAD и т.п.'''
        method = environ['REQUEST_METHOD'].lower()

        '''извлекаем параметры запроса в словареподобный объект'''
        params = cgi.FieldStorage(environ['wsgi.input'], environ=environ)

        environ['params'] = {key: params.getvalue(key) for key in params}

        '''из атрибута patchmap по ключу (метод, путь) получаем
           соответствующую ф-ю или ф-ю notfound в случае отсутствия ключа. '''
        handler = self.patchmap.get((method, path), notfound_404)

        ''' передаем в нашу ф-ю словарь и ф-ю используемую для ответа.
            возвращаем результат.'''
        return handler(environ, start_response)

