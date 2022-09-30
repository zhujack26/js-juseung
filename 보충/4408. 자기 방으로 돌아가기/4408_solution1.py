for tc in range(1, int(input())+1):
    N = int(input())
    arr = [0] * 200 # 복도리스트
    for i in range(N):
        now, back = map(int, input().split())
        if now > back:
            now, back = back, now
        for i in range((now+1)//2, (back+1)//2+1):
            arr[i-1] += 1
    print(f'#{tc}', max(arr))