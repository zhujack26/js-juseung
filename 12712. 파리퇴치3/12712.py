# import sys
# sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 분명 범위 밖을 벗어나서 인덱스 에러가 뜰 텐데 어떻게 하지?
    # if 문으로 범위 지정
    # +
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    # x
    dxx = [-1, 1, 1, -1]
    dyy = [1, 1, -1, -1]
    max_value = 0   #최대값을 구하기 위해 변수 설정
    for i in range(N):
        for j in range(N):
            # 초기값이 0이 아니고 아래와 같은 이유는 문제에서 상하좌우뿐만 아니라
            # 가운데 값도 구해야하기 때문. 따라서 초기값이 0이면 상하좌우+0 으로 된다.
            temp1 = arr[i][j]
            temp2 = arr[i][j]
            for k in range(4) :
                for l in range(1, M):
                    if 0 <= i+dx[k]*l <N and 0 <= j+dy[k]*l < N:
                        temp1 += arr[i+dx[k]*l][j+dy[k]*l]  # M의 값에 에 따라 길이를 조절 할수 있다
                for l in range(1, M):
                    if 0 <= i+dxx[k]*l <N and 0 <= j+dyy[k]*l < N:
                        temp2 += arr[i+dxx[k]*l][j+dyy[k]*l]
            if temp1 < temp2:    # 여기서 if 위치 크게 상관없음
                if max_value < temp2:
                    max_value = temp2
            else:     # =포함해도 상관없음.
                if max_value < temp1:
                    max_value = temp1
    print(f'#{tc} {max_value}')
