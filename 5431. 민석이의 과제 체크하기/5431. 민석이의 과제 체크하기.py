for tc in range(1, int(input())+1):
    N, K = map(int, input().split())
    arr = []
    problem = map(int, input().split())
    for i in range(1, N+1):
        arr.append(i)
    for i in problem:
        arr.remove(i)
    print(f'#{tc}', *arr)