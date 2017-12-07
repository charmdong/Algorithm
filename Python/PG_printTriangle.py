def printTriangle(num):
    s =""
    for i in range(num):
        s +='*'*(i+1)
        s += '\n'
        return s

print(printTriangle(3))
