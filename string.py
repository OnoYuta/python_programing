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

# リテラル連結が有効な例
s = ('aaaaaaaaaaaaaaaa'
     'bbbbbbbbbbbbbbbb')
print(s)
# aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbb