import heapq

# vrem un drum cu risc minim
# ex: 2^(-3) -> 2^(-6) -> 2^(-2) are risc 2^(-11)
# pe cand 2^(-2) -> 2^(-5) -> 2^(-1) are risc 2^(-8)
# 2^(-8) > 2^(-11) deci evident al doilea drum are risc mai mare

# putem transforma 2^(-x) in -x si cautam minimul.
# Intradevar drumul -3 -> -6 -> -2 => -11 este mai scurt decat -2 -> -5 -> -1 => -8

# Pentru a avea doar valori pozitive, memoram valoarea minima si adunam la toate muchiile aceasta valoare
# Drumurile devin 3 -> 0 -> 4 => 7; 4 -> 1 -> 5 => 10


def getInput():
    f = open("input.txt", "r")
    continut_fisier = f.read()
    inputList = continut_fisier.split('\n')
    line = inputList[0].split(' ')
    n, m = line
    n, m = int(n), int(m)
    min_w = 1000000
    edges = []
    adj = [[] for i in range(n + 1)]
    for i in range(1, len(inputList)):
        line = inputList[i].split()
        x, y, w = int(line[0]), int(line[1]), int(line[2])
        min_w = min(min_w, w)
        adj[x].append((y, w))
        edges.append((x, y, w))

    # adunam la fiecare muchie valoarea prag
    for i in range(len(adj)):
        for j in range(len(adj[i])):
            y, w = adj[i][j]
            adj[i][j] = y, w-min_w
    for i in range(len(edges)):
        x, y, w = edges[i]
        edges[i] = (x, y, w-min_w)

    return n, m, edges, adj, min_w


INF = 1000000
n, m, edges, adj, min_w = getInput()
dist = [INF for node in range(n + 1)]
parent = [0 for node in range(n + 1)]

start = int(input())
finish = int(input())

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

node = finish
path = []
risc = 0
while node != start:
    risc += 1
    path.append(node)
    node = parent[node]
path.append(start)

print(path[::-1])
print("Risc: 1/2^(",risc*min_w + dist[finish],")",sep='')