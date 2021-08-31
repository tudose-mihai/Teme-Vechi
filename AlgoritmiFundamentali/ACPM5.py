def getInput():
    f = open("input.txt", "r")
    continut_fisier = f.read()
    inputList = continut_fisier.split('\n')

    input = inputList[0].split()
    n, m = int(input[0]), int(input[1])
    inputList.pop(0)
    edges = []
    for line in inputList:
        input = line.split()
        x, y, w = int(input[0]), int(input[1]), int(input[2])
        edges.append((x, y, w))
    return n, m, edges


def create_tree(x):
    parent[x] = x
    rank[x] = 0


def get_tree(x):
    if x == parent[x]:
        return x
    return get_tree(parent[x])


def tree_union(x, y):
    tree_x = get_tree(x)
    tree_y = get_tree(y)
    if not tree_x == tree_y:
        if rank[tree_x] < rank[tree_y]:
            tree_x, tree_y = tree_y, tree_x
        parent[tree_y] = tree_x
        if rank[tree_x] == rank[tree_y]:
            rank[tree_x] += 1


def KruskralDSU(n, m, edges):
    for i in range(1, n+1):
        create_tree(i)
    edges = sorted(edges, key=lambda x: x[2])
    mst = []
    cost = 0
    for edge in edges:
        x, y, w = edge
        if get_tree(x) != get_tree(y):
            mst.append(edge)
            cost += w
            tree_union(x, y)
    return mst, cost


n, m, edges = getInput()
parent = [0 for x in range(n + 1)]
rank = [0 for x in range(n + 1)]
visited = [False for x in range(n+1)]

apcm, cost = KruskralDSU(n, m, edges)

print("Muchiile apcm in G:")
adj_list = [[] for x in range(n+1)]
for edge in apcm:
    x, y, w = edge
    adj_list[x].append((y, w))
    adj_list[y].append((x, w))
    print(x, y)
print("Cost", cost)
# for line in adj_list:
#     index_list = [x[0] for x in line]
#     print(index_list)
#
value = input()
value = value.split()
x, y, w = int(value[0]), int(value[1]), int(value[2])
# x, y, w = 3, 5, 4
new_edge_weight = w
cycle_nodes = [(x, y, w)]
for i in range(len(adj_list)):
    line = adj_list[i]
    index_list = [x[0] for x in line]
    if x in index_list and y in index_list:
        y, w = line[0]
        cycle_nodes.append((i, y, w))
        y, w = line[1]
        cycle_nodes.append((i, y, w))
muchie_max = max(cycle_nodes[:][2])
muchie_min = min(cycle_nodes[:][2])
print("Muchia de cost maxim din ciclul inchis de", end = " ")
for edge in cycle_nodes:
    if muchie_max == edge[2]:
        print("in apcm este", edge[0], edge[1],"de cost", muchie_max)

print("Dupa adaugarea muchie apcm are costul", cost - muchie_max + new_edge_weight)

