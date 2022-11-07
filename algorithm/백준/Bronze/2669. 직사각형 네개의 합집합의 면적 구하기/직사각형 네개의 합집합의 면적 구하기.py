#전부 0 찍어주기
# 사각형 범위에 1을 찍어주고 다 더하면 중복값 상관 x
arr = [[0]*99 for _ in range(100)]
for i in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for j in range(x1, x2):
        for k in range(y1, y2):
            arr[j][k] = 1
count = 0
for i in arr:  # 2차원 배열안에서의 합으로 1 개수 카운팅 [[0,0,0...][0,0,1...]]
    count += sum(i)
print(count)