T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    arr = list(map(int, input().split()))
    board = [0]*100
# N명의 사람, M초의 시간을 들여, K개의 붕어빵
#M*K  M초 시점에서 붕어빵 갯수
    for i in range(N):
        if arr[i] >= M: 



