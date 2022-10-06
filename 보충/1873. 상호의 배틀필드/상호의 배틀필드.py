for tc in range(1, int(input())+1):
    H, W = map(int, input().split())
    arr = [list(input()) for _ in range(H)]
    N = int(input())
    N_list = list(input())
    cnt = 0
    a = [i for i in N_list if i == 'S']
    print(len(a))
    print(f'#{a}')