# import sys
# sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    bus = [0] * 1001
    # 카운팅 정렬 활용
    # 1~1000개라서 처음에 1000으로 했다가,
    # arr[i][2]가 1000까지 나와 밑에 bus[변수]를 위해 1001개가 필요
    for i in range(N):
        if arr[i][0] == 1:
            for j in range(arr[i][1], arr[i][2] + 1):  # range이기 때문에 뒤에 +1
                bus[j] += 1
        elif arr[i][0] == 2:
            for k in range(arr[i][1], arr[i][2] + 1, 2):
                bus[k] += 1
        elif arr[i][0] == 3:
            for l in range(arr[i][1], arr[i][2] + 1):
                if arr[i][1] % 2 == 0 and l % 4 == 0:
                    bus[l] += 1
                elif arr[i][1] % 2 == 1 and l % 3 == 0 and l % 10 != 0:
                    bus[l] += 1

    print(f'#{tc} {max(bus)}')