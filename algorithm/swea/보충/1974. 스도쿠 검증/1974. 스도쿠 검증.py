import sys
sys.stdin = open('input.txt')
for tc in range(1, int(input())+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    # 각 줄을 1~9로 정렬시키고 리스트에 append하여 1~9와 일치 여부
    A = [i for i in range(1,10)]
    ans = 1
    D = []
    E = []
    F = []
    ans = 1
    for i in range(9):
        B = []
        C = []
        for j in range(9):
            B.append(arr[i][j]) # 가로검증
            C.append(arr[j][i]) # 세로검증
        B.sort() #[1,2,3,4,5,6,7,8,9]
        C.sort()
        if A != B:
            ans = 0
        if A !=C:
            ans = 0
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            D = []
            for k in range(3):
                for l in range(3):
                    D.append(arr[i+k][j+l])
            D.sort()
            if A != D:
                ans = 0

    print(f'#{tc} {ans}')