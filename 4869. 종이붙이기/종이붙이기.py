for tc in range(1, int(input())+1):
    N = int(input())
    N_10 = N//10   # 40
    arr = [0, 1, 1, 3]
    if N == 10:
        result = 1
    elif N == 20:
        result = 3
    elif N >= 30:
        for i in range(3, N_10+1):
            arr.append(arr[i-1] + arr[i-1] + arr[i])
            result = arr[-1]
    print(f'#{tc} {result}')
    # arr[1]+ arr[1] + arr[2] = arr[3]
    # arr[2]+ arr[2] + arr[3] = arr[4]
    # arr[3]+ arr[3] + arr[4] = arr[5]