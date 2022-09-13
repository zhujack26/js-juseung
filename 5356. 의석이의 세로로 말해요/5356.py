T = int(input())
for tc in range(1, T+1):
    arr = [list(map(str, input().split())) for _ in range(5)]
    max_arr = 0
    result = []
    for i in range(5):
        if len(*arr[i]) > max_arr:
            max_arr = len(*arr[i])
        for j in range(max_arr):
            result.append(arr[j][i])
            print(result)

