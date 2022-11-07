import sys
sys.stdin = open('input.txt')
for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dx = [1, -1]
    dy = [0, 0]
    for i in range(N):
        for j in range(N):
            if 0 <= i+dx[0] <N and arr[i][j] == 1: #1이 아래로 갈때
                if arr[i+dx[0]][j+dy[0]] == 0:
                    arr[i][j] = 0
                    arr[i+dx[0]][j+dy[0]] = 1
            if i + dx[0] == N and arr[i][j] == 1: #1이 아래 도착
                arr[i][j] = 0
            if 0 <= i+dx[1] <N and arr[i][j] == 2: #2가 위로 갈 때
                if arr[i+dx[1]][j+dy[1]] == 0:
                    arr[i][j] = 0
                    arr[i+dx[1]][j+dy[1]] = 2
            if i + dx[1] == -1 and arr[i][j] == 2: #2가 위 도착
                arr[i][j] = 0
    cnt = 0
    for i in range(N):
        for j in range(N):
            if i+1 <= N and arr[i][j] == 1 and arr[i+1][j] == 2:
                cnt += 1
    print(f'#{tc} {cnt}')

