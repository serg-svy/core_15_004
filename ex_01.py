"""list"""

lst = []
lst1 = list()

lst2 = [1, 2, 3, 4]

print(type(lst1))


for i in range(10, 20):
    lst1.append(i)
    
print(lst1[3]) 

# print(lst1[0])   

for index, item in enumerate(lst1):
    print( index, item)