T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    ans = "NO"
    check = []
    check_1 = []
    for i in range(N):
        for j in range(N):
            result ="".join(check)
            if "ooooo" in result :
                ans = "YES"

    for i in range(N):
         check_1.append(arr[i][i])
         result_1 = "".join(check_1)
         if "ooooo" in result_1 :
             ans = "YES"

    for i in range(N):
        check_2 = []
        for j in range(N):
            check_2.append(arr[i][j])
            result_2 = "".join(check_2)
            if "ooooo" in result_2:
                ans = "YES"

    for i in range(N):
        check_3 = []
        for j in range(N):
            check_3.append(arr[j][i])
            result_3 = "".join(check_3)
            if "ooooo" in result_3:
                ans = "YES"

    print(f"#{tc} {ans}")