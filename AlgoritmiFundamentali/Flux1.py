def getInput():
    f = open("input.txt", "r")
    continut_fisier = f.read()
    inputList = continut_fisier.split('\n')
    n = int(inputList[0])
    start, finish = inputList[1].split(' ')
    start, finish = int(start), int(finish)
    m = int(inputList[2])
    edges = []
    adj = [[] for x in range(n+1)]
    rev_adj = [[]for x in range(n+1)]
    flux = [[0 for y in range(n+1)] for x in range(n+1)]
    rev_capacitate = [[0 for y in range(n+1)] for x in range(n+1)]
    capacity2 = [[0 for y in range(n+1)] for x in range(n+1)]

    for i in range(3, len(inputList)):
        line = inputList[i].split()
        x, y, c, f = [int(x) for x in line]
        edges.append((x, y, c, f))
        adj[x].append((y, c, f))
        rev_adj[x].append(y)
        flux[x][y] = f
        rev_capacitate[y][x] = c - f
        capacity2[x][y] = c
    return n, m, edges, adj, flux, rev_capacitate, capacity2, rev_adj, start, finish

INF = 1000000
n, m, edges, adj, flux, rev_capacitate, capacity2, rev_adj, start, finish = getInput()

flux_in = [0 for x in range(n+1)]
flux_out = [0 for x in range(n+1)]

ok = True
for edge in edges:
    x, y, c, f = edge
    if f > c:
        ok = False
    flux_out[x] += f
    flux_in[y] += f

for i in range(1, n+1):
    if flux_in[i] != flux_out[i] and i != start and i != finish:
        ok = False

# if ok:
#     print("DA")
# else:
#     print("NU")


# O(nm^2)
# rezolvarea in O(mL) este in fisierul Fulkerson.py

def bfs(start, finish):
    parent = [-1 for x in range(n + 1)]
    parent[start] = -2
    queue = [(start, INF)]
    while queue:
        node, flow = queue.pop(0)
        for dest_node in adj[node]:
            y, c, f = dest_node
            if parent[y] == -1 and capacity2[node][y] > 0:
                parent[y] = node
                dest_flow = min(flow, capacity2[node][y])
                if y == finish:
                    return dest_flow, parent
                queue.append((y, dest_flow))
    return 0, parent


def getFlow2(start, finish):
    flow = 0
    ok = True
    while ok:
        new_flow, parent = bfs(start, finish)
        if new_flow == 0:
            break
        flow = flow + new_flow
        node = finish
        while node != start:
            capacity2[parent[node]][node] -= new_flow
            capacity2[node][parent[node]] += new_flow
            node = parent[node]
    return flow


print(getFlow2(start, finish))

def get_rez_list():
    for i in range(n+1):
        for j in range(n+1):
            if capacity2[i][j] > 0:
                capacity2[j][i] = capacity2[i][j]
    for i in range(n + 1):
        for j in range(n + 1):
            if capacity2[i][j] > 0 and j in [x[0] for x in adj[i]]:
                print(i, j, capacity2[i][j])

    queue = [start]
    ans = [start]
    while queue: #bfs pentru gasirea setului dinaintea taieturii
        node = queue.pop(0)
        for next_node in adj[node]:
            y, c, f = next_node
            if y not in ans and capacity2[y][node] < c:
                ans.append(y)
                queue.append(y)
    min_cut = 0
    list = []
    for i in ans:
        for node in adj[i]:
            y, c, f = node
            if y not in ans:
                min_cut += c
                list.append((i, y))
    return min_cut, list


min_cut, list = get_rez_list()
print(min_cut)
for node in list:
    print(node)