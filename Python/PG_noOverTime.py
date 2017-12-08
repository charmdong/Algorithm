def noOvertime(n, works):
    if n > sum(works): return 0
    for i in range(n):
        works[works.index(max(works))] -= 1
    return sum(x**2 for x in works)


print(noOvertime(4,[4,4,3]))