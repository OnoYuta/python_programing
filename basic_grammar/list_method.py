r = [1, 2, 3, 4, 5, 1, 2, 3]

# 3という要素が何番めにあるか
print(r.index(3))
# >>> print(r.index(3))
# 2

# index3以降で3が最初に登場する位置
print(r.index(3,3))
# >>> print(r.index(3,3))
# 7

# 3という要素の数
print(r.count(3))
# >>> print(r.count(3))
# 2

# listに含まれているか判定する
if 3 in r:
    print('exist')
# exist

# listをsortする
r.sort()
print(r)
# [1, 1, 2, 2, 3, 3, 4, 5]
r.sort(reverse=True)
print(r)
# [5, 4, 3, 3, 2, 2, 1, 1]
r.reverse()
print(r)
# [1, 1, 2, 2, 3, 3, 4, 5]

# 文字列をlistに変換
# list('abcdefg')
# ['a', 'b', 'c', 'd', 'e', 'f', 'g']
s = 'My name is Mike.'
to_split = s.split(' ')
print(to_split)
# ['My', 'name', 'is', 'Mike.']

# 空白文字でlistを連結する
x = ' '.join(to_split)
print(x)
# My name is Mike.