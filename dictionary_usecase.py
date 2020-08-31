# dictinaryはハッシュテーブルなのでappleを取り出すのが早い
fruits = {
    'apple': 100,
    'banana': 200,
    'orange': 300,
}
print(fruits['apple'])

# listは先頭からappleを探すプログラムが必要
l = [
    ['apple', 100],
    ['banana', 200],
    ['orange', 300],
]
