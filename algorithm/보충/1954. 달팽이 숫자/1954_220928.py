# import sys
# sys.stdin = open('input.txt')
for tc in range(1, int(input())+1):
    N, M = map(int, (input().split()))
    arr = [[0] *N for _ in range(N)]
    # dr = [-1, 1, 0, 0]
    # dc = [0, 0, 1, -1]
    ans = 0
    for i in range(N):
        for j in range(N):
            kill = arr[i][j]
            for k in range(1, M):
                if i + k < N and i - k >= 0 and j + k < N and j - k >= 0:
                    kill += arr[i + k][j]
                    kill += arr[i][j + k]
                    kill += arr[i - k][j]
                    kill += arr[i][j - k]
            ans = max(ans, kill)

    for i in range(N):
        for j in range(N):
            kill = arr[i][j]
            for k in range(1, M):
                if i + k < N and i - k >= 0 and j + k < N and j - k >= 0:
                    kill += arr[i + k][j + k]
                    kill += arr[i + k][j - k]
                    kill += arr[i - k][j - k]
                    kill += arr[i - k][j + k]
            ans = max(ans, kill)

    print(ans)