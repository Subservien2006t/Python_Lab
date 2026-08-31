import array as arr

a = arr.array('i', [1, 2, 3, 4, 5])

a.append(6)
print(a)
print(a.buffer_info())
print(a.count(3))
a.extend([7, 8, 9])
print(a)
print(a.index(4))
a.insert(4, 10)
print(a)
a.pop()
print(a)
a.remove(2)
print(a)
print(a.reverse())
