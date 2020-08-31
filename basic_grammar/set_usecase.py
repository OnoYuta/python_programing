# 共通の要素を取り出す
my_frinends = {'A', 'C', 'D'}
A_frinends = {'B', 'D', 'E', 'F'}
print(my_frinends & A_frinends)
# {'D'}

# 種類を調べる
fruits = ['apple', 'banana', 'apple', 'banana', 'orange']
kind = set(fruits)
print(kind)
# {'apple', 'banana', 'orange'}