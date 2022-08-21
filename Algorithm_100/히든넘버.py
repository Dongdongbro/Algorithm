# import sys
# input = sys.stdin.readline
input = __import__('sys').stdin.readline
import re

n = int(input())
dan_auh = input().strip()

# dan_auh = re.split("[a-z]+",dan_auh)
dan_auh = re.findall("[0-9]+",dan_auh)
# print(dan_auh)
dan_auh = list(map(int,dan_auh))
print(sum(dan_auh))
