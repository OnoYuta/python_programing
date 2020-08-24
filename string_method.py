s = 'My name is Mike. Hi Mike.'
print(s)
# >>> print(s)
# My name is Mike. Hi Mike.

# 特定の文字で始まっているか
is_start = s.startswith('My')
print(is_start)
is_start = s.startswith('X')
print(is_start)
# >>> is_start = s.startswith('My')
# >>> print(is_start)
# True
# >>> is_start = s.startswith('X')
# >>> print(is_start)
# False

# 何文字めに登場するか
print(s.find('Mike'))
# >>> print(s.find('Mike'))
# 11

# 後ろから何文字めに登場するか
print(s.rfind('Mike'))
# >>> print(s.rfind('Mike'))
# 20

# 特定の単語のカウント
print(s.count('Mike'))

# 先頭だけ大文字で残りは小文字にする
print(s.capitalize())
# My name is mike. hi mike.

# 単語の先頭の文字を大文字にする
print(s.title())
# My Name Is Mike. Hi Mike.

# すべてを大文字
print(s.upper())
# MY NAME IS MIKE. HI MIKE.

# すべてを小文字
print(s.lower())
# my name is mike. hi mike.

# 特定の単語を置換する
print(s.replace('Mike', 'Nancy'))
# My name is Nancy. Hi Nancy.