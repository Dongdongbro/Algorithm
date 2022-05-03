import sys
input = sys.stdin.readline

a = list(map(str,input().strip()))
b = list(map(str,input().strip()))
stack = []


for i in a :
    stack.append(i)
    if stack[-1] == b[-1] :
        if len(stack) >= len(b) :
            if stack[-len(b):] == b:
                for i in range(len(b)) :
                    stack.pop()
if stack :
    print("".join(stack))
else :
    print("FRULA")




