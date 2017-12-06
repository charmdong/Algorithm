string = input()

for i in range(26):
    print(string.find(chr(97+i)), end=" ")
