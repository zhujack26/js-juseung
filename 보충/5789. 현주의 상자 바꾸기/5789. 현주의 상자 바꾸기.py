for tc in range(1, int(input())+1):
    N, Q = map(int, input().split())
    counting = [0] * N
    for i in range(1, Q+1):
        L, R = map(int, input().split())
        for j in range(L, R+1):
            counting[j-1] = i  #여기서 괜히 replace 같은거 안써도 됨.
    print(f'#{tc}', *counting)  # 여기{} 앞에는 asterisk 안됨.

