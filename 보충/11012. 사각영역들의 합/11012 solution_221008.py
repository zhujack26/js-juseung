for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    count = 0
    for i in range(M):
        x,y,l = map(int, input().split())
        for j in range(l):
            for k in range(l):
                if 0 <= x+j < N and 0 <= y+k <N:
                #정사각형 구하는게 기억이 안남..
                    count += arr[x+j][y+k]
                    arr[x + j][y + k] = 0
    print(f'#{tc} {count}')