# 単純な出力
print('hello')
# hello

# シングルクォートエスケープ
print('I don\'t know')
# I don't know

# 複数行の出力
print("""\
line1
line2
line3\
""")
# line1
# line2
# line3

# 文字列の反復
print('Hi,' * 3 + 'Mike.')
# Hi,Hi,Hi,Mike.

# リテラル連結
print('Py''thon')
# Python

# 変数に入れた文字列の連結
prefix = 'Py'
print(prefix + 'thon')
# Python

# プラス記号がないとリテラルが複数行に渡るときも読みやすい
s = ('aaaaaaaaaaaaaaaa'
     'bbbbbbbbbbbbbbbb')
print(s)
# aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbb

# バックスラッシュで連結することもできるが読みにくいので嫌う人もいる
s = 'aaaaaaaaaaaaaaaa'\
     'bbbbbbbbbbbbbbbb'
print(s)
# aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbb

# リテラルの一部を出力
word = 'python'
print(word[0])
print(word[1])
print(word[-1])
# >>> print(word[0])
# p
# >>> print(word[1])
# y
# >>> print(word[-1])
# n

# スライス
print(word[0:2])
# >>> print(word[0:2])
# py
print(word[:2])
# >>> print(word[:2])
# py
print(word[2:])
# >>> print(word[2:])
# thon

# リテラルの一文字めを置き換える
word = 'python'
word = 'j' + word[1:]
print(word)
# jython

# リテラルの長さ
n = len(word)
print(n)
# >>> print(n)
# 6