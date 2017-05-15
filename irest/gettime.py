from urllib.request import urlopen

u = urlopen('http://localhost:9090/time')
print(u.read().decode('utf-8'))
