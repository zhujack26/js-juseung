result = []
for tc in range(int(input())):
    N, M = map(int, input().split())
    visit = []
    compare = []
    count = 0
    for i in range(1, N+1):
        compare.append(i)
    for i in range(M):
        count += 1
        a, b = map(int, input().split())
        visit.append(a)
        visit.append(b)
        if sum(set(visit)) == sum(compare) and count != M:
            result.append(count)
        elif sum(set(visit)) == sum(compare) and count == M and result == []:
            result.append(count)
print(result)
