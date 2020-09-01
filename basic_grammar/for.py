some_list = [1, 2, 3, 4, 5]

for i in some_list:
    print(i)

# 文字列も一文字ずつ取り出せる
for s in 'abcde':
    print(s)

for word in ['My', 'name', 'is', 'Mike']:
    if word == 'name':
        continue
    print(word)

# breakしなければelse句が実行される
for fruit in ['apple', 'banana', 'orange']:
    if fruit == 'melon':
        print('stop eating')
        break
    print(fruit)
else:
    print('I ate all!')