def preorder(n):
    if n <= N:
        pre_tree.append(n)
        preorder(2*n)
        preorder(2*n+1)

def inorder(n):
    if n <= N:
        inorder(2*n)
        in_tree.append(n)
        inorder(2*n+1)

def postorder(n):
    if n <= N:
        postorder(2*n)
        postorder(2*n+1)
        post_tree.append(n)

def last_inorder(n):
    if n <= len(max_tree)-1:
        last_inorder(2*n)
        ans.append(max_tree[n])
        last_inorder(2*n+1)

t = int(input())
for tc in range(t):
    N = int(input())

    pre_tree = [0]
    in_tree = [0]
    post_tree = [0]

    preorder(1)   # 전위순회
    inorder(1)    # 중위순회
    postorder(1)  # 후위순회
    # print(pre_tree)
    # print(in_tree)
    # print(post_tree)

    max_tree = [0]

    # 전위순회, 중위순회, 후위순회 중에 각 노드의 최대값을 구해서 멕스트리에 넣어줌
    for i in range(1, len(pre_tree)):
        max_tree.append(max(pre_tree[i], in_tree[i], post_tree[i]))
    # print(max_tree)

    # 멕스트리를 중위순회해서 최종 정답 리스트에 담아준다.
    ans = []
    last_inorder(1)
    print(f'#{tc+1}', *ans)


