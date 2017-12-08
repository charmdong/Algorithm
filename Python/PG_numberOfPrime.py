def numberOfPrime(n):
    prime = []
    for i in range(2, n+1):
        if i == 2 : prime.append(i)
        check = 0
        for j in prime :
            if i%j != 0 : check+=1
        if check == len(prime) : prime.append(i)

    return len(prime)


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(numberOfPrime(315))