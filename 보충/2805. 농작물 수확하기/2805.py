for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    result, result_1 = 0, 0
    for i in range(0, N//2+1): # 0 , 1, 2
        for j in range(N//2-i, i+N//2+1):
            result += arr[i][j]
    for i in range(N//2+1, N):
        for j in range(i-N//2, N-(i-N//2)):
            result_1 += arr[i][j]
    print(f"#{tc}", result+result_1)


