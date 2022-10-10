for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    result = 'possible'
    for i in range(N):
        for j in range(M):
            for d in range(4):
                if arr[i][j] == '#' and 0<= i+dx[d]< N and 0<= j+dy[d] <M and arr[i+dx[d]][j+dy[d]] == '?':
                    arr[i+dx[d]][j+dy[d]] = '.'
                if arr[i][j] == '.' and 0<= i+dx[d]< N and 0<= j+dy[d] <M and arr[i+dx[d]][j+dy[d]] == '?':
                    arr[i + dx[d]][j + dy[d]] = '#'
            if arr[i][j] != '?':
                for d_2 in range(4):
                    if 0<= i+dx[d_2]< N and 0<= j+dy[d_2] <M and arr[i][j] == arr[i+dx[d_2]][j+dy[d_2]]:
                        result = 'impossible'
    print(f'#{tc} {result}')