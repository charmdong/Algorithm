def Jaden_Case(s):
    return " ".join(x[0].upper() + x[1:].lower() for x in s.split())

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(Jaden_Case("3people unFollowed me for the last week"))