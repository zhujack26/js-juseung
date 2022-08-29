T = int(input())
for t in range(T):
    N, K_min, K_max = map(int, input().split())
    lst = list(map(int, input().split()))
    ans = 10000
    for j in range(min(lst), max(lst)+1):
        for k in range(min(lst), max(lst)+1):
            A, B, C = 0, 0, 0
            for i in range(N):
                if lst[i] < j:
                    A += 1
                elif j <= lst[i] < k:
                    B += 1
                else:
                    C += 1
            if min(A, B, C) < K_min or max(A, B, C) > K_max:
                continue
            else:
                ans = min(ans, max(A, B, C) - min(A, B, C))

    if ans == 10000 or max(A, B, C)*3 < N or min(A, B, C)*3 > N:
        print(f'#{t+1} -1')
    else:
        print(f'#{t+1} {ans}')

"""
5
5 1 4
3 5 5 4 5
6 2 6
5 3 3 5 5 1
7 1 6
3 3 5 2 5 1 2
8 1 7
3 1 1 2 2 5 3 5
10 1 6
4 4 2 4 5 2 5 3 5 5
"""