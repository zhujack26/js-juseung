import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = list(map(int, input().split()))

    print(f"#{tc}", (round((sum(N)/len(N)))))