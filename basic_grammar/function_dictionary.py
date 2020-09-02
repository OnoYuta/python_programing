# アスタリスク2つで辞書型を渡せる
def menu(**kwargs):
    for k, v in kwargs.items():
        print(k, v)
menu(entree='beef', drink='coffee')

# 辞書型を展開して渡す
d = {
    'entree': 'beef',
    'drink': 'ice coffee',
    'dessert': 'ice',
}
menu(**d)
# entree beef
# drink ice coffee
# dessert ice

# 位置引数のタプル化とキーワード引数の辞書化を併用
def new_menu(food, *args, **kwargs):
    print(food)
    print(args)
    print(kwargs)

new_menu('banana', 'apple', 'orange', entree='beef', drink='coffee')
# banana
# ('apple', 'orange')
# {'entree': 'beef', 'drink': 'coffee'}