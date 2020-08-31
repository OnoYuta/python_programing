d = {'x': 10, 'y': 20}
print(d)

# keyのみ取り出す
print(d.keys())

# valueを取り出す
print(d.values())

# 値のオーバライド
d2 = {'x': 1000, 'z': 50}
d.update(d2)
print(d)
# {'x': 1000, 'y': 20, 'z': 50}

# 値の取得
print(d['x'])
print(d.get('x'))

# get()を使うと存在しないkeyでNoneTypeを返す
# print(d['a'])
# KeyError: 'a'
print(d.get('a'))
# None

# 値を取得して削除
print(d)
# {'x': 1000, 'y': 20, 'z': 50}
print(d.pop('x'))
# 1000
print(d)
# {'y': 20, 'z': 50}

# 値の削除
del d['y']
print(d)
# {'z': 50}

# すべての値を削除
d.clear()
print(d)
# {}

# keyが存在するか判定
d = {'a': 100, 'b': 200}
print('a' in d)
# True
print('c' in d)
# False