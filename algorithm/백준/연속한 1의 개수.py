T = int(input())
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
for tc in range(T):
    N = int(input())
    surround_sum = 0
    arr = [list(map(int, input().split())) for _ in range(N)]
    #print(arr)

    for i in range(N): # 행 탐색
        for j in range(N): # 열 탐색
            for k in range(4): # 4방향 인접 요소를 탐색
                ni = i + di[k] # 만약 i=0, k=0, ni=0 / i=0, k=1, ni=1
                nj = j + dj[k] # 만약 j=0, k=0, nj=1 / j=0, k=1, nj=0
                # 따라서 arr[0][0] 인접한 요소는 arr[0][1], arr[1][0]
                if (0 <= ni < N) and (0 <= nj < N):
                    if (arr[ni][nj] - arr[i][j]) > 0:
                        surround_sum = surround_sum + (arr[ni][nj] - arr[i][j])
                    else: #음수값이 나왔을 경우 '-'를 곱해준다
                        surround_sum = surround_sum - (arr[ni][nj] - arr[i][j])

    print(f'#{tc+1} {surround_sum}')