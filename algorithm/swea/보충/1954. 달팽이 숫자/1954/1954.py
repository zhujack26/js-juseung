import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    dr = [0, 1, 0, -1 ]
    dc = [1, 0, -1, 0 ] #우하좌상 tc 안, 밖 상관 없다
    r, c = 0, 0  # 초기값 설정
    direction = 0 # 방향 초기값 설정  #우0 하:1 좌:2 상:3

    count = 0
    for i in range(1, N*N +1):
        arr[r][c] = i
        # N*N 만큼 숫자를 찍으며 돌아야 하므로
        r += dr[direction]
        c += dc[direction]
        # ex) 0 += 0
        # ex) 1 += 1 2..3..4 계속 우측으로 이동

        if r < 0 or c <0 or r>= N or c >= N or arr[r][c] !=0:
            r -= dr[direction]
            c -= dc[direction]
            direction = (direction +1) % 4

            r += dr[direction]
            c += dc[direction]

    print(f'#{tc} ')
    for i in arr:
        print(*i)
