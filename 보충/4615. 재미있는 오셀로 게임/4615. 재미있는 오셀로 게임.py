for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    dx = [0, 0, 1, -1, 1, 1, -1, -1]
    dy = [-1, 1, 0, 0, 1, -1, 1, -1]
    arr = [[0] *N for _ in range(N)]
    arr[N//2-1][N//2-1] =2
    arr[N//2][N//2] = 2 #배치된 2개 백돌
    arr[N//2-1][N//2] =1
    arr[N//2][N//2-1] =1 #배치된 2개 흑돌
    for i in range(M):
        r,c,color = map(int, input().split())
        r = r-1
        c = c-1
        if color == 1 :
            arr[r][c] = 1
            for d in range(8):  # 8방향 탐색을 해서
                for p in range(1, 2):
                    if arr[r][c] == 1 and 0 <= r + dx[d] * (p + 1) < N and 0 <= c + dy[d] * (p + 1) < N:
                        if arr[r + dx[d] * p][c + dy[d] * p] == 2 and arr[r + dx[d] * (p + 1)][c + dy[d] * (p + 1)] == 1:
                            arr[r + dx[d] * p][c + dy[d] * p] = 1
                            break
                    if arr[r][c] == 1 and 0 <= r + dx[d] * (p + 2) < N and 0 <= c + dy[d] * (p + 2) < N:
                        if arr[r + dx[d] * p][c + dy[d] * p] == 2 and arr[r + dx[d] * (p + 1)][c + dy[d] * (p + 1)] == 2 and arr[r + dx[d] * (p + 2)][c + dy[d] * (p + 2)] == 1:
                            arr[r + dx[d] * p][c + dy[d] * p] = 1
                            arr[r + dx[d] * (p + 1)][c + dy[d] * (p + 1)] = 1
                            break
                    if arr[r][c] == 1 and 0 <= r + dx[d] * (p + 3) < N and 0 <= c + dy[d] * (p + 3) < N:
                        if arr[r + dx[d] * p][c + dy[d] * p] == 2 and arr[r + dx[d] * (p + 1)][c + dy[d] * (p + 1)] == 2 and arr[r + dx[d] * (p + 2)][c + dy[d] * (p + 2)] == 2 and arr[r + dx[d] * (p + 3)][c + dy[d] * (p + 3)] == 1:
                            arr[r + dx[d] * p][c + dy[d] * p] = 1
                            arr[r + dx[d] * (p + 1)][c + dy[d] * (p + 1)] = 1
                            arr[r + dx[d] * (p + 2)][c + dy[d] * (p + 2)] = 1
                            break
                    if arr[r][c] == 1 and 0 <= r + dx[d] * (p + 4) < N and 0 <= c + dy[d] * (p + 4) < N:
                        if arr[r + dx[d] * p][c + dy[d] * p] == 2 and arr[r + dx[d] * (p + 1)][c + dy[d] * (p + 1)] == 2 and arr[r + dx[d] * (p + 2)][c + dy[d] * (p + 2)] == 2 and arr[r + dx[d] * (p + 3)][c + dy[d] * (p + 3)] == 2 and arr[r + dx[d] * (p + 4)][c + dy[d] * (p + 4)] == 1:
                            arr[r + dx[d] * p][c + dy[d] * p] = 1
                            arr[r + dx[d] * (p + 1)][c + dy[d] * (p + 1)] = 1
                            arr[r + dx[d] * (p + 2)][c + dy[d] * (p + 2)] = 1
                            arr[r + dx[d] * (p + 3)][c + dy[d] * (p + 3)] = 1
                            break
                    if arr[r][c] == 1 and 0 <= r + dx[d] * (p + 5) < N and 0 <= c + dy[d] * (p + 5) < N:
                        if arr[r + dx[d] * p][c + dy[d] * p] == 2 and arr[r + dx[d] * (p + 1)][c + dy[d] * (p + 1)] == 2 and arr[r + dx[d] * (p + 2)][c + dy[d] * (p + 2)] == 2 and arr[r + dx[d] * (p + 3)][c + dy[d] * (p + 3)] == 2 and arr[r + dx[d] * (p + 4)][c + dy[d] * (p + 4)] == 2 and arr[r + dx[d] * (p + 5)][c + dy[d] * (p + 5)] == 1:
                            arr[r + dx[d] * p][c + dy[d] * p] = 1
                            arr[r + dx[d] * (p + 1)][c + dy[d] * (p + 1)] = 1
                            arr[r + dx[d] * (p + 2)][c + dy[d] * (p + 2)] = 1
                            arr[r + dx[d] * (p + 3)][c + dy[d] * (p + 3)] = 1
                            arr[r + dx[d] * (p + 4)][c + dy[d] * (p + 4)] = 1
                            break
                    if arr[r][c] == 1 and 0 <= r + dx[d] * (p + 6) < N and 0 <= c + dy[d] * (p + 6) < N:
                        if arr[r + dx[d] * p][c + dy[d] * p] == 2 and arr[r + dx[d] * (p + 1)][
                            c + dy[d] * (p + 1)] == 2 and arr[r + dx[d] * (p + 2)][c + dy[d] * (p + 2)] == 2 and \
                                arr[r + dx[d] * (p + 3)][c + dy[d] * (p + 3)] == 2 and arr[r + dx[d] * (p + 4)][
                            c + dy[d] * (p + 4)] == 2 and arr[r + dx[d] * (p + 5)][c + dy[d] * (p + 5)] == 2 and \
                                arr[r + dx[d] * (p + 6)][c + dy[d] * (p + 6)] == 1:
                            arr[r + dx[d] * p][c + dy[d] * p] = 1
                            arr[r + dx[d] * (p + 1)][c + dy[d] * (p + 1)] = 1
                            arr[r + dx[d] * (p + 2)][c + dy[d] * (p + 2)] = 1
                            arr[r + dx[d] * (p + 3)][c + dy[d] * (p + 3)] = 1
                            arr[r + dx[d] * (p + 4)][c + dy[d] * (p + 4)] = 1
                            arr[r + dx[d] * (p + 5)][c + dy[d] * (p + 5)] = 1
                            break
        if color == 2 :
            arr[r][c] = 2
            for d in range(8):  # 8방향 탐색을 해서
                for p in range(1, 2):
                    if arr[r][c] == 2 and 0 <= r+dx[d]*(p+1) <N and 0<= c+dy[d]*(p+1) <N:
                        if arr[r+dx[d]*p][c+dy[d]*p]== 1 and arr[r+dx[d]*(p+1)][c+dy[d]*(p+1)] == 2 :
                            arr[r+dx[d]*p][c+dy[d]*p] = 2
                            break
                    if arr[r][c] == 2 and 0 <=r+dx[d]*(p+2)<N and 0<=c+dy[d]*(p+2)<N:
                        if arr[r+dx[d]*p][c+dy[d]*p] == 1  and arr[r+dx[d]*(p+1)][c+dy[d]*(p+1)]== 1 and arr[r+dx[d]*(p+2)][c+dy[d]*(p+2)] == 2 :
                            arr[r+dx[d]*p][c+dy[d]*p] = 2
                            arr[r+dx[d]*(p+1)][c+dy[d]*(p+1)] = 2
                            break
                    if arr[r][c] == 2 and 0 <= r + dx[d] * (p + 3) < N and 0 <= c + dy[d] * (p + 3) < N:
                        if arr[r+dx[d]*p][c+dy[d]*p] == 1 and arr[r+dx[d]*(p+1)][c+dy[d]*(p+1)] == 1 and arr[r+dx[d]*(p+2)][c+dy[d]*(p+2)] == 1 and arr[r+dx[d]*(p+3)][c+dy[d]*(p+3)] == 2:
                            arr[r + dx[d] * p][c + dy[d] * p] = 2
                            arr[r + dx[d] * (p + 1)][c + dy[d] * (p + 1)] = 2
                            arr[r + dx[d] * (p + 2)][c + dy[d] * (p + 2)] = 2
                            break
                    if arr[r][c] == 2 and 0 <= r + dx[d] * (p +4) < N and 0 <= c + dy[d] * (p + 4) < N:
                        if arr[r+dx[d]*p][c+dy[d]*p] == 1 and arr[r+dx[d]*(p+1)][c+dy[d]*(p+1)] == 1 and arr[r+dx[d]*(p+2)][c+dy[d]*(p+2)] == 1 and arr[r+dx[d]*(p+3)][c+dy[d]*(p+3)] == 1 and arr[r+dx[d]*(p+4)][c+dy[d]*(p+4)] == 2:
                            arr[r + dx[d] * p][c + dy[d] * p] = 2
                            arr[r + dx[d] * (p + 1)][c + dy[d] * (p + 1)] = 2
                            arr[r + dx[d] * (p + 2)][c + dy[d] * (p + 2)] = 2
                            arr[r + dx[d] * (p + 3)][c + dy[d] * (p + 3)] = 2
                            break
                    if arr[r][c] == 2 and 0 <= r + dx[d] * (p + 5) < N and 0 <= c + dy[d] * (p + 5) < N:
                        if arr[r+dx[d]*p][c+dy[d]*p] == 1 and arr[r+dx[d]*(p+1)][c+dy[d]*(p+1)] == 1 and arr[r+dx[d]*(p+2)][c+dy[d]*(p+2)] == 1 and arr[r+dx[d]*(p+3)][c+dy[d]*(p+3)] == 1 and arr[r+dx[d]*(p+4)][c+dy[d]*(p+4)] == 1 and arr[r+dx[d]*(p+5)][c+dy[d]*(p+5)] == 2:
                            arr[r + dx[d] * p][c + dy[d] * p] = 2
                            arr[r + dx[d] * (p + 1)][c + dy[d] * (p + 1)] = 2
                            arr[r + dx[d] * (p + 2)][c + dy[d] * (p + 2)] = 2
                            arr[r + dx[d] * (p + 3)][c + dy[d] * (p + 3)] = 2
                            arr[r + dx[d] * (p + 4)][c + dy[d] * (p + 4)] = 2
                            break
                    if arr[r][c] == 2 and 0 <= r + dx[d] * (p + 6) < N and 0 <= c + dy[d] * (p + 6) < N:
                        if arr[r+dx[d]*p][c+dy[d]*p] == 1 and arr[r+dx[d]*(p+1)][c+dy[d]*(p+1)] == 1 and arr[r+dx[d]*(p+2)][c+dy[d]*(p+2)] == 1 and arr[r+dx[d]*(p+3)][c+dy[d]*(p+3)] == 1 and arr[r+dx[d]*(p+4)][c+dy[d]*(p+4)] == 1 and arr[r+dx[d]*(p+5)][c+dy[d]*(p+5)] == 1 and arr[r+dx[d]*(p+6)][c+dy[d]*(p+6)] == 2:
                            arr[r + dx[d] * p][c + dy[d] * p] = 2
                            arr[r + dx[d] * (p + 1)][c + dy[d] * (p + 1)] = 2
                            arr[r + dx[d] * (p + 2)][c + dy[d] * (p + 2)] = 2
                            arr[r + dx[d] * (p + 3)][c + dy[d] * (p + 3)] = 2
                            arr[r + dx[d] * (p + 4)][c + dy[d] * (p + 4)] = 2
                            arr[r + dx[d] * (p + 5)][c + dy[d] * (p + 5)] = 2
                            break
    cnt_b = 0
    cnt_w = 0
    for j in range(N):
        for k in range(N):
            if arr[j][k] == 1:
                cnt_b += 1
            if arr[j][k] == 2:
                cnt_w += 1
    print(f'#{tc} {cnt_b} {cnt_w}')
