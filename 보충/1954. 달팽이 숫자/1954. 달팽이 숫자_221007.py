for tc in range(1, int(input())+1):
    N = int(input())
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    arr = [[0] * N for _ in range(N)]
    # for i in range(N):
    #     for j in range(N):
    # for k in range(4):
    #     for l in range(N):
    #         if 0 <= 0 + dx[k] * l < N and 0 <= 0 + dy[k] * l < N:
    #             arr[0 + dx[k] * l][0 + dy[k] * l]
    #         for m in range(1, N*N+1):
    #
    #             if 0+dx[k]* l <0 or 0+dy[k]*l >= N:
    #                 break
    r, c = 0, 0
    for i in range(1, N*N+1):
        arr[r][c] = i
    for j in range(4):
        for k in range(N):
            if 0<= r + dx[j]*k < N and 0 <= c + dy[j]*k < N:




    print(f'#{tc} {arr}')
