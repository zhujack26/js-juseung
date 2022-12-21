
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    matrix = [list(map(str, input().split())) for _ in range(N)]
    zipped_matrix = list(map(list, zip(*matrix)))

    matrix90 = [i[::-1] for i in zipped_matrix]
    # print(matrix90)
    matrix180 = [i[::-1] for i in matrix[::-1]]
    # print(matrix180)
    matrix270 = zipped_matrix[::-1]
    # print(matrix270)

