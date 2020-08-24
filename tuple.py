# タプルはパレンテシスで要素を囲む
t = (1, 2, 3, 4, 1, 2)

print(t[0])

# タプルには値の再代入ができない => 読み込み専用のときに使用する
# t[0] = 100
#   File "<stdin>", line 1, in <module>
# TypeError: 'tuple' object does not support item assignment

# タプルにlistを格納する場合、listの要素は再代入可能
t = ([1, 2, 3], [4, 5, 6])
t[0][0] = 0
print(t)
# ([0, 2, 3], [4, 5, 6])

# tupleを結合する
t = (1, 2, 3) + (4, 5, 6)
print(t)
# (1, 2, 3, 4, 5, 6)

# tupleのアンパッキング
t = (10, 20)
x, y = t
print(x, y)
# 10 20

# tupleのパレンテシスは省略できる
min, max = 10, 20
print(min, max)
# 10 20

# アンパッキングを利用した値の入れ替え
i = 10
j = 20
i, j = j, i
print(i, j)
# 20 10