# T = int(input())
# for tc in range(1, T+1):
#     N, K = map(int, input().split())
#     arr = set(map(int, input().split()))
#     change = list(arr)
#     print(f'#{tc} {change[K-1]}')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    counting = [0] * (N+1)
    for i in arr:
        counting[i] += 1
    result = 0
    for i in range(len(counting)):
        if counting[i] != 0:
            result += 1
            if result == K:
                print(f'#{tc} {i}')