t = int(input())
for tc in range(t):
    n = int(input())
    miro = [list(map(int, input())) for _ in range(n)]
    # print(miro)
    end = 0
    ans = 0

    for i in range(n):
        for j in range(n):
            if miro[i][j] == 3:
                end = (i, j)
    # print(end)
    visited = []
    Que = [end]

    while Que:
        (x, y) = Que.pop(0)
        if x+1 < n and miro[x+1][y] == 2:
            ans = 1
            break
        elif x+1 < n and miro[x+1][y] == 0 and (x+1, y) not in visited:
            visited.append((x+1, y))
            Que.append((x+1, y))

        if y+1 < n and miro[x][y+1] == 2:
            ans = 1
            break
        elif y+1 < n and miro[x][y+1] == 0 and (x, y+1) not in visited:
            visited.append((x, y+1))
            Que.append((x, y+1))

        if y-1 >= 0 and miro[x][y-1] == 2:
            ans = 1
            break
        elif y-1 >= 0 and miro[x][y-1] == 0 and (x, y-1) not in visited:
            visited.append((x, y-1))
            Que.append((x, y-1))

        if x-1 >= 0 and miro[x-1][y] == 2:
            ans = 1
            break
        elif x-1 >= 0 and miro[x-1][y] == 0 and (x-1, y) not in visited:
            visited.append((x-1, y))
            Que.append((x-1, y))


    print(f'#{tc+1} {ans}')