def getDayName(a,b):
    day ={3:"MON",4:"TUE",5:"WED",6:"THU",0:"FRI",1:"SAT",2:"SUN"}
    date = [31,29,31,30,31,30,31,31,30,31,30,31]
    return day[(sum(date[:a-1])+b-1)%7]


#아래 코드는 테스트를 위한 출력 코드입니다.
print(getDayName(5,24))