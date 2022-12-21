for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    da = [1, -1, 1, -1]
    db = [1, -1, -1, 1]

    # 상하좌우 + 중앙 합
    result = 0
    for i in range(N):
        for j in range(N):
            count = arr[i][j]
            for l in range(1, M): #M의 세기 M은 2 이상 N 이하
                for k in range(4):
                    if 0<= i+dx[k]*l < N and 0<= j+dy[k]*l < N:
                        count += arr[i+dx[k]*l][j+dy[k]*l]
            if count > result:
                result = count

    # 대각선 + 중앙 합
    result2 = 0
    for i in range(N):
        for j in range(N):
            count = arr[i][j]
            for l in range(1, M):  # M의 세기 #M 2, 1 #M은 2 이상 N 이하
                for k in range(4):
                    if 0<= i+da[k]*l < N and 0<= j+db[k]*l < N:
                        count += arr[i+da[k]*l][j+db[k]*l]
            if count > result2:
                result2 = count
    print(f'#{tc}', max(result,result2))