from re import finditer


class Iterable:
    def __init__(self, text):
        self.text = text

    def __iter__(self):
        return (w.group() for w in finditer(r'\w+', self.text))

s = ''' You'll make find best examples of code
        on "Alexander Krivenko" chanel '''

it = Iterable(s)
print(it)

for word in it:
    print(word)
