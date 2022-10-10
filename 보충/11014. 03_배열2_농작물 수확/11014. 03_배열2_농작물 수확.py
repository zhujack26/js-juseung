for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = []
    for i in range(N-1):
        for j in range(N-1):
            print(arr[0:i][0:j])

            # cnt.append(arr[0:i][0:j]) # 1번 농지
            # cnt.append(arr[i:N][0:j]) # 2번 농지
            # cnt.append(arr[:][j:N]) # 3번 농지
            # print(cnt)
            # result.append(max(cnt)-min(cnt))
    # print(f'#{tc}', min(result))