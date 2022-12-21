def preorder(n):
    global count
    if n == 0:
        return
    count += 1
    preorder(ch1[n])
    preorder(ch2[n])

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))
    ch1 = [0]*(E+2)
    ch2 = [0]*(E+2)
    for i in range(0,len(arr),2):
        p, c = arr[i], arr[i+1]
        if ch1[p] :
            ch2[p] = c
        else:
            ch1[p] = c

    count = 0
    preorder(N)
    print(f"#{tc} {count}")