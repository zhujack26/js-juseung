for tc in range(1, int(input())+1):
    N = int(input())
    board_1 = [0]*200 #홀수리스트
    board_2 = [0]*200 #짝수리스트
    for i in range(N):
        now, back = map(int, input().split())
        #1,6 #5,10
        if now > back :
            now, back = back, now
        if now % 2== 1 and back % 2 == 1: #now랑 back 홀수일때  ex) 1,5 3,9일 때
            for j in range(now//2, back//2+1):
                board_1[j] += 1
                board_2[j] += 1
        elif now % 2== 1 and back % 2== 0: #now랑 back 홀짝일때  ex) 1,4 3,6일 때
            for j in range(now//2, back//2):
                board_1[j] += 1
                board_2[j] += 1
        elif now % 2== 0 and back % 2== 1: #now랑 back 짝홀일때  ex) 2,5 4,7일 때
            for j in range(now//2-1, back//2+1):
                board_1[j] += 1
                board_2[j] += 1
        elif now % 2== 0 and back % 2 == 0: #now랑 back 짝수일때  ex) 2,6 4,8일 때
            for j in range(now//2-1, back//2):
                board_1[j] += 1
                board_2[j] += 1
    print(f'#{tc}' ,max(board_1+board_2))