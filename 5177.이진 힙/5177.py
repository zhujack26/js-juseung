def heap_make(idx):   # 힙만드는 거
    if heap[idx] < heap[idx//2]:
        heap[idx], heap[idx//2] = heap[idx//2], heap[idx]
        heap_make(idx//2) # 위치 이동



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nord = list(map(int, input().split()))
    heap = [0]
    idx = 0

    for i in nord:
        heap.append(i)
        idx += 1
        heap_make(idx)

    result = 0
    while idx > 0:
        idx //=2
        result += heap[idx]
    # idx = idx // 2
    print(f'#{tc} {result}')