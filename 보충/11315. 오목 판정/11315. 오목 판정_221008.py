for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    dx = [1, 1, -1, -1, 0, 0, 1, -1]
    dy = [1, -1, 1, -1, -1, 1, 0, 0]
    ans = 'NO'
    for i in range(N):
        for j in range(N):
            for d in range(8):
                cnt = []
                # cnt = 0
                for p in range(5):
                    if 0<= i+dx[d]*p <N and 0<= j+dy[d]*p <N and arr[i+dx[d]*p][j+dy[d]*p] == 'o':
                        # cnt += 1
                        cnt.append(arr[i+dx[d]*p][j+dy[d]*p])
                if 'ooooo' == ''.join(cnt):
                    ans = 'YES'
                # if cnt == 5:  #cnt는 최대 5인데 >= == 차이 떄문에 pass 된다는게 이해가 안된다.
                #     ans = 'YES'
                #     break
    print(f'#{tc} {ans}')