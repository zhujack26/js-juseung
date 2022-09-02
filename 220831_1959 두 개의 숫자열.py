T = int(input())
for tc in range(1, T+1):
    N , M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    #for 문을 돌릴 i 값은
    # ex) N, M이 2, 3 일 경우 2가지, 3, 5일 경우 4가지

    result = 0
    for i in range(abs(N-M)+1):   # N M 어떤게 더 클지 모르니 절댓값을 씌워준다
        value = 0
        for j in range(min(N, M)):
            if N < M :
                value += A[j+i] * B[j]
            elif N > M :
                value += A[j] * B[j+i]
            elif N == M :
                value += A[j] * B[j]

        if value > result :
            result = value

    print(f'#{tc} {result}')

