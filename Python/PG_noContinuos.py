def no_continuous(s):
    res =[]
    for i in range(len(s)):
        if i == 0 :
            res.append(s[i])
        else :
            if s[i] != res[len(res)-1]:
                res.append(s[i])
    return res

print( no_continuous( "133303" ))