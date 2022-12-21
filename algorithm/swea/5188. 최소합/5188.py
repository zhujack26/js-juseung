T = int(input())
for k in range(T):
    N = int(input())
    routeList = [list(map(int,input().split())) for _ in range(N)]
    global minNum
    minNum = 99999

    def findRoute(nowIdx,thisNum):
        global minNum
        if nowIdx[1]==N-1 and nowIdx[0]+1<N-1:
            nowCount = thisNum+ routeList[nowIdx[0]+1][nowIdx[1]]
            findRoute([nowIdx[0]+1,nowIdx[1]],nowCount)
        elif nowIdx[1]==N-1 and nowIdx[0]+1==N-1:
            nowCount = thisNum + routeList[N-1][N-1]
            if nowCount<minNum:
                minNum = nowCount
        elif nowIdx[1]+1<N-1 and nowIdx[0]==N-1:
            nowCount = thisNum+ routeList[nowIdx[0]][nowIdx[1]+1]
            findRoute([nowIdx[0],nowIdx[1]+1],nowCount)
        elif nowIdx[1]+1==N-1 and nowIdx[0]==N-1:
            nowCount = thisNum + routeList[N-1][N-1]
            if nowCount<minNum:
                minNum = nowCount
        else:
            nowCount1 = thisNum+ routeList[nowIdx[0]][nowIdx[1]+1]
            findRoute([nowIdx[0],nowIdx[1]+1],nowCount1)
            nowCount2 = thisNum+ routeList[nowIdx[0]+1][nowIdx[1]]
            findRoute([nowIdx[0]+1,nowIdx[1]],nowCount2)




    findRoute([0,0],routeList[0][0])
    print(f'#{k+1} {minNum}')