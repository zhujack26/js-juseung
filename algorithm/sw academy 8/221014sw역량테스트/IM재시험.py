for tc in range(1, int(input())+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dx = [0, 1, 0, -1] # 우 하 좌 상
    dy = [1, 0, -1, 0]
    s_x = 0
    s_y = 0
    result = []
    for i in range(1, (N-K+1)+1):
        for j in range(1, (N-K+1)+1):
            s_x, s_y = i-1, j-1
            count = 0
            for dir in range(4):
                for p in range(1, K):
                    s_x += dx[dir]
                    s_y += dy[dir]
                    count += arr[s_x][s_y]
                    result.append(count)
    print(f'#{tc} {max(result)}')

