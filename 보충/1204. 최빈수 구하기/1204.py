import sys
sys.stdin = open('input.txt')
for t in range(1, int(input())+1):
    tc = int(input())
    arr = list(map(int, input().split()))
    counting = [0]*101
    a = ''
    for i in arr:
        counting[i] += 1
        if max(counting)== counting[i]:
            a = i

    print(f'#{tc} {a}')