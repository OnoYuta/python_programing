# 任意の数の引数を渡す
# def say_something(*args):
#     for arg in args:
#         print(arg)
# say_something('Hi!', 'Mike', 'Nancy')

def say_something(word, *args):
    print('word =', word)
    for arg in args:
        print(arg)
# say_something('Hi!', 'Mike', 'Nancy')

t = ('Mile', 'Nancy')
say_something('Hi!', *t)

print(t)
print(*t)