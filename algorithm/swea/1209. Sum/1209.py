import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    arr_max = 0
    check_3 = 0
    for i in range(100):
        if sum(arr[i]) > arr_max:
            arr_max = sum(arr[i])
        check = 0
        for j in range(100):  # 각 열의 합
            check += arr[j][i]  #check  = check + arr[j][i]
            if check > arr_max:
                arr_max = check
            check_2 = 0
            if i==j:
                check_2 += arr[i][j]
                if check_2 > arr_max:
                    arr_max = check_2
        check_3 += arr[i][99-i]
        if check_3 > arr_max:
            arr_max = check_3

    print(f"#{tc} {arr_max}")

