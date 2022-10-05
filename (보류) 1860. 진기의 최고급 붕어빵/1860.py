T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    times = list(map(int, input().split()))
    times.sort()
      #사람들이 온 시간 정렬
# N명의 사람, M초의 시간을 들여, K개의 붕어빵
#M*K  M초 시점에서 붕어빵 갯수
    for i in range(M, sorted(time)[N-1]+1, M):
        board[i]+K
    for i in range(N):
        if sorted(time)[i] >= M:



