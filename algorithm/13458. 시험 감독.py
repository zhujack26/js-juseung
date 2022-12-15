import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B, C = map(int, sys.stdin.readline().split())
count = 0
for i in range(len(A)):
    if A[i]-B > 0 :
        if (A[i]-B)%C == 0:
            count += (A[i]-B)//C+1
        elif (A[i]-B)%C != 0:
            count += (A[i]-B)//C+2
    elif A[i]-B<= 0:
        count += 1
print(count)