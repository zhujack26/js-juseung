import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # 남은 값 중 가장 가까운 인덱스의 값이 크지 않을 경우(if 사용)
    # 매매가가 가장 큰 날을 기준으로 이전에는 다 사고, 큰 날에 팔아버린다. (1)
    # 다 팔고 나서 다시 나머지 일자를 대상으로 (1) 반복
    number = list(map(int, input().split()))
    sum = 0  # 매매 저장할 값
    idx = 0
    while number :
        if number[0] != max(number) :
            idx = number.index(max(number))
            for i in range(idx):
                sum -= number[i] #(1) 과정
            sum = sum + idx * max(number)
            del number[0:idx+1]
        elif number[0] == max(number):
            del number[0]
    print(f"#{tc} {sum}")



#다른 풀이법
# T = int(input())
# for t in range(1, T + 1):
#     N = int(input())
#     prices = list(map(int, input().split()))
#
#     profit = 0
#     max_prices = 0
#     for i in range(N - 1, -1, -1):
#         if prices[i] > max_prices:
#             max_prices = prices[i]
#         else:
#             profit += max_prices - prices[i]
#
#     print(f'#{t} {profit}')