N, M = map(int, input().split())
X = []
J = []
current = 0
count = 0
for i in range(N):
    X.append(int(input()))
for i in range(M):
    J.append(int(input()))
for i in range(M):
    count += 1
    current += J[i]   #J[0] 주사위 처음 던지면 값만큼 N 이동
    if current >= N:
        break
    current += X[current]  #X에 따라 다시 이동
    if current >= N:
        break
print(count)