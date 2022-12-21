import sys
for tc in range(int(sys.stdin.readline())):
    N, M = map(int, sys.stdin.readline().split())
    visit = []
    compare = []
    count = 0
    for i in range(1, N+1):
        compare.append(i)
    for i in range(M):
        count += 1
        a, b = map(int, sys.stdin.readline().split())
        if a not in visit :
            visit.append(a)
        if b not in visit :
            visit.append(b)
        if sum(visit) == sum(compare) and count != M :
            print(count)
            for j in range(M-count):
                c, d = map(int, sys.stdin.readline().split())
            break
        if sum(visit) == sum(compare) and count == M:
            print(count)


# 정답 코드
# import sys
# for _ in range(int(sys.stdin.readline())):
#     N, M = map(int, sys.stdin.readline().split())
#     for _ in range(M):
#         a, b = map(int, sys.stdin.readline().split())
#     print(N - 1)