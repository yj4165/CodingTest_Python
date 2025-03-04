import sys

N = int(sys.stdin.readline()) 
arr1 = set(map(int, sys.stdin.readline().split()[:N])) 
M = int(sys.stdin.readline())  
arr2 = list(map(int, sys.stdin.readline().split()[:M]))

for q in arr2:
    if q in arr1:
        print("1", end=" ")
    else:
        print("0", end=" ")