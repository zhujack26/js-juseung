T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    row_count = 0
    column_count = 0
    r_count = []
    c_count = []
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:  # 1일 때마다 count 더해주기
                row_count += 1
            if arr[i][j] == 0 or j == M - 1:  # 탐색 멈추는 조건
                r_count.append(row_count)
                row_count = 0

    for i in range(M):
        for j in range(N):
            if arr[j][i] == 1:
                column_count += 1
            if arr[j][i] == 0 or j == N - 1:
                c_count.append(column_count)
                column_count = 0

    print(f'#{tc} {max(r_count+c_count)}')