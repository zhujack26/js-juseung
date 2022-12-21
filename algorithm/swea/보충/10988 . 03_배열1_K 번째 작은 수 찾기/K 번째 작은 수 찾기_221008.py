for tc in range(1, int(input())+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    # 방법1 : 그냥 sorted 함수와 set으로 간단히 풀기
    # print(f'#{tc}', list(set(sorted(arr)))[K-1])

    # 방법2 : 카운팅 정렬
    board = [0] * 1000 # 정수의 범위가 1~1000인데 인덱스 맞추기 위해 1001개 생성
    result = 0
    for i in arr:
        board[i] += 1
    for i in range(1000):
        if board[i] != 0:
            K -= 1  # 0이 아닐때 K의 값을 하나씩 빼주면 K번째 수를 구할 수 있다.
            if K == 0 :
                result = i
    print(f'#{tc} {result}')