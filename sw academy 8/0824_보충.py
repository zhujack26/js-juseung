N = 7
arr = [[0] * N for _ in range(N)]
dc = [1, -1, 0, 0]
dr = [0, 0, -1, 1]
r = c = 3
arr[r][c] = '*'

for i in range(4):
    nr = r +dr[i]
    nc = c +dc[i]
    arr[nr][nc] = 1

for line in arr:
    print(*line)