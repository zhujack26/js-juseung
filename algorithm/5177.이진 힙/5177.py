def heap_push(item):
    heap.append(item)
    # 완전 이진 트리니까 맨 마지막 노드는 노드 길이 끝에, 부모 = 자식 // 2
    child_idx = len(heap) - 1
    parent_idx = child_idx // 2
    # 부모 노드가 루트 노드일 때까지, 작은 게 계속 위로
    while parent_idx and heap[parent_idx] > heap[child_idx]:
        heap[parent_idx], heap[child_idx] = heap[child_idx], heap[parent_idx]
        # 안에서 바꿔줘야 함 / 밖에서 부모idx변수가 자동으로 바뀌지 않음.
        child_idx = parent_idx
        parent_idx = child_idx // 2


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    nums = list(map(int, input().split()))
    heap = ['최소힙 :'] # 0번 인덱스는 안 쓸 거니까 표시로나 쓰자
# [1] 인풋 리스트를 모두 힙리스트에 추가
    for i in nums:
        heap_push(i)
# [2] 마지막 인덱스를 찾아서
    end_idx = len(heap) - 1
# [3] 부모(인덱스//2)를 구해서 더하기 루트까지 반복
    answer = 0
    while end_idx > 1:
        answer += int(heap[end_idx // 2])
        end_idx = end_idx // 2
    print(f'#{tc} {answer}')