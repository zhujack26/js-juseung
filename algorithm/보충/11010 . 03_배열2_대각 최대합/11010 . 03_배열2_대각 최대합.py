for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dx = [1, 1, -1, -1]
    dy = [1, -1, 1, -1]
    max_box = []

    for i in range(N):
        for j in range(N):
            box = arr[i][j]
            for k in range(4):
                for l in range(1, N):
                    if 0<= i+dx[k]*l <N and 0<= j+dy[k]*l < N:
                        box += arr[i+dx[k]*l][j+dy[k]*l]
            max_box.append(box)
    print(f'#{tc}', max(max_box))
