seat = []
min = 0
max = 5

print(min <= len(seat) < max)
# True

seat.append('person')
seat.append('person')
seat.append('person')
seat.append('person')
seat.append('person')
print(min <= len(seat) < max)
# False

seat.pop()
print(min <= len(seat) < max)
# True