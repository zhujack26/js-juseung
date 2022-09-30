for tc in range(1, int(input())+1):
    N = int(input())
    board = [0]* 401
    lst = []
    count = []
    for i in range(N):
        now, back = map(int, input().split())
        for j in range(now-1, back):
            board[j] += 1
    for i in range(400):
        if board[i] != board[i+1] :
            lst.append(board[i])
    # for i in lst:
    #     if i != 1 and i != 0:
    #         count.append(i)
    print(lst)
    # print(f'#{tc}', len(count)+1)

    #
    # print(f'#{tc} {max(board)}')
    # print(len(board))