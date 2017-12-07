def string_middle(str) :
    if len(str)%2 !=0 :
        return str[int(len(str)/2)]
    return (str[int(len(str)/2)-1]+str[int(len(str)/2)])

print(string_middle("power"))
print(string_middle("TEST"))