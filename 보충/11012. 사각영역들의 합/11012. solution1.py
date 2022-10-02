for tc in range(1, int(input())+1):
    N, M = map(int, input().split())  #배열의 크기 N과 정사각 영역의 수 M
    arr = [list(map(int, input().split())) for _ in range(N)]
    for i in range(M):
        r, c, l = map(int, input().split()) # 좌상단 위치 ,변의 길이
        cnt = 0
        for j in range(l):
            for k in range(l):
                if r+j < N and c+k < N:
                    cnt += arr[r+j][c+k]
                    arr[r+j][c+k] = 0
    print(f'#{tc} {cnt}')

