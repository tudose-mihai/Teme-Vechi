import heapq


def getInput():
    f = open("input.txt", "r")
    continut_fisier = f.read()
    inputList = continut_fisier.split('\n')
    line = inputList[0].split(' ')
    n, m = line
    n, m = int(n), int(m)

    edges = []
    adj = [[] for i in range(n + 1)]
    for i in range(1, len(inputList)):
        line = inputList[i].split()
        x, y, w = int(line[0]), int(line[1]), int(line[2])
        adj[x].append((y, w))
        adj[y].append((x, w))
        edges.append((x, y, w))
    return n, m, edges, adj


INF = 1000000
n, m, edges, adj = getInput()
dist = [INF for node in range(n + 1)]
parent = [0 for node in range(n + 1)]

start = 4
# start = int(input())

dist[start] = 0
h = [(0, start)]

while h:
    w, node = heapq.heappop(h)
    if w > dist[node]:
        continue
    for next_node in adj[node]:
        y, next_w = next_node
        if w + next_w < dist[y]:  # mai bun decat drumul curent!
            parent[y] = node  # penultima muchie pentru drumul cel mai scurt
            dist[y] = w + next_w
            heapq.heappush(h, (dist[y], y))

print(dist)
