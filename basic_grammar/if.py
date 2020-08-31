x = 10

# 半角スペース4つでインデントをつけるのが通例
if x < 0:
    print('negative')
elif x == 0:
    print('zero')
else:
    print('positive')

a = 5
b = 10

# pythonではブレイシスではなくインデントでブロックを区切る
if a > 0:
    print('a is positive')
    if b > 0:
        print('b is positive')
