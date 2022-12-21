# import sys
# sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(str, input().split())) for _ in range(N)]

    # 가로행 리스트 중에 k자리가 있을 경우,
    result = []
    for i in range(N):
        for j in range(N):
            result.append(arr[i][j])
            count = 0
            if (*K) in result :
                count = count + 1
    print(count)
    # 여기까지 했는데 이 방법으로는 더 이상 못풀었습니다..

