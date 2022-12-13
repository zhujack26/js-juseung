# MxN 행렬을 돌면서, 경로 지나면서 빈 칸은 1로 메꾸기
M, N, K = map(int, input().split())
arr = [[0]*N for _ in range(M)]

# 1. 2차원 리스트에 사각형 채우기
for _ in range(K):
    x_1, y_1, x_2, y_2 = map(int, input().split())
    for i in range(y_1, y_2):  #여기서 x,y 헷갈리지 않게 주의
        for j in range(x_1, x_2):
            arr[i][j] = 1
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
count_total = []

# 2. 0 인곳 1로 만들어주고 카운팅하여 넓이 구하기
for i in range(M):
    for j in range(N):
        if arr[i][j] == 0:
            stack = [(i, j)]
            count = 0

            while stack:
                current = stack.pop()
                if arr[current[0]][current[1]] == 0:
                    arr[current[0]][current[1]] = 1
                    count += 1

                    for k in range(4):
                        if 0 <= current[0] + dx[k] < M and 0 <= current[1] + dy[k] < N:
                            if arr[current[0] + dx[k]][current[1] + dy[k]] == 0:
                                stack.append((current[0] + dx[k], current[1] + dy[k]))
            count_total.append(count)
            # 1로 만들어주었다면, 만든 구역 넓이 추가
print(len(count_total))
print(*sorted(count_total))
