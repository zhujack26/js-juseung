for tc in range(1, int(input())+1):
    arr = []
    P, A, B = map(int, input().split())
    c_A = P//2
    c_B = P//2
    count_A = 0
    count_B = 0
    result = 0
    while P >= 1 :
        if A > c_A and A != c_A:
            c_A = (P+c_A)//2
            count_A += 1
            if A == c_A:
                break
        elif A < c_A and A != c_A:
            c_A = c_A//2
            count_A += 1
            if A == c_A:
                break
    while P >= 1 :
        if B > c_B and B != c_B:
            c_B = (P+c_B) // 2
            count_B += 1
            if B == c_B:
                break
        elif B < c_B and B != c_B:
            c_B = c_B // 2
            count_B += 1
            if B == c_B:
                break
    if count_A > count_B :
        result = 'A'
    if count_B > count_A:
        result = 'B'
    if count_A == count_B :
        result = 0
    print(f'{tc} {result}')