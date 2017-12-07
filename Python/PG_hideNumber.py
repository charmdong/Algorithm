def hide_numbers(string):
    return '*' *(len(string)-4) + string[-4:]

print("결과 : " + hide_numbers('01033334444'));