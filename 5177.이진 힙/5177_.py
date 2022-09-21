def heap_push(item):
    heap.append(item)  # 완전 이진트리니까 맨끝에 +

    child = len(heap) - 1
    parent = child // 2
    # 루트노드가 아니고, 위에 봤는데 더 큰 경우 계속 돎
    while parent and heap[parent] > heap[child]:
        heap[parent], heap[child] = heap[child], heap[parent]  # swap
        child = parent
        parent = child // 2


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    heap = [0] + []

    for i in map(int, input().split()):
        heap_push(i)

    sum = 0
    idx = N // 2
    for i in range(N // 2):
        if idx < 1:
            break
        else:
            sum += heap[idx]
            idx = idx // 2
    '''
    이걸로 대체 가능한
    ans = 0
    while N:
        N //= 2
        ans += tree[N]
    print(f'#{t + 1} {ans}')
    '''

    print(f'#{tc} {sum}')
