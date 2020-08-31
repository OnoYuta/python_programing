x = True
y = False

# 等しい
print(x == y)

# 等しくない
print(x != y)

# どちらかがtrue
print(x or y)

# 両方がtrue
print(x and y)

# 否定
print(not x)

y = [1, 2, 3]
x = 1

if x in y:
    print('in')

if 100 not in y:
    print('not in')

is_OK = False

if not is_OK:
    print('NG')

l = [1, 2, 3]
if len(l) > 0:
    print('in')
else:
    print('not in')

# 空のリストはfalseと判定されるので下記でもOK
if l:
    print('in')
else:
    print('not in')

# 下記の値はすべてFalseと判定される
# False, 0, 0.0, '', [], (), {}, set{}