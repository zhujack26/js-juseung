#완전탐색으로 모든 경로를 검색해서 구하는 것은 시간초과 발생
#왼쪽 혹은 위쪽의 값 중 큰 값을 현재 위치의 값과 더해서 현재 위치에 저장
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
# 1행 누적
for i in range(1, M):
    arr[0][i] += arr[0][i-1]

# 1열 누적
for i in range(1, N):
    arr[i][0] += arr[i-1][0]

# 좌측, 상단 값 비교해 누적
for i in range(1, N):
    for j in range(1, M):
        if arr[i-1][j] > arr[i][j-1]:
            arr[i][j] += arr[i-1][j]
        else:
            arr[i][j] += arr[i][j-1]
# 가장 마지막 값 출력
print(arr[-1][-1])