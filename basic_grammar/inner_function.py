# ある関数内でだけ使用される関数を関数内関数と呼ぶ
def outer(a, b):
    print(a, b)

    # 関数内で何度も実行したい処理がある場合は関数内関数を使用する
    def plus(c, d):
        return c + d
    
    r1 = plus(a, b)
    r2 = plus(b, a)
    print(r1, r2)

outer(1, 2)