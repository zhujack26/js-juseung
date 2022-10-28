# T = int(input())
# for tc in range(1, T+1):
#     N = int(input()) #지형의 수
#     high = list(map(int, input().split())) #지형의 높이
#     count = 0
#     for i in range(N):
#         if high[i] == high[i+1]:
#             high.pop(i+1)    #연속된 봉우리 때문에 pop으로 중복 제거
#     for j in range(1, len(high)-1):
#         if high[j-1] < high[j] and high[j] > high[j + 1]:  # 맨 앞과 끝을 제외한 봉우리 구하기
#             count = count + 1
#     if high[0] > high[1]:   # 맨 앞 봉우리
#         count = count + 1
#     if high[len(high)-1] > high[len(high)-2]:  # 맨 끝 봉우리
#         count = count + 1
#     print(f'#{tc} {count}')

## 220929###
T = int(input())
for tc in range(1, T+1):
    N = int(input()) #지형의 수
    high = list(map(int, input().split()))+[''] #지형의 높이
    count = 0
    A = []
    if N == 1:
        if high[0] > 0:
            count = count + 1
        else :
            pass
    if N == 2:
        if high[0] > 0 or high[1]>0 :
            count = count+1
    if N > 2:
        for i in range(N):
            if high[i] != high[i+1]:
                A.append(high[i])
        for i in range(1, len(A)-1):
            if A[i-1] < A[i] and A[i] > A[i+1]:
                count = count + 1
        if A[0] > A[1]:
            count = count + 1
        if A[len(A)-1] > A[len(A)-2]:
            count = count + 1
    print(f'#{tc} {count}')



