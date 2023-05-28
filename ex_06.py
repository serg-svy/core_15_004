lst1 = [x for x in range(10)]

lst2 = [x for x in range(10, 20)]

print(lst1)

print(lst2)

lst1.extend(lst2)

print(lst1)

lst3 = lst1 + lst2

print(lst1, lst2, lst3)

lst4 = [*lst1, *lst2]

print(lst4)

lst5 = [1] * 3

print(lst5)