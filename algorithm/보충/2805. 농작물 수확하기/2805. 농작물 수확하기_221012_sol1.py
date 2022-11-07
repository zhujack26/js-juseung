for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    x, y = N//2 , N//2
    rx = [0, 0, -1, 1]
    ry = [1, -1, 0, 0]
    cnt = 0
    for i in range(N):
        cnt += arr[x][i]
        arr[N//2][i] = 0
    if N != 1:
        for i in range(N//2):
            x_1 = x - i
            x_2 = x + i
            for p in range((N//2)+1-i):
                for d in range(4):
                    if 0<= x_1+rx[d]*p :
                        cnt += arr[x_1+rx[d]*p][y+ry[d]*p]
                        arr[x_1+rx[d]*p][y+ry[d]*p] = 0

            for p in range((N//2)+1-i):
                for d in range(4):
                    if x_2+rx[d]*p < N:
                        cnt += arr[x_2+rx[d]*p][y+ry[d]*p]
                        arr[x_2+rx[d]*p][y+ry[d]*p] = 0
    print(f'#{tc} {cnt}')