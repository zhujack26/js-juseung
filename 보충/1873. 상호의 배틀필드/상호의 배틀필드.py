for tc in range(1, int(input())+1):
    H, W = map(int, input().split())
    arr = [list(input()) for _ in range(H)]
    N = int(input())
    N_list = list(input())
    dx = [0, 0, -1, 1]    #좌우상하
    dy = [-1, 1, 0, 0]
    direction = ['<', '>', '^', 'v']
    for i in range(3):
        for j in range(5):
            for k in range(23) :  # N_list 순회
                for l in range(max(H, W)):
                    if N_list[k] == 'S':
                        if arr[i][j] == '<' and 0<= i+dx[0]*l<H and 0<= j+dy[0]*l < W and arr[i+dx[0]*l][j+dy[0]*l]== '#':
                            break
                        if arr[i][j] == '>' and 0<= i+dx[1]*l<H and 0<= j+dy[1]*l < W and arr[i+dx[1]*l][j+dy[1]*l]== '#':
                            break
                        if arr[i][j] == '^' and 0<= i+dx[2]*l<H and 0<= j+dy[2]*l < W and arr[i+dx[2]*l][j+dy[2]*l]== '#':
                            break
                        if arr[i][j] == 'v' and 0<= i+dx[3]*l<H and 0<= j+dy[3]*l < W and arr[i+dx[3]*l][j+dy[3]*l]== '#':
                            break
                        if arr[i][j] == '<' and 0<= i+dx[0]*l<H and 0<= j+dy[0]*l < W and arr[i+dx[0]*l][j+dy[0]*l]== '*':
                            arr[i+dx[0]*l][j+dy[0]*l] = '.'
                            break
                        if arr[i][j] == '>' and 0<= i+dx[1]*l<H and 0<= j+dy[1]*l< W and arr[i+dx[1]*l][j+dy[1]*l]== '*':
                            arr[i+dx[1]*l][j+dy[1]*l] = '.'
                            break
                        if arr[i][j] == '^' and 0<= i+dx[2]*l<H and 0<= j+dy[2]*l< W and arr[i+dx[2]*l][j+dy[2]*l]== '*':
                            arr[i+dx[2]*l][j+dy[2]*l] = '.'
                            break
                        if arr[i][j] == 'v' and 0<= i+dx[3]*l<H and 0<= j+dy[3]*l< W and arr[i+dx[3]*l][j+dy[3]*l]== '*':
                            arr[i+dx[3]*l][j+dy[3]*l] = '.'
                            break

                    if N_list[k] == 'U':
                        for a in direction:
                            if arr[i][j]== a and arr[i+dx[2]][j+dy[2]]!='.' and 0<= i+dx[2]<H and 0<= j+dy[2]<W :
                                arr[i][j] = '^'
                                break
                            if 0<= i+dx[2]<H and 0<= j+dy[2]<W and arr[i+dx[2]][j+dy[2]]=='.':
                                arr[i][j] = '^'
                                i += dx[2]
                                j += dy[2]
                                break

                    if N_list[k] == 'D':
                        for a in direction:
                            if arr[i][j]== a and arr[i+dx[3]][j+dy[3]]!='.' and 0<= i+dx[3]<H and 0<= j+dy[3]<W :
                                arr[i][j] = 'v'
                                break
                            if 0<= i+dx[3]<H and 0<= j+dy[3]<W and arr[i+dx[3]][j+dy[3]]=='.':
                                arr[i+dx[3]][j+dy[3]] = 'v'
                                arr[i][j] = '.'
                                i = i + dx[3]
                                j = j + dy[3]
                                break

                    if N_list[k] == 'L':
                        for a in direction:
                            if arr[i][j]== a and arr[i+dx[0]][j+dy[0]]!='.' and 0<= i+dx[0]<H and 0<= j+dy[0]<W :
                                arr[i][j] = '<'
                                break
                            if 0<= i+dx[0]<H and 0<= j+dy[0]<W and arr[i+dx[0]][j+dy[0]]=='.':
                                arr[i+dx[0]][j+dy[0]] = '<'
                                arr[i][j] = '.'
                                i = i + dx[0]
                                j = j + dy[0]
                                break

                    if N_list[k] == 'R':
                        for a in direction:
                            if arr[i][j]== a and arr[i+dx[1]][j+dy[1]]!='.' and 0<= i+dx[1]<H and 0<= j+dy[1]<W :
                                arr[i][j] = '>'
                                break
                            if 0<= i+dx[1]<H and 0<= j+dy[1]<W and arr[i+dx[1]][j+dy[1]]=='.':
                                arr[i+dx[1]][j+dy[1]] = '>'
                                arr[i][j] = '.'
                                i = i + dx[1]
                                j = j + dy[1]
                                break

    print(f'#{arr}')