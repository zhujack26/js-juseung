for tc in range(1, int(input())+1):
    arr = list(map(int, input().split()))
    result = []
    for i in arr:
        for j in arr:
            for k in arr:
                if i != j and j != k and i != k:
                    result.append(i+j+k)
    print(f'#{tc}', sorted(list(set(result)))[-5])
