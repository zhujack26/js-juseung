for tc in range(1, int(input())+1):
    N = int(input())
    arr = [0]*5001
    for i in range(N):
        A, B = map(int, input().split())
        for j in range(A, B+1):  # range(1,4) j = 1,2,3
            arr[j] = arr[j] + 1
    P = int(input())
    list = []
    for i in range(P):
        list.append(arr[int(input())])
    print(f'#{tc}', *list)
