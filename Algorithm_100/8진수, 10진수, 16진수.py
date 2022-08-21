input = __import__('sys').stdin.readline

x = input()
len_x = len(x)-1
sum = 0
if int(x[0]) > 0 :
    print(x)
elif x[0] == '0' and x[1] != 'x' :
    for i in range(1, len_x) :
        if len_x-i == 1 :
            sum += int(x[i])
        else :
            sum += int(x[i]) * 8 ** (len_x-1-i)
    print(sum)

elif x[0] == '0' and x[1] == 'x' :
    for i in range(2, len_x) :
        if len_x-i == 1 :
            if 97 <= ord(x[i]) <= 102 :
                a = ord(x[i]) - 87
                sum += a
            else :
                sum += int(x[i])
        else :
            if 97 <= ord(x[i]) <= 102 :
                a = ord(x[i]) - 87
                sum += a * 16 ** (len_x-1-i)
            else :
                sum += int(x[i]) * 16 ** (len_x-1-i)
    print(sum)