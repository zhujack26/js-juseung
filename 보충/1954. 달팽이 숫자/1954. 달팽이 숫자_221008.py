for tc in range(1, int(input())+1):
    N = int(input())
    dx = [0, 1, 0, -1] #우하좌상
    dy = [1, 0, -1, 0]
    arr = [[0] * N for _ in range(N)]
    start_r, start_c = 0, 0
    direction = 0
    for i in range(1, N*N+1):
        arr[start_r][start_c] = i
        if start_r + dx[direction%4] < 0 or start_r + dx[direction%4] == N or start_c + dy[direction%4] < 0 or start_c + dy[direction%4] == N or arr[start_r+dx[direction%4]][start_c+dy[direction%4]] != 0:
            direction += 1
        start_r += dx[direction % 4]
        start_c += dy[direction % 4]

    print(f'#{tc}')
    for i in range(N):
        print(*arr[i])
    """
    for i in arr:
        print(*i) 도 가능
    """

