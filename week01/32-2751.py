import sys

def orum(array) :
    if len(array) <= 1 : #길이가 1보다 작을때는 그냥 실행
        return array
    mid = len(array)//2 
    left = orum(array[:mid]) #길이가 5면 0~1까지 left
    right = orum(array[mid:])

    i,j,k =0,0,0
    
    while i < len(left) and j < len(right) :
        if left[i] < right[j] :
            array[k] = left[i]
            i += 1 

        else :
            array[k] = right[j]
            j += 1
        k += 1
    
    
    if i == len(left) :
        while j < len(right) :
            array[k] = right[j]
            j += 1
            k += 1
    elif j == len(right) :
        while i <len(left) :
            array[k] = left[i]
            i += 1
            k += 1
    
    return array

a = int(sys.stdin.readline())
data = []
for i in range(a):
   
    data.append(int(sys.stdin.readline()))

data = orum(data)
for _ in data :
    print(_)