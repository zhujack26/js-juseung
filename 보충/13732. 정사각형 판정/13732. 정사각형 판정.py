# for tc in range(1, int(input())+1):
#     N = int(input())
#     arr = [list(input()) for _ in range(N)]
#     dx = [0, 1, 0, -1]
#     dy = [1, 0, -1, 0]
#     cnt = 0
#     ans ='no'
#     for i in range(N):
#         for j in range(N):
#             x, y = i, j
#             arr[x][y] = 1
#             for p in range(1, p):
#                 if 0<= x+dx[0]*p <N and 0<= y+dy[0]*p < N and arr[x][y] == '#'and arr[x+dx[0]*p][y+dy[0]*p]=='#':
#                     x = x+dx[0]*p
#                     y = y+dy[0]*p
#                     arr[x][y] = 1
#                     if 0<= x+dx[1]*p <N and 0<= y+dy[1]*p < N and arr[x][y] == '#'and arr[x+dx[1]*p][y+dy[1]*p]=='#':
#                         x = x + dx[1] * p
#                         y = y + dy[1] * p
#                         arr[x][y] = 1
#                         if 0<= x+dx[2]*p <N and 0<= y+dy[2]*p < N and arr[x][y] == '#'and arr[x+dx[2]*p][y+dy[2]*p]=='#':
#                             x = x + dx[2] * p
#                             y = y + dy[2] * p
#                             arr[x][y] = 1
#                             if 0<= x+dx[3]*p <N and 0<= y+dy[3]*p < N and arr[x][y] == '#'and arr[x+dx[3]*p][y+dy[3]*p]=='#':
#                                 x = x + dx[3] * p
#                                 y = y + dy[3] * p
#     if cnt == 1:
#         ans = 'yes'
#     print(f'#{tc} {ans}')

# for tc in range(1, int(input())+1):
#     N = int(input())
#     arr = [list(input()) for _ in range(N)]
#     cnt = 0
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] == '#' and arr[i][j+1] !='#' and arr[i+1][j] !='#' and arr[i+1][j+1] !='#':
#                 cnt += 1
#                 if arr[i][j+1] !='#' and arr[i+1][j] == '#' :
#                     cnt -= 1
#                 if arr[i+1][j] == '#' and arr[i][j+1] != '#':
#                     cnt -= 1

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    ans = ''
    aa = []
    for i in range(1, N+1):
        aa.append(i*i)
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] =='#':
                cnt += 1
    for i in range(N):
        for j in range(N):
            if cnt == 1:
                ans = 'yes'
            if cnt in aa and cnt != 1:
                num = int(cnt**(1/2))
                for n in range(1, num+1):
                    if 0<= i+n <N and 0<= j+n <N and arr[i][j] == '#':
                        if arr[i][j] != arr[i][j+n] or arr[i][j] != arr[i+n][j]:
                            ans ='no'
                            break
                    if 0 <= i + n < N and 0 <= j + n < N and arr[i][j] == '#':
                        if arr[i][j] == arr[i][j + n] and arr[i][j] == arr[i + n][j]:
                            ans ='yes'
            if not cnt in aa:
                ans = 'no'
    print(f'#{tc} {ans}')

