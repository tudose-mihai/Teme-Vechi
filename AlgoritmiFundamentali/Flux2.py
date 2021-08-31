# Atribuim capacitate 1 fiecarei muchii
# Aplicam Ford Fulkerson O(mL) pe noul graf
# O(mL) dar L este maxim n deci avem O(mn)


def getInput():
    f = open("input.txt", "r")
    continut_fisier = f.read()
    inputList = continut_fisier.split('\n')
    n, m = inputList[0].split(' ')
    n, m = int(n), int(m)
    edges = []
    adj = [[] for x in range(n + 1)]
    adj_init = [[] for x in range(n + 1)]
    for i in range(1, len(inputList)):
        line = inputList[i].split()
        x, y, c, f = [int(x) for x in line]
        edges.append((x, y, c, f))
        adj[x].append(y)
        adj[y].append(x)
        adj_init[x].append((y, c))
    return n, m, edges, adj, adj_init, start, finish


INF = 1000000
n, m, edges, adj, adj_init, start, finish = getInput()
visited = [False for x in range(n+1)]
red_nodes, blue_nodes = [1], []

visited[1] = True
queue = [1]
while queue:
    node = queue.pop(0)
    for next_node in adj[node]:
        if not visited[next_node]:
            if node in red_nodes:
                blue_nodes.append(next_node)
            elif node in blue_nodes:
                red_nodes.append(next_node)
            visited[next_node] = True
            queue.append(next_node)
start = 0
finish = n + 1

capacity = [[0 for y in range(n + 2)] for x in range(n + 2)]

for node in red_nodes:
    adj[start].append(node)
    adj[node].append(start)

adj.append([])
for node in blue_nodes:
    adj[node].append(finish)
    adj[finish].append(node)

for x in red_nodes:
    capacity[start][x] = INF
    for y in adj[x]:
        capacity[x][y] = 1
        capacity[y][x] = 1

for y in blue_nodes:
    capacity[y][finish] = INF



def get_path(start, end, path):
    if start == end:
        return path
    for node in adj[start]:
        cap_reziduala = capacity[start][node]
        if cap_reziduala > 0 and node not in [i[0] for i in path]:
            temp_path = [x for x in path]
            temp_path.append((node, cap_reziduala))
            next_path = get_path(node, end, temp_path)
            if next_path is not None:
                return next_path

def getFlow1(start, finish):
    path = get_path(start, finish, [])
    while path is not None:
        next_flow = min([x[1] for x in path])
        capacity[start][path[0][0]] -= next_flow
        capacity[path[0][0]][start] += next_flow
        for i in range(len(path)-1):
            x = path[i][0]
            y = path[i+1][0]
            capacity[x][y] -= next_flow
            capacity[y][x] += next_flow
        path = get_path(start, finish, [])

getFlow1(start,finish)


for i in range(1, len(adj_init)):
    for j in range(len(adj_init[i])):
        y, c = adj_init[i][j]
        print(i, y, c-capacity[i][y])
