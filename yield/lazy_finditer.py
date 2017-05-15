from re import finditer


class Iterable:
    def __init__(self, text):
        self.text = text

    def __iter__(self):
        for w in finditer(r'\w+', self.text):
            yield w.group()

s = ''' You'll make find best examples of code
        on "Alexander Krivenko" chanel '''

for word in Iterable(s):
    print(word)
