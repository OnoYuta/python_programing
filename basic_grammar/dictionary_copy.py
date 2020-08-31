# 参照渡し
x = {'a': 1}
y = x
y['a'] = 1000
print(x)
# {'a': 1000}
print(y)
# {'a': 1000}

# 辞書型のコピー
x = {'a': 1}
y = x.copy()
y['a'] = 1000
print(x)
# {'a': 1}
print(y)
# {'a': 1000}