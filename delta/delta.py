import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dr = [-1, 1, 0, 0]
    dc = [0, 0, 1, -1]

    ans = 0

    for r in range(N):
        for c in range(N):
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]

                if nr < 0  or nr > N-1 or nc < 0 or nc > N-1:
                    continue
                ans += abs(arr[r][c]-arr[nr][nc])
                # if 0 <= nr < N and 0 <= nc < N :
                    #ans += abs(arr[r][c]-arr[nr][nc]) 도 가능
    print(f"#{tc} {ans}")