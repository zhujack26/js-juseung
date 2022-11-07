import sys
sys.stdin = open('input.txt')

# 빌딩의 개수 만큼 for 문을 돌린다.
# -2, -1, +1, +2 칸의 빌딩과 비교, if문 클시
# 조망권 빌딩으로 count
for tc in range(1, 11):
    N = int(input())
    building = list(map(int, input().split()))
    count = 0
    for i in range(2, N-2):
        buildings = []
        if building[i] > building[i-2] and building[i] > building[i-1] and building[i] > building[i+1] and building[i] > building[i+2]:
            buildings.append(building[i-2])
            buildings.append(building[i-1])
            buildings.append(building[i+1])
            buildings.append(building[i+2])
            count += building[i]-max(buildings)
    print(f'#{tc} {count}')