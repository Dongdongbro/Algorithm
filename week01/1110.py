import sys

a = str(sys.stdin.readline())
result1 = ''
result2 = ''
count =1

if int(a)<10 :
    a = "0".join(a)

result1 = int(a[0]) + int(a[1])
tmp = str(result1)
result2 = a[1]+tmp[-1:]



while result2 != a :
    count += 1
    result1  = int(result2[0]) + int(result2[1])
    tmp = str(result1)
    result2 = result2[1]+tmp[-1:]

    if int(result2)==int(a) :
        break

if int(a) == 00 :
    print(count-1)
else :
    print(count)