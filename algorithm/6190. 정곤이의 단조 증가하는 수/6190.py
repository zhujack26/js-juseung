for tc in range(1, int(input())+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = []
    ans = -1
    ans_number = []
    ans_max = 0
    arr.sort()
    for i in range(N-1):
        for j in range(1, N):
            if i+j < N:
                cnt.append(arr[i] * arr[i+j])
    for k in range(len(cnt)):  # 10 20 26 50 65 130
        for l in range(len(str(cnt[k]))-1): # 130 일 때 j 0,1
            if str(cnt[k])[l] > str(cnt[k])[l+1]:
                cnt.remove(cnt[k])
    print(f'#{tc} {cnt}')