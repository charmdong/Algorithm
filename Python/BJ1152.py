string = input("Input the string : ")

tmpList = string.split(' ')
res = []

for i in tmpList:
    if not i in res:
        res.append(i)

print(res)
print(len(res))

