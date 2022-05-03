import sys
x= int(sys.stdin.readline())


for i in range(x) :
    data = list(map(str,sys.stdin.readline().strip()))
    
    count = 0
    amount = 0
    for j in data :
        if j == 'O' :
            count += 1
            amount += count
        else :
            count = 0
    print(amount)
          




