lst = [i for i in input()]
alpha = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
total = len(lst)

for i in lst:
    for j in alpha:
        if i in j: total += (alpha.index(j)+2)

print(total)
