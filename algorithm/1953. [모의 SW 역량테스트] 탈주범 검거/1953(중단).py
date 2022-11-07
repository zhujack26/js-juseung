T = int(input())
for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 터널 구조물 타입에 맞게
    dr = [0, 1, 0, -1 ]
    dc = [1, 0, -1, 0 ] #우하좌상 (달팽이 경로)
    direction = 0

    result = set((R,C))  #초기 값 설정
    for i in range(1, L):
        if arr[R][C] == 1 : #상하좌우
            R += dr[0]
            C += dc[0]
            result += (R+1, C)
            result += (R-1, C)
            result += (R, C+1)
            result += (R, C-1)
        if arr[R][C] == 2: #상하
            result += (R+1, C)
            result += (R-1, C)
        if arr[R][C] == 3: #좌우
            result += (R, C+1)
            result += (R, C-1)
            C = C+1, C-1
        if arr[R][C] == 4, #상우
        if arr[R][C] == 5, #하우
        if arr[R][C] == 6, #하좌
        if arr[R][C] == 7, #상좌
        if arr[R][C] == 0 :
            result.remove((R, C))

