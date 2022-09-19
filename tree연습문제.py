def preorder(n):   # 전위순회
    if n:
        print(n, end = '')  # visit(n)
        preorder(ch1[n])
        preorder(ch2[n])

# def inorder(n):  # 중위순회
#     if n:
#         inorder(ch1[n])
#         print(n, end = '') #visit(n)
#         inorder(ch2[n])
#
# def postorder(n):
#     if n :
#         postorder(ch1[n])
#         postorder(ch1[n])
#         print(n, end = '') #visit(n)

V = int(input()) # 간선 수
arr = list(map(int, input().split()))
E = V-1    # 정점 번호, 노드
root = 1
# 부모를 인덱스로 자식 번호 저장
ch1 = [0]*(V + 1)   # 표1
ch2 = [0]*(V + 1)   # 표2

for i in range(E):
    p, c = arr[i*2], arr[i*2+1]
# for j in range(0, E*2, 2):
#     p, c = arr[j], arr[j+1]
    if ch1[p] == 0:
        ch1[p] = c
    else :
        ch2[p] = c

preorder(root)