def nodenum(i):
    if i <= n:
        nodenum(i * 2)
        nodenumlst.append(i)
        nodenum(i * 2 + 1)

# 원래 중위순회 공식
# def inorder(n):
#     if n:
#         inorder(ch1[n])
#         print(n, end =' ')
#         inorder(ch2[n])

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
# [2] 노드 번호와 노드 값, 두 가지 리스트 = 4번 노드 값은 1, 2번 노드 값은 2
    nodenumlst = []  # [4, 2, 5, 1, 6, 3]
    num = []         # [1, 2, 3, 4, 5, 6]
# [3] 1~n이 노드 값인데 완전 이진 검색 트리는 중위 순회하면 번호순으로 나옴
    for i in range(1, n+1):
        num.append(i)
    nodenum(1)
# [4] 노드 번호 1번이 루트 노드니까, nodenumlst[ 1의 인덱스 ]로 num에서 값 꺼내오기
    root = num[nodenumlst.index(1)]
# [5] 위와 같이 해당 노드 번호의 값 꺼내오기
    node = num[nodenumlst.index(n//2)]
    print(f'#{tc} {root} {node}')