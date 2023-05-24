"""list"""

lst = []
lst1 = list()

lst2 = [1, 2, 3, 4]

print(type(lst1))


for i in range(10):
    lst1.append(i)
    
print(lst1) 

print(lst1[0])   

for i in range(len(lst1)):
    print(lst1[i])