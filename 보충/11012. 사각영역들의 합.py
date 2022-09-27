# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     r, c, l = map(int, input().split())
#
#     for i in range(M):
#         arr[r][c]+arr[r][c+1]+arr[r+1][c]+arr[r+1][c+1]
#         # M 개수 만큼의 좌표들 구현 x

for tc in range(1, int(input()) + 1):  #T 바로 삽입
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for _ in range(M):   # M 개수 만큼의 좌표들 구현
        sr, sc, wh = map(int, input().split())
        for r in range(sr, min(sr + wh, N)):   #min으로 비교를 통해 N넘어가는거 방지
            for c in range(sc, min(sc + wh, N)):
                ans += arr[r][c]
                arr[r][c] = 0   # 0으로 만들어줌으로써 중복값도 방지

    print(f'#{tc} {ans}')