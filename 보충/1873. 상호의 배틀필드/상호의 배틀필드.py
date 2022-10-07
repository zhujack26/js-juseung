for tc in range(1, int(input())+1):
    H, W = map(int, input().split())
    arr = [list(input()) for _ in range(H)]
    N = int(input())
    N_list = list(input())
    dx = [0, 0, -1, 1]    #좌우상하
    dy = [-1, 1, 0, 0]
    direction = ['<', '>', '^', 'v']
    for i in range(H):
        for j in range(W):
            if arr[i][j] == '<' or arr[i][j] == '>' or arr[i][j] == '^' or arr[i][j] =='v':
                for k in range(N) :  # N_list 순회
                    if N_list[k] == 'S':
                        for l in range(max(H, W)):
                            if arr[i][j] == '<' and 0<= i+dx[0]*l< H and 0<= j+dy[0]*l < W:
                                if arr[i+dx[0]*l][j+dy[0]*l] == '#':
                                    break
                                if arr[i+dx[0]*l][j+dy[0]*l] == '*':
                                    arr[i+dx[0]*l][j+dy[0]*l] = '.'
                                    break

                            if arr[i][j] == '>' and 0<= i+dx[1]*l < H and 0<= j+dy[1]*l < W:
                                if arr[i+dx[1]*l][j+dy[1]*l]== '#':
                                    break
                                if arr[i+dx[1]*l][j+dy[1]*l]== '*':
                                    arr[i+dx[1]*l][j+dy[1]*l] = '.'
                                    break

                            if arr[i][j] == '^' and 0<= i+dx[2]*l<H and 0<= j+dy[2]*l < W :
                                if arr[i+dx[2]*l][j+dy[2]*l]== '#':
                                    break
                                if arr[i+dx[2]*l][j+dy[2]*l]== '*':
                                    arr[i+dx[2]*l][j+dy[2]*l] = '.'
                                    break

                            if arr[i][j] == 'v' and 0<= i+dx[3]*l<H and 0<= j+dy[3]*l < W :
                                if arr[i+dx[3]*l][j+dy[3]*l]== '#':
                                    break
                                if arr[i+dx[3]*l][j+dy[3]*l]== '*':
                                    arr[i+dx[3]*l][j+dy[3]*l] = '.'
                                    break

                    if N_list[k] == 'U':
                        if 0 <= i+dx[2] < H and 0 <= j+dy[2] < W :
                            if arr[i + dx[2]][j + dy[2]] != '.' :
                                arr[i][j] = '^'
                            if arr[i+dx[2]][j+dy[2]]=='.':
                                arr[i][j] = '.'
                                arr[i + dx[2]][j + dy[2]] ='^'
                                i += dx[2]
                                j += dy[2]


                    if N_list[k] == 'D':
                        if  0<= i+dx[3]<H and 0<= j+dy[3]<W :
                            if arr[i + dx[3]][j + dy[3]] != '.' :
                                arr[i][j] = 'v'
                            if arr[i + dx[3]][j + dy[3]] == '.':
                                arr[i][j] = '.'
                                arr[i + dx[3]][j + dy[3]] = 'v'
                                i += dx[3]
                                j += dy[3]


                    if N_list[k] == 'L':
                        if 0<= i+dx[0]<H and 0<= j+dy[0]<W :
                            if arr[i + dx[0]][j + dy[0]] != '.':
                                arr[i][j] = '<'
                            if arr[i + dx[0]][j + dy[0]] == '.':
                                arr[i][j] = '.'
                                arr[i + dx[0]][j + dy[0]] = '<'
                                i += dx[0]
                                j += dy[0]

                    if N_list[k] == 'R':
                        if 0<= i+dx[1]<H and 0<= j+dy[1]<W :
                            if arr[i + dx[1]][j + dy[1]] != '.' :
                                arr[i][j] = '>'
                            if arr[i + dx[1]][j + dy[1]] == '.':
                                arr[i][j] = '.'
                                arr[i + dx[1]][j + dy[1]] = '>'
                                i += dx[1]
                                j += dy[1]

                print(f'#{tc}')
                for o in range(H):
                    print(''.join(arr[o]))