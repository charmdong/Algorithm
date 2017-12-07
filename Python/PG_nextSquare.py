def nextSqure(n):
    tmp = n **(1/2)

    if tmp % 1==0:
        return (tmp+1)**2
    return 'no'

print("결과 : {}".format(nextSqure(213444)));