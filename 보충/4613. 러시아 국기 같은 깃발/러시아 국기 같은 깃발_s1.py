for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = [list(map(str, input().split())) for _ in range(N)]
    ans = []
    for i in range(1, N-1):
        for j in range(i+1, N):
            first = arr[0:i][:]
            two = arr[i:j][:]
            three = arr[j:N][:]

            cnt_first = (a.count('W') for a in first)
            cnt_two = (b.count('B') for b in two)
            cnt_three = (c.count('R') for c in three)

            result_first = len(first) * M - sum(cnt_first)
            result_two = len(two) * M - sum(cnt_two)
            result_three = len(three) * M - sum(cnt_three)

            ans.append(result_first + result_two + result_three)

        print(f'#{tc}', min(ans))

