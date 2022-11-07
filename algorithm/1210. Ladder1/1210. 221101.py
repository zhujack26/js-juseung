import sys
sys.stdin = open('input.txt')
for tc in range(1, 11):
    T = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    c = 0
    r = 99
    result = 0
    for i in range(99):
        if arr[99][i] == 2:
            c = i
    dx = [0, -1, 0] #좌 위 우
    dy = [-1, 0, 1]
    dir = 1
    for i in range(10000):
        if arr[r][c] == 1 and 0< r < 99 and c == 0:
            dir = 1
        elif arr[r][c] == 1 and 0< r < 99 and c == 99:
            dir = 1
        if 0<= c+dy[dir] < 100 and arr[r+dx[dir]][c+dy[dir]] == 1:
            r = r + dx[dir]
            c = c + dy[dir]
            if r == 0:
                result = c
                break
            elif 0<= r+dx[0] < 100 and 0<= c+dy[0] < 100 and dir == 1 and arr[r+dx[0]][c+dy[0]] == 1:
                dir = 0
            elif 0<= r+dx[2] < 100 and 0<= c+dy[2] < 100 and dir == 1 and arr[r+dx[2]][c+dy[2]] == 1:
                dir = 2
        elif arr[r+dx[dir]][c+dy[dir]] == 0:
            if dir == 0 :
                dir = 1
            elif dir == 2 :
                dir = 1


    print(f'#{tc} {result}')