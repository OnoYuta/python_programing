# 選択肢が書き換えられないようにlistではなくtupleを使う
chose_from_two = ('A', 'B', 'C')

answer = []
answer.append('A')
answer.append('C')
print(chose_from_two)
# ('A', 'B', 'C')
print(answer)
# ['A', 'C']