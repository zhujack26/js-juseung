import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())

# 단위가 50000원, 10000원, 5000원, 1000원, 500원, 100원, 50원, 10원 구간 별로
# 최소 갯수의 당락을 좌우하므로 각 단위들로 N을 나누어 본다.
# 예시) 50000원으로 32850을 나눌 수 있나?(나눴을 때 몫이 있나?)-> No
# 10000원으로 나눌 수 있나? -> YES -> 몫 3  32850//10000 = 3
# 32850 % 10000 로 구한 나머지 2850을 5000원으로 나눌 수 있나? -> No
# 32850 % 10000 로 구한 나머지 2850을 1000원으로 나눌 수 있나? -> YES -> 몫 2
# 이런식으로 진행

    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    count = [0, 0, 0, 0, 0, 0, 0, 0]

    for i in range(0, 8):
        if N // money[i] != 0 :   # True& False
            count[i] = N // money[i]  # 몫이 최솟값이므로 count 리스트에 저장
            N = N % money[i]  # 돈은 나머지로 변한다

        # elif N // money[i] == 0:  #
        #     pass & continue

    print(f'#{tc}')
    print(*count)