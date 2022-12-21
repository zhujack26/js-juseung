for tc in range(1, int(input())+1):
    N, M, K = map(int, input().split())  # N명의 손님, M초의 시간을 들여, K개의 붕어빵
    guest_time = list(map(int, input().split()))
    guest_time.sort() #사람들이 온 시간 정렬
    cokie = 0
    ans = 'Possible'
    for t in range(0, 11112): # 시간을 순회(처음에 0을 빼고 했다가 테스트 케이스 1000/993개..)
        if t != 0 and t % M ==0 : # 현재 시간이 0이 아니고(M이 1부터이므로) M의 배수일때 쿠키 생성
            cokie += K
        for i in range(N):
            if t == guest_time[i]:  #손님 오는 시간과 현재시간이 같을 때 쿠키 냠냠
                cokie -= 1
        if cokie < 0 :  # 쿠키가 -1이 되는 순간 종료
            ans = 'Impossible'
            break
    print(f'#{tc} {ans}')

'''
@@@ 시간 초과 코드 @@@
for tc in range(1, int(input())+1):
    N, M, K = map(int, input().split())
    # N명의 사람, M초의 시간을 들여, K개의 붕어빵
    times = list(map(int, input().split()))
    times.sort() #사람들이 온 시간 정렬
    A = max(times)
    board = [0] *(A+1)
    ans = 'possible'
    for i in range(M, A+1, M):
        for j in range(i, A+1):
            board[j] += K
    for i in times:
        for j in range(i, A+1):
            board[j] -= 1
    for i in board:
        if i < 0:
            ans = 'impossible'
            break
    print(f'#{tc} {ans}')


@@@정답 코드 @@@
for tc in range(1, int(input()) + 1):
    N, M, K = map(int, input().split())         # 손님수, 생성시간, 개수
    times = list(map(int, input().split()))     # 정렬된 상태가 아님
    times.sort()
    total = 0                               # 붕어빵의 현재 개수
    ans = 'Possible'
    for i in range(N):
        if (times[i]//M)*K  < i + 1:        # 시간 t에 가능한 붕어빵수  (t // M) * K
            ans = 'Impossible'
            break
    print(f'#{tc} {ans}')



for tc in range(1, int(input()) + 1):
    N, M, K = map(int, input().split())
    times = list(map(int, input().split()))
    times.sort()
    total = 0
    ans = 'Possible'
    for t in range(0, 11111 + 1):
        if t != 0 and t % M == 0:
            total += K
        if t in times:
            if total <= 0:
                ans = 'Impossible'
                break
            else:
                total -= 1
    print(f'#{tc} {ans}')
'''






