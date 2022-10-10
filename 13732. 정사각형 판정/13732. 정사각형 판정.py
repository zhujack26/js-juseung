for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    ans = 'no'
    fx = [0, 1, 1]   #오른쪽, 대각선 아래, 아래 검증
    fy = [1, 1, 0]

    for i in range(N):
        for j in range(N):
            for p in range(1, N):
                if arr[i][j] =='#' and arr[i+fx[0]*p][j+fy[0]*p] != '#' or j+fy[0]*p== N:
                    arr[i+fx[0]*(p-1)][j+fy[0]*(p-1)]
    print(ans)
