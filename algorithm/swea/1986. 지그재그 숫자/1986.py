# 1부터 N까지의 숫자에서 홀수는 더하고 짝수는 뺐을 때 최종 누적된 값을 구해보자.

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    N_odd = 0
    for i in range(1, N+1, 2):
        N_odd = N_odd+ i

    N_even = 0
    for j in range(2, N+1, 2):
        N_even = N_even - j

    print(f"#{tc} {N_odd+N_even}")