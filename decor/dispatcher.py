from functools import singledispatch
import html


@singledispatch
def base_handler(obj):
    content = html.escape(repr(obj))
    return '<pre>{}</pre>'.format(content)

