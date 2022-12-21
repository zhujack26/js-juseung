for tc in range(1, int(input())+1):
    H, W = map(int, input().split())
    arr = [list(input()) for _ in range(H)]
    N = int(input())  #입력의 개수
    N_list = list(input()) #길이가 N인 문자열
    dx = [0, 0, -1, 1]    #좌우상하
    dy = [-1, 1, 0, 0]
    direction = ['<', '>', '^', 'v']
    s_i, s_j = 0, 0  #시작점
    for i in range(H):
        for j in range(W):
            if arr[i][j] == '<' or arr[i][j] == '>' or arr[i][j] == '^' or arr[i][j] == 'v':
                s_i, s_j = i, j
    for k in range(N) :  # N_list 순회
        if N_list[k] == 'S':
            for l in range(max(H, W)):
                if arr[s_i][s_j] == '<' and 0<= s_i+dx[0]*l< H and 0<= s_j+dy[0]*l<W:
                    if arr[s_i+dx[0]*l][s_j+dy[0]*l] == '#':
                        break
                    if arr[s_i+dx[0]*l][s_j+dy[0]*l] == '*':
                        arr[s_i+dx[0]*l][s_j+dy[0]*l] = '.'
                        break
                if arr[s_i][s_j] == '>' and 0<= s_i+dx[1]*l < H and 0<= s_j+dy[1]*l<W:
                    if arr[s_i+dx[1]*l][s_j+dy[1]*l]== '#':
                        break
                    if arr[s_i+dx[1]*l][s_j+dy[1]*l]== '*':
                        arr[s_i+dx[1]*l][s_j+dy[1]*l] = '.'
                        break
                if arr[s_i][s_j] == '^' and 0<= s_i+dx[2]*l<H and 0<= s_j+dy[2]*l<W :
                    if arr[s_i+dx[2]*l][s_j+dy[2]*l]== '#':
                        break
                    if arr[s_i+dx[2]*l][s_j+dy[2]*l]== '*':
                        arr[s_i+dx[2]*l][s_j+dy[2]*l] = '.'
                        break
                if arr[s_i][s_j] == 'v' and 0<= s_i+dx[3]*l<H and 0<= s_j+dy[3]*l < W :
                    if arr[s_i+dx[3]*l][s_j+dy[3]*l]== '#':
                        break
                    if arr[s_i+dx[3]*l][s_j+dy[3]*l]== '*':
                        arr[s_i+dx[3]*l][s_j+dy[3]*l] = '.'
                        break
        if N_list[k] == 'U':
            arr[s_i][s_j] = '^'
            if 0 <= s_i+dx[2] < H and 0 <= s_j+dy[2] < W and arr[s_i+dx[2]][s_j+dy[2]]=='.':
                arr[s_i + dx[2]][s_j + dy[2]] = '^'
                arr[s_i][s_j] = '.'
                s_i += dx[2]
                s_j += dy[2]
        if N_list[k] == 'D':
            arr[s_i][s_j] = 'v'
            if 0<= s_i+dx[3]< H and 0<= s_j+dy[3]< W and arr[s_i + dx[3]][s_j + dy[3]] == '.':
                arr[s_i + dx[3]][s_j + dy[3]] = 'v'
                arr[s_i][s_j] = '.'
                s_i += dx[3]
                s_j += dy[3]
        if N_list[k] == 'L':
            arr[s_i][s_j] = '<'
            if 0<= s_i+dx[0]<H and 0<= s_j+dy[0]<W and arr[s_i + dx[0]][s_j + dy[0]] == '.':
                arr[s_i + dx[0]][s_j + dy[0]] = '<'
                arr[s_i][s_j] = '.'
                s_i += dx[0]
                s_j += dy[0]
        if N_list[k] == 'R':
            arr[s_i][s_j] = '>'
            if 0<= s_i+dx[1]<H and 0<= s_j+dy[1]<W and arr[s_i + dx[1]][s_j + dy[1]] == '.':
                arr[s_i + dx[1]][s_j + dy[1]] = '>'
                arr[s_i][s_j] = '.'
                s_i += dx[1]
                s_j += dy[1]
    print(f'#{tc}', end=' ')
    for i in range(H):
        print(''.join(arr[i]))