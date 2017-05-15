import re


class Iterator:
    inx = 0

    def __init__(self, words):
        self.words = words

    def __iter__(self):
        return self

    def __next__(self):
        try:
            word = self.words[self.inx]
            self.inx += 1
        except IndexError:
            raise StopIteration
        return word


class Iterable:

    def __init__(self, text):
        self.text = text
        self.words = re.findall(r'\w+', text)

    def __iter__(self):
        return Iterator(self.words)

s = 'Hello, my best Friend! How do you fill'

'''for word in Iterable(s):
    print(word)'''

it = iter(Iterable(s))
print(next(it))
print(next(it))
print(next(it))

