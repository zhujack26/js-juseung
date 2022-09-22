import sys
sys.stdin = open('input.txt')
# 시작점을 찾는 함수
def find_start(arr):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                return i, j


# BFS 구현
def BFS(rs, cs):
    visited = [[False] * N for _ in range(N)]
    queue = []
    queue.append((rs, cs))
    visited[rs][cs] = True

    while queue:
        r, c = queue.pop(0)
        # 도착점 '3'에 도착하면, return 1
        if arr[r][c] == 3:
            return 1

        # 상하좌우 움직임 구현
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            next_r, next_c = r + dr, c + dc
            if arr[next_r][next_c] != 1 and visited[next_r][next_c] == False:
                queue.append((next_r, next_c))
                visited[next_r][next_c] = True

    return 0


def DFS(rs, cs):
    visited = [[False] * N for _ in range(N)]
    stack = []
    stack.append((rs, cs))
    visited[rs][cs] = True

    while stack:
        r, c = stack[-1]
        # 도착점 '3'에 도착하면, return 1
        if arr[r][c] == 3:
            return 1

        # 상하좌우 움직임 구현
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            next_r, next_c = r + dr, c + dc
            if arr[next_r][next_c] != 1 and visited[next_r][next_c] == False:
                stack.append((next_r, next_c))
                visited[next_r][next_c] = True
                break
        else:
            stack.pop()

    return 0


for _ in range(10):
    tc = int(input())
    N = 100
    arr = [list(map(int, input())) for _ in range(N)]

    rs, cs = find_start(arr)

    # print(f'#{tc} {BFS(rs, cs)}')
    print(f'#{tc} {BFS(rs, cs)}')