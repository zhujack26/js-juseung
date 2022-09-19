T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    Number = list(map(int, input().split()))  # 변수할당

    # N = 10, M=3 때 비교할 집합이 8개
    # N = 20, M 19 때 비교할 집합이 2개
    # 비교할 집합의 개수 공식 & for 문 in에 넣을 값 : N-M+1

    max_Number = 0
    min_Number = 999999999999

    for i in range(N - M + 1):  # ex i= 0,1
        if sum(Number[i:i + M]) < min_Number:  # if - elif가 아닌 if-if 독립 조건으로 최댓값 최솟값을 구한다.
            min_Number = sum(Number[i:i + M])
        if sum(Number[i:i + M]) > max_Number:
            max_Number = sum(Number[i:i + M])

    print(f"#{tc} {max_Number - min_Number}")