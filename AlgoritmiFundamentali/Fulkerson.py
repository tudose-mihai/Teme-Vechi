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
    adj_init = [[]for x in range(n+1)]
    capacity = [[0 for y in range(n+1)] for x in range(n+1)]

    rev_capacitate = [[0 for y in range(n+1)] for x in range(n+1)]
    capacity2 = [[0 for y in range(n+1)] for x in range(n+1)]

    for i in range(3, len(inputList)):
        line = inputList[i].split()
        x, y, c, f = [int(x) for x in line]
        edges.append((x, y, c, f))
        adj[x].append(y)
        adj[y].append(x)
        adj_init[x].append((y, c))
        capacity[x][y] = c - f
        capacity[y][x] = f
        capacity2[x][y] = c
    return n, m, edges, adj, adj_init, capacity, capacity2, start, finish


INF = 1000000
n, m, edges, adj, adj_init, capacity, capacity2, start, finish = getInput()


# for line in flux:
#     print(line)
# print()




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

