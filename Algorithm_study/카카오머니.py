input = __import__('sys').stdin.readline

N = int(input())

log = [list(map(int, input().split())) for i in range(N)]

if len(log) == 1 :
    print(1)
else :
    account = 0
    remain = 0
    charge = []

    for money, remains in log :
        if money > 0 :
            remain = remains
        else :
            if remain < abs(money) :
                charge.append(remains - money - remain)
            remain = remains
    charge.sort()
    change = charge[0]
    flag = 0
    if len(charge) == 0 :
        print(1)
    elif len(charge) == 1 :
        print(charge[0])
    else :
        for charges in charge[1:] :
            if charges % change != 0 :
                print(-1)
                flag = 1
                break
            else :
                change = charges

        if not flag :
            print(min(charge))

