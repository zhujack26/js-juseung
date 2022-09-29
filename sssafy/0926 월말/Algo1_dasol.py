# 봉우리으 개수를 구하는 문제
# 높은데서 낮은 지형을 만나면 봉우리 하나를 카운트한다.

t = int(input())
for tc in range(t):
    N = int(input())
    arr = list(map(int, input().split()))
    # print(N, arr)
    # N은 지형의 수, arr은 지형의 높이
    # cnt = 0     # 지형 수를 세는 변수
    #
    # if N == 1:  # 만약 지형이 1개일 경우 1개를 카운트
    #     cnt = 1
    #
    # elif N > 1: # 지형이 2개 이상일 때부터 계산
    #
    #     if len(set(arr)) == 1:  # 만약 지형의 높이가 전부 같을 경우 처리
    #         cnt += 1
    #
    #     else:  # 지형의 높이가 다를 경우
    #         for i in range(len(arr)):
    #
    #             if i == 0:   # 첫 번째 지형
    #                 if arr[i] > arr[i+1]:
    #                     cnt += 1
    #             elif i > 0 and i <= len(arr)-2:  # 가운데 지형
    #                 if arr[i-1] < arr[i] and arr[i] >= arr[i+1]:
    #                     cnt += 1
    #             elif i == len(arr)-1:   # 마지막 지형
    #                 if arr[i] > arr[i-1]:
    #                     cnt += 1
    #
    # print(f'#{tc+1} {cnt}')

    new_arr = []
    for i in range(len(arr)-1):
        if arr[i] != arr[i+1]:
            new_arr.append(arr[i])
    new_arr.append(arr[-1])

    cnt = 0     # 지형 수를 세는 변수

    if N == 1:  # 만약 지형이 1개일 경우 1개를 카운트
        cnt = 1

    elif N > 1: # 지형이 2개 이상일 때부터 계산

        if len(set(new_arr)) == 1:  # 만약 지형의 높이가 전부 같을 경우 처리
            cnt += 1

        else:  # 지형의 높이가 다를 경우
            for i in range(len(new_arr)):

                if i == 0:   # 첫 번째 지형
                    if new_arr[i] > new_arr[i+1]:
                        cnt += 1
                elif i > 0 and i <= len(new_arr)-2:  # 가운데 지형
                    if new_arr[i-1] < new_arr[i] and new_arr[i] >= new_arr[i+1]:
                        cnt += 1
                elif i == len(new_arr)-1:   # 마지막 지형
                    if new_arr[i] > new_arr[i-1]:
                        cnt += 1
    print(f'#{tc+1} {cnt}')



