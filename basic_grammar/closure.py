def outer(a, b):

    def inner():
        return a + b
    
    return inner

# outerの戻り値は関数なので、この時点では実行しない
f = outer(1, 2)

# ここで初めて実行する
r = f()

print(r)

def circle_area_func(pi):
    def circle_area(radius):
        return pi * radius + radius
    
    return circle_area

ca1 = circle_area_func(3.14)
ca2 = circle_area_func(3.141592)

# 大雑把に円の面積を計算する
print(ca1(19))
# もう少し細かく面積を計算する
print(ca2(19))