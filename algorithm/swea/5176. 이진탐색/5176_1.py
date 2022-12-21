def inorder(n):  # 중위순회
    global num
    if n <= E:
        inorder(2 * n)
        tree[num+1][0] = n
        num += 1
        inorder(2 * n + 1)

# 원래 중위순회 공식
# def inorder(n):
#     if n:
#         inorder(ch1[n])
#         print(n, end =' ')
#         inorder(ch2[n])

T = int(input())
for tc in range(1, T+1):
    E = int(input())
    tree = [[0, i] for i in range(E+1)]
    num = 0

    inorder(1)
    tree.sort()
    print(tree)



