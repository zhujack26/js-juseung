# 분할 => 조합과 관련이 있다.
# 주어진 전체 N개의 자료에서 2개 혹은 3개를 뽑는 (선택하는) 모든 경우를
N = 5
arr = [i for i in range(1, N+1)]

# 3구간으로 분할 => (0, i)(i, j)(j, N-1)
for i in range(1, N-2+1): # 1,
    for j in range(i+1, N-1+1): #2,3,4 조합  IM 임의 2개 점수구간
        print(arr[0:i], arr[i:j], arr[j:N]) # arr[0:1], arr[1:2]  arr[2:5]