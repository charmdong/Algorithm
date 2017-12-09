cnt = int(input())
lst=[]
while cnt:
    lst.append(input())
    cnt -= 1

for i in sorted(list(map(int, lst))):
    print(i)