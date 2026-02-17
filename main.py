import heapq

n, m = map(int, input().split())
graph = [[] for _ in range(n)]

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

start = int(input())
dist = [float('inf')] * n
dist[start] = 0

pq = [(0, start)]
while pq:
    d, node = heapq.heappop(pq)
    if d > dist[node]:
        continue
    for nei, w in graph[node]:
        if dist[nei] > d + w:
            dist[nei] = d + w
            heapq.heappush(pq, (dist[nei], nei))

print(*dist)
