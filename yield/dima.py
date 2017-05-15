class MyException(Exception):
    def __init__(self, type, msg):
        self.error = type
        self.msg = msg

    def __str__(self):
        return self._msg


def run():
    collection = [1,2,3,4,5]
    try:
        for i in range(0,6):
            print(collection[i])
    except Exception as e:
        raise MyException(e.__class__, "It's index error")


try:
    run()
except MyException as me:
    print(me.error, me.msg )



