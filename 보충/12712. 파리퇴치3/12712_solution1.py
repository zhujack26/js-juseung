for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    da = [1, -1, 1, -1]
    db = [1, -1, -1, 1]

    # 상하좌우 + 중앙 합
    count_max = 0
    for i in range(N):
        for j in range(N):
            count = 0
            for l in range(1, M): #M의 세기 #M 2, 1
                for k in range(4):
                    if i+dx[k]*l < N and j+dy[k]*l < N:
                        count += arr[i+dx[k]*l][j+dy[k]*l]
                        if count > count_max:
                            count_max = count
    print(count_max)
    # 대각선 + 중앙 합