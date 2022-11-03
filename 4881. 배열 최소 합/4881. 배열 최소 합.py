for tc in range(1, int(input())+1):
    N = int(input())
    # arr = [list(map(int, input().split())) for _ in range(N)]
    choice_a = []
    sum_b = []
    for i in range(N):
        arr = list(map(int, input().split()))
        if len(choice_a)>0:
            arr.remove(choice_a[-1])
        for j in range(N):
            if arr[j] == min(arr):
                choice_a.append(j)
                sum_b.append(arr[j])
