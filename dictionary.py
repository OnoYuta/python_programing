# dictionaryはブレイシス{}で囲む
d = {'x': 10, 'y': 20}
print(d)
# {'x': 10, 'y': 20}
print(type(d))
# <class 'dict'>

d['x'] = 100
print(d)
# {'x': 100, 'y': 20}

d['z'] = 300
print(d)
# {'x': 100, 'y': 20, 'z': 300}

d = dict(a = 10, b = 20)
print(d)
# {'a': 10, 'b': 20}

d = dict([('a', 10), ('b', 20)])
print(d)
# {'a': 10, 'b': 20}