for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    cnt = 0
    for i in range(M):
        x,y,power = map(int, input().split()) #폭발 위치, 폭발 파워
        for direction in range(4): # 폭발 방향
            for p in range(power+1): # 폭발력
                if 0 <= x + dx[direction]*p < N and 0 <= y + dy[direction]*p < N :
                    cnt += arr[x + dx[direction]*p][y + dy[direction]*p]
                    arr[x + dx[direction]*p][y + dy[direction]*p] = 0
    print(f'#{tc} {cnt}')

