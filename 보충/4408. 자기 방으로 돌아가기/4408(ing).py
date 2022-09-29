for tc in range(1, int(input())+1):
    N = int(input())
    board = [0]* 401
    list = []
    for i in range(N):
        now, back = map(int, input().split())
        for j in range(now-1, back):
            board[j] += 1
        if i in board:
            list.append(i)
    print(max(list))