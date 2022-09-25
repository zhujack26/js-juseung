T = int(input())
for tc in range(T):
    N = int(input())  # 카드 장수 N
    ai = list(map(int, input()))
    count = [0] * 10
    for i in ai:
        count[i] += 1
        max_ai = 0

    for j in range(len(ai)):
        cnt = 0
        if ai[j] > max_ai:
            max_ai = ai[j]
        elif count[j] > cnt:
            cnt = count[j]

    print(f"#{tc + 1} {max_ai} {cnt}")




