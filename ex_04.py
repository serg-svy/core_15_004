lst1 = [x for x in range(100)]

print(f"len before pop: {len(lst1)}")

item = lst1.pop()

print(item)

print(f"len after pop: {len(lst1)}")


item = lst1.pop(100)

for i in lst1:
    print(lst1.pop(33))

print(item)

print(f"len after pop: {len(lst1)}")