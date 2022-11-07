for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    W_count =0
    B_count = 0
    R_count = 0
    for i in range(1,N-1):  #1 2
        for j in range(i+1, N): #  3
            W = arr[0:i]  # 0:1 0:2
            B = arr[i:j]  # 2:3
            R = arr[j:N]  # 3:4
            # for k in range(M):
            #     if arr[i-1][k] =='W':
            #         W_count += 1
            #         if arr[j-1][k] == 'B':
            #             W_count += 1
            #             if arr[N-1][k] == 'R':
            #                 W_count += 1
    print(f'#{tc}', N*M-(W_count))
