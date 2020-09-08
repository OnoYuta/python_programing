def print_more(func):
    def wrapper(*args, **ksargs):
        print('func:', func.__name__)
        print('args:', args)
        print('ksargs:', ksargs)
        result = func(*args, **ksargs)
        print('result:', result)
        return result
    return wrapper

def print_info(func):
    def wrapper(*args, **ksargs):
        print('start')
        result = func(*args, **ksargs)
        print('end')
        return result
    return wrapper

# def add_num(a, b):
#     return a + b

# add_numを引数にデコレータを呼び出す
# f = print_info(add_num)
# r = f(10, 20)
# print(r)
# start
# end
# 30

# 上記を@でデコレータを指定することができる
@print_info
@print_more
def add_num(a, b):
    return a + b

r = add_num(10, 20)
print(r)

@print_info
def sub_num(a, b):
    return a - b

r = sub_num(20, 10)
print(r)