a = [1,2,3,4,5,1,2,3]
print(set(a))
for i in set(a):
    print(i)

b = ["tony","tom"]
print(b[0][1:3])

dict1 = {
    'name' : 77
}

for i,j in dict1.items():
    print(i,j)
    print(type(i),type(j))

for i in dict1:
    print(i,dict1[i])
    print(type(i),type(dict1[i]))


print(int(3.5))