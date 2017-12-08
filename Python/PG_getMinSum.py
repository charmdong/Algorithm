def getMinSum(A,B):
    return sum(map(lambda a,b : a*b, sorted(A), sorted(B, reverse=True)))

#아래 코드는 출력을 위한 테스트 코드입니다.

print(getMinSum([1,2],[3,4]))