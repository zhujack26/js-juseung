for tc in range(1, int(input())+1):
    P, A, B = map(int, input().split())
    A_l = 1
    A_r = P
    A_count = 0
    while True :
        if A > int((A_l+A_r)/2):
            A_l = int((A_l+A_r)/2)
            A_count += 1
        elif A < int((A_l+A_r)/2):
            A_r = int((A_l+A_r)/2)
            A_count += 1
        elif A == int((A_l+A_r)/2):
            A_count += 1
            break
    B_l = 1
    B_r = P
    B_count = 0
    while True :
        if B > int((B_l+B_r)/2):
            B_l = int((B_l+B_r)/2)
            B_count += 1
        elif B < int((B_l+B_r)/2):
            B_r = int((B_l+B_r)/2)
            B_count += 1
        elif B == int((B_l+B_r)/2):
            B_count += 1
            break
    result = 0
    if A_count > B_count :
        result = 'B'
    elif A_count < B_count :
        result = 'A'
    elif A_count == B_count :
        result = 0

    print(f'#{tc} {result}')