for tc in range(1, int(input())+1):
    N = int(input())
    arr = list(map(int, input().split()))
    result = []
    for i in range(1, N - 1):
        for j in range(i + 1, N):
            cnt = []
            cnt.append(sum(arr[0:i]))
            cnt.append(sum(arr[i:j]))
            cnt.append(sum(arr[j:N]))
            result.append(max(cnt) - min(cnt))
    print(f'#{tc}', min(result))
