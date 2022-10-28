for tc in range(1, int(input())+1):
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    day = 0
    count_1 = 0
    count_2 = 0
    for i in range(1, N): # 4개 나무면 처음 가장 큰 거 빼고 3개
        if (max(arr)-arr[i]) % 3 == 0:
            day += (max(arr)-arr[i])//3*2
        if (max(arr)-arr[i]) % 3 == 1:
            day += (max(arr)-arr[i])//3*2
            count_1 += 1
        if (max(arr)-arr[i]) % 3 == 2:
            day += (max(arr)-arr[i])//3*2
            count_2 += 1
    if count_1 == count_2:
        day += count_1+count_2
    if count_1 > count_2:  #7 #3
        day += count_2*2
        count_1 -= count_2
        count_2 = 0
        if count_2 == 0:
            day += (count_1 * 2) - 1
    if count_1 < count_2:  #3 #7
        day += count_1*2
        count_2 -= count_1
        count_1 = 0
        if 1 <= count_2 < 4:
            day += count_2 + 1
        if 4 <= count_2 < 7:
            day += count_2 + 2
        if 7 <= count_2 < 10:
            day += count_2 + 3
        if 10 <= count_2 < 13:
            day += count_2 + 4
        if 13 <= count_2 < 16:
            day += count_2 + 5
        if 16 <= count_2 < 19:
            day += count_2 + 6
        if 19 <= count_2 < 22:
            day += count_2 + 7
        if 22 <= count_2 < 25:
            day += count_2 + 8
        if 25 <= count_2 < 28:
            day += count_2 + 9
        if 28 <= count_2 < 31:
            day += count_2 + 10
        if 31 <= count_2 < 34:
            day += count_2 + 11
        if 34 <= count_2 < 37:
            day += count_2 + 12
        if 37 <= count_2 < 40:
            day += count_2 + 13
        if 40 <= count_2 < 43:
            day += count_2 + 14
        if 43 <= count_2 < 46:
            day += count_2 + 15
        if 46 <= count_2 < 49:
            day += count_2 + 16
        if 49 <= count_2 < 52:
            day += count_2 + 17
        if 52 <= count_2 < 55:
            day += count_2 + 18
        if 55 <= count_2 < 58:
            day += count_2 + 19
        if 58 <= count_2 < 61:
            day += count_2 + 20
        if 61 <= count_2 < 64:
            day += count_2 + 21
        if 64 <= count_2 < 67:
            day += count_2 + 22
        if 67 <= count_2 < 70:
            day += count_2 + 23
        if 70 <= count_2 < 73:
            day += count_2 + 24
        if 73 <= count_2 < 76:
            day += count_2 + 25
        if 76 <= count_2 < 79:
            day += count_2 + 26
        if 79 <= count_2 < 82:
            day += count_2 + 27
        if 82 <= count_2 < 85:
            day += count_2 + 28
        if 85 <= count_2 < 88:
            day += count_2 + 29
        if 88 <= count_2 < 91:
            day += count_2 + 30
        if 91 <= count_2 < 94:
            day += count_2 + 31
        if 94 <= count_2 < 97:
            day += count_2 + 32
        if 97 <= count_2 < 100:
            day += count_2 + 33
    print(f'#{tc} {day}')



# for tc in range(1, int(input())+1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     arr.sort(reverse=True)
#     day = 0
#     count_1 = 0
#     count_2 = 0
#     for i in range(1, N): # 4개 나무면 처음 가장 큰 거 빼고 3개
#         if (max(arr)-arr[i]) % 3 == 0:
#             day += (max(arr)-arr[i])//3*2
#         if (max(arr)-arr[i]) % 3 == 1:
#             day += (max(arr)-arr[i])//3*2
#             count_1 += 1
#         if (max(arr)-arr[i]) % 3 == 2:
#             day += (max(arr)-arr[i])//3*2
#             count_2 += 1
#     if count_1 == count_2:
#         day += count_1+count_2
#     if count_1 > count_2:
#         if count_2 != 0:
#             day += count_1+count_2
#         if count_2 == 0:
#             day += count_1
#     if count_2 > count_1:
#         if count_1 != 0:
#             day += count_1+count_2+1
#         if count_1 == 0:
#             day += count_2+1
#     print(f'#{tc} {day}')


# for tc in range(1, int(input())+1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     arr.sort(reverse=True)
#     count = 0
#     ans = 0
#     for i in range(1, N): # 4개 나무면 처음 가장 큰 거 빼고 3개
#         count += max(arr)-arr[i]
#     if count % 3 == 0:
#         ans = (count//3)*2
#     if count % 3 == 1:
#         ans = (count//3)*2+1
#     if count % 3 == 2:
#         ans = (count//3)*2+2
#     print(f'#{tc} {ans}')

#1 0
#2 2
#3 1
#4 14
#5 4
#6 168
#7 17
#8 26
#9 32
#10 196
#11 404
#12 28
#13 36
#14 34
#15 363
#16 984
#17 55
#18 62
#19 62
#20 889
#21 1847
#22 66
#23 98
#24 94
#25 1892
#26 4172
#27 111
#28 132
#29 122
#30 3878

