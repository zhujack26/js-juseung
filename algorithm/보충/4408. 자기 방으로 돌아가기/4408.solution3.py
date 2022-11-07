for tc in range(1, int(input())+1):
    N = int(input())
    board = [0]* 401
    for i in range(N):
        now, back = map(int, input().split())
        if now > back:
            now, back = back, now
        if back % 2 == 1:
            for j in range(now, back+2):
                board[j] += 1
        elif back % 2 == 0:
            for j in range(now, back+1):
                board[j] += 1
    print(f'#{tc}', max(board))