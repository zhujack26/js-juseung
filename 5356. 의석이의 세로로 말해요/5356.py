T = int(input())
for tc in range(1, T+1):
    arr = [list(map(str, input())) for _ in range(5)]
    result = ''
    # 인덱스 사용방식, 전체(공란포함) 구하고 나중에 빼기, zip 함수 사용 방식
    max_len = 0
    for i in range(5):
        if max_len < len(arr[i]):
            max_len = len(arr[i])
    for j in range(1, max_len+1):
        for k in range(5):
            if j <= len(arr[k]):
                result += arr[k][j-1]
            else:
                continue
    print(f'#{tc}', end=' ')
    for i in range(len(result)):
        print(result[i], end = '')
    print()

