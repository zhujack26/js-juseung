def inorder(n):
    if n <= N:
        inorder(2*n)
        nodenumber.append(n)
        inorder(2*n+1)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nodenumber = [[0]]  # 0 4 2 5 1 6 3
    number = [[0]]  # 0 1 2 3 4 5 6
    for i in range(1, N+1):
        number.append(i)
    inorder(1)
    root = number[nodenumber.index(1)]
    result = number[nodenumber.index(N//2)]
    # print(nodenumber)
    print(f'#{tc} {root} {result}')
