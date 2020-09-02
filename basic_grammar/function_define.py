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