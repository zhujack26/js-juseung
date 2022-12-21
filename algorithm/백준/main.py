# import sys
# sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split(' '))
    N_str = map(int, input().split(' '))  #변수 할당
    A = list(N_str)    #정수 ai의 리스트
    # N=10, M=3 일 때는 비교할 집합이 8개
    # N=20, M 19일 때는 비교할 집합이 2개
    # 따라서 비교할 집합의 개수를 구하는 공식은 N-M+1
    # for문 in에 넣을 값 : N-M+1
    max_A = 0
    min_A = 10000000
    for i in range(N-M+1):  # ex) i = 0,1
        if sum(A[i:i+M]) > max_A:
            max_A == sum(A[i:i+M])
        elif sum(A[i:i+M]) < min_A:
            min_A == sum(A[i:i+M])
        print(f"{tc}", max_A-min_A)
