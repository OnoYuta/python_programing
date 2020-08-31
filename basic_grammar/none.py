is_empty = None
# print(help(is_empty))
# class NoneType(object)

if is_empty == None:
    print('None')

if is_empty is None:
    print('None')

is_empty = 1
if is_empty is not None:
    print('Not None')