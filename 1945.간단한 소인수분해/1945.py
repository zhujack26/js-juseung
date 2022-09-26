T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    answer = [0, 0, 0, 0, 0]
    while n >= 2:   # n이 2이상일때 계속 돈다
        if n % 11 == 0:
            n = n // 11
            answer[4] += 1
        elif n % 7 == 0:
            n = n // 7
            answer[3] += 1
        elif n % 5 == 0:
            n = n // 5
            answer[2] += 1
        elif n % 3 == 0:
            n = n // 3
            answer[1] += 1
        elif n % 2 == 0:
            n = n // 2
            answer[0] += 1

    print(f'#{tc}', *answer)