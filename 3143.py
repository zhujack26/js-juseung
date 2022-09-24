T = int(input())
for tc in range(1, T+1):
    A, B = map(str, input().split())
    result = len(A.replace(B, "1"))  #len 값을 구하기 위해 임의의 값 1 활용
    print(f"#{tc} {result}")
    list = []
    