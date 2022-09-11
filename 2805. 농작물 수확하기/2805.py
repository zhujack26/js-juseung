T = int(input())
for tc in range(1, T+1):
    # 가장 수익 구간이 큰 곳부터 구한다음 위 아래로 1칸씩 줄여나가기
    # 규칙찾기 N = 3 일때 [1],  5일 때 [2]  7일때 [3] 9일때 [4]
    # 가장 큰 구간의 위치는 [1] 씩 늘어난다.
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    # N//2 이 가장 큰 구간의 행 위치
    # arr[0][2]+ arr[1][1]+arr[1][2]+arr[1][3]+ arr[2][0]~[2][4]+ arr[3][1]~[3][3]+ arr[4][2]
    # arr[0][3]+arr[1][2]+arr[1][3]+ arr[1][4]+ arr[2][1]~[2][5]+arr[3][0]~[3][6]+ arr[4][1]~[4][5] [5][2]~[5][4]
    result = 0
    result_1 = 0
    result_2 = 0
    for i in range(0, N//2):
        for j in range(N//2-i, i+N//2+1):
            result = result + arr[i][j]
    for i in range(N):
        result_1 = result_1 + arr[N//2][i]
    for i in range(N//2+1, N):
        for j in range(i-N//2, N-(i-N//2)):
            result_2 = result_2 + arr[i][j]

    print(f"#{tc}", result+result_1+result_2)


