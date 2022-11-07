def inorder(n):  # 중위순회
    if n <= N:
        inorder(2*n)
        ans.append(E_list[n])  # visit(n)
        inorder(2*n+1)

# 원래 중위순회 공식
# def inorder(n):
#     if n:
#         inorder(ch1[n])
#         print(n, end =' ')
#         inorder(ch2[n])

for tc in range(1, 11):
    N = int(input())
    E_list = [""] * (N + 1)  # 정점 총 수 + 1= 간선 수
    for i in range(1, N+1):
        list_input = input().split()
        E_list[i] = list_input[1]

    ans = []
    inorder(1)
    print(f'#{tc} {"".join(ans)}')
    #구분자를 공백으로 지정하여 출력
