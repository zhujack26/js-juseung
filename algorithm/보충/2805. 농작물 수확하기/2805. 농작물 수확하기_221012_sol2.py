for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    cnt = 0
    for i in range(N//2+1):
        for j in range((N//2-i),N-(N//2-i)):
            cnt += arr[i][j]
    for i in range(N//2+1, N):  # i= 4,5,6
        for j in range(i-(N//2), (N-i+(N//2))):
            cnt += arr[i][j]
    print(f'#{tc} {cnt}')