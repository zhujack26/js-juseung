def enq(n):
    global last
    last += 1 #마지막 정점 추가
    heap[last] = n #마지막 정점에 key 추가
    #부모 < 자식 인 경우 자리 교환
    c = last
    p = c//2  # 완전이진트리에서 부모 정점 번호
    while p and heap[p] < heap [c]:
# 부모가 있고, 부모 < 자식 인경우 자리 교환
        heap[p], heap[c] = heap[c], heap[p]
heap = [0] * 100
last = 0
