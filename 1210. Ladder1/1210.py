import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    dr = [-1, 0, 0]  # 상, 우, 좌
    dc = [0, 1, -1]
    direction = 0

    for i in range(100):
        if arr[99][i] == 2:
            x, y = 99, i #당첨이자 시작점
            break





