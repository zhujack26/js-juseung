#인접 행렬로 정리하기
V, E = map(int, input().split())  # Vertex(포도알), Edge(선) 갯수

adj_matrix = [[0] * (V + 1) for _ in range(V + 1)]  # 인접행렬 기본틀 + 0번 포도알은 안씀

for _ in range(E):  # 간선 갯수만큼 돌면서 연결 정보를 받음
    start, end = map(int, input().split())  # 시작점과 끝점
    adj_matrix[start][end] = 1
    adj_matrix[end][start] = 1

print(adj_matrix)


#인접 리스트로 정리하기
V, E = map(int, input().split())

adj_list = [[] for _ in range(V + 1)]

for _ in range(E):
    start, end = map(int, input().split())
    adj_list[start].append(end)
    adj_list[end].append(start)  # 양방향


# DFS 풀이방법 정리

# 1. 스택 + 인접행렬
V, E = map(int, input().split())
adj_matrix = [[0]*(V+1) for _ in range(V+1)]
for _ in range(E):
    start, end = map(int, input().split())
    adj_matrix[start][end] == 1
    adj_matrix[end][start] == 1
stack = [1]
visited = []

while stack:
    current = stack.pop()
    if current not in visited:
        visited.append(current)
    for destination in range(V+1)



