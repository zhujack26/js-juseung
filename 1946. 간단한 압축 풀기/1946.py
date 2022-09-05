import sys
sys.stdin = open('input.txt')
T = int(input())
for t in range(1, T + 1):
    N = int(input())
    Ci_list = ""
    for i in range(N):
        Ci, Ni = map(str, input().split())
        Ni_int = int(Ni)
        Ci_list += Ci * Ni_int
    for i in range(0, len(Ci_list), 10):
        print(Ci_list[i:i+10])