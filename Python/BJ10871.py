size, num = map(int , input().split())

lst = []
lst = input().split()

if len(lst) is size:
    res = list(filter(lambda x : int(x)<num, lst))
    for i in res :
        print(i, end=" ")
