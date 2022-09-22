# 부모 노드의 값 < 자식 노드의 값 유지
def heap_min(number):   # 힙만드는 거
    if heap[number] < heap[number//2]: #자식 노드의 값이 부모 노드의 값보다 작으면,
        heap[number], heap[number//2] = heap[number//2], heap[number]
        heap_min(number//2) # 위치 이동



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nord = list(map(int, input().split()))
    heap = [0]
    index = 0

    for i in nord:
        heap.append(i)
        index += 1
        heap_min(index)
        #디버깅
        #tc 1, nord = 7,2,5,3,4,6
        #heap 7추가 idx =1, hepa_min(1)

    result = 0
    while index > 0:
        index = index // 2
        result += heap[index]
    print(f'#{tc} {result}')