# di = [0, 1, 0, -1]
# dj = [1, 0, -1, 0]
# N = 3
# M = 4
# arr = [[1, 2, 3, 4], [4, 5, 6, 8]]
# for i in range(N):
#     for j in range(M):
#         for k in range(4):
#             ni = i + di[k]
#             nj = j + dj[k]
#             if 0 <= ni <N and 0<=nj<M:
#                 print(ni, nj)

# for i in range(N):
#     for j in range(M):
#         for di, dj in [[0,1], [1,0], [0,-1], [-1,0]]:
#             ni, nj = i + di, j +dj
#             if 0 <= ni < N and 0 <= nj < M:
#                 print(ni, nj)

# numbers = (1, 2, 3, 4, 5)
#
# print(*numbers)

# matrix = [[1, 8, 4],
#           [7, 3, 9],
#           [5, 2, 6]]

# for r in range(3):
#     for c in range(3):
#         if r > c:
#             matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
# for i in range(3): # 그냥 매트릭스 형태로 보고 싶어서 출력 형식 조정
#     print(matrix[i])
#
# cards = [1, 3, 2, 5 ,8 ,0, 7 ,5 ,2 ,4 ,8, 4 ,7 ,5 ,2 ,3 ,5, 4, 7, 9]
#
# card_counts = [0]*10
#
# for num in cards:
#     card_counts[num] += 1
#
# print(card_counts)

# import sys
# sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):

    cards = list(map(int, input().split()))

    count_dict = dict()  # .get 으로 없는걸 부를땐 None 을 반환합니다.

    for num in cards:
        if not count_dict.get(num): # get 은 키값이 없어도 오류가 나지 않습니다.
            count_dict[num] = 1 # 없는 경우는 1을 최초로 넣어줍니다.
        else: # 있는 경우는
            count_dict[num] += 1  # 1을 더해줍니다.

    for i in count_dict:
        # print(i)
    # for i in range(len(count_dict)):
        if count_dict[i] % 2 == 1:
            print(i)
