import re

while True :
    test = input()
    if test == '#' : break
    test = test.lower()

    p = re.findall('a|e|i|o|u',test)
    print(len(p))