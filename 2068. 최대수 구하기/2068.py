import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = list(map(int, input().split()))
    N.sort(reverse=True)
    print(f"#{tc}", N[0])