import re


class Iterable:

    def __init__(self, text):
        self.text = text
        self.words = re.findall(r'\w+', text)

    def __iter__(self):
        for word in self.words:
            yield word
        '''return iter(self.words)'''
        # return

s = 'Hello, my best Friend! How do you feel?'

'''it = Iterable(s)
print(iter(it))  # <generator object __iter__ at 0x7f1dec015360>

for word in Iterable(s):  # for = iter(obj) then next(obj) ...
    print(word)'''

# it = iter(Iterable(s))
# print(next(it))

# print(next(it))
# print(next(it))
# print(next(it))

gen = Iterable(s)
for i in gen:
    print(i)
