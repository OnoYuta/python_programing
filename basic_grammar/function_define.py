# 関数の定義と実行（任意の名前とパレンテシス）
def say_something():
    print('hi')

say_something()

# 戻り値のある関数
def get_something():
    s = 'hi'
    return s
result = get_something()
print(result)

# 引数の定義
def what_is_this(color):
    if color == 'red':
        return 'tomato'
    elif color == 'green':
        return 'green papper'
    else:
        return "I don't know"
result = what_is_this('red')
print(result)

# 関数の型宣言
def add_num(a: int, b: int) -> int:
    return a + b

r = add_num(1,2)
print(r)

# 宣言した型が一致しない場合もエラーにならない
r = add_num('a', 'b')
print(r)
# ab

def menu(entree, drink, dessert):
    print(entree)
    print(drink)
    print(dessert)

# 位置引数
menu('beef', 'ice', 'beer')

# キーワード引数
menu(entree='beef', dessert='ice', drink='beer')
menu('beef', dessert='ice', drink='beer')

# デフォルト引数
def default_menu(entree='beef', drink='wine', dessert='ice'):
    print(entree)
    print(drink)
    print(dessert)

default_menu(entree='chicken', drink='beer')