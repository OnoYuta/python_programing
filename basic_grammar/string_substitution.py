# グレイシス{}に文字を代入する
print('a is {}'.format('a'))
# a is a

# 複数のリテラルの代入
print('a is {} {} {}'.format(1,2,3))
# a is 1 2 3
print('a is {0} {1} {2}'.format(1,2,3))
# a is 1 2 3
print('a is {2} {1} {0}'.format(1,2,3))
# a is 3 2 1

print('My name is {0} {1}. Watashi ha {1} {0}.'.format('Yuta', 'Ono'))
# My name is Yuta Ono. Watashi ha Ono Yuta.

# 変数に入れて代入
print('My name is {name} {family}. Watashi ha {family} {name}.'.format(name='Yuta', family='Ono'))
# My name is Yuta Ono. Watashi ha Ono Yuta.

# f-string（Python 3.6より）
a = 'a'
print(f'a is {a}')

x, y, z = 1, 2, 3
print(f'a is {x}, {y}, {z}')

name = 'Yuta'
family = 'Ono'
print(f'My name is {name} {family}. Watashi ha {family} {name}.')