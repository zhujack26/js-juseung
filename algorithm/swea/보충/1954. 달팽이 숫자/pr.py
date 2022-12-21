# import sys
# sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    r,c = 1,1
    arr[r][c] = '*'
    for i in range(N):
        nr = r + dr[1]
        nc = c + dc[1]
        if nr <N and nc < N:
            arr[nr][nc] = 1
            r = nr
            c = nc
    print(arr)
