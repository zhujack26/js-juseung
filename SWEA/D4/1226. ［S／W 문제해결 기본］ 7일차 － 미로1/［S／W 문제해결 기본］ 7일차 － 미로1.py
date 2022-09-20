def maze_call(r, c):
    ans = 0
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                r, c = i, j
    Q = [[r, c]] # 기본시작점 setting
    visited = [] # 방문하는 곳들을 저장할 빈 list를 생성
    while Q: # Q의 원소가 있을 동안에
        [r, c] = Q.pop() # 시작점을 뽑아내고
        visited.append([r, c]) # 방문한 곳에 담고
        for i in range(4): # 방향전환
            r1 = r + dr[i]
            c1 = c + dc[i]

            if 0 <= r1 < 16 and 0 <= c1 < 16: # index error를 방지하는 조건
                if not maze[r1][c1] and [r1, c1] not in visited: # maze[r1][c1] == 0일때
                    Q.append([r1, c1]) #
                if maze[r1][c1] == 3:
                    ans = 1
                    break
    return ans


T = 10
for test_case in range(1, T + 1):
    tc = int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    dr = [0, 1, 0, -1]  # 우 -> 하 -> 좌 -> 상이 한 사이클이라고 생각
    dc = [1, 0, -1, 0]  # 우하좌상
    print(f'#{test_case} {maze_call(0,0)}')

    maze_call(0, 0)