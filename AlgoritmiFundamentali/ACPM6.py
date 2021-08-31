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
    if(x == parent[x]):
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

def Kruskral(n, m, edges):
    global parent, rank
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

def KruskralSecondBest(n, m, edges, best_cost):
    global parent, rank
    for i in range(1, n+1):
        create_tree(i)
    edges = sorted(edges, key=lambda x: x[2])

    mst = []
    min_cost = 1000000
    min_index = 0
    for i in range(len(edges)):
        mst.clear()
        for j in range(1, n + 1):
            create_tree(j)
        rank = [0 for x in range(n + 1)]
        second_best_edges = [edge for edge in edges if edge != edges[i]]
        cost = 0
        for edge in second_best_edges:
            x, y, w = edge
            if get_tree(x) != get_tree(y):
                mst.append(edge)
                cost += w
                tree_union(x, y)
        if best_cost < cost < min_cost:
            min_cost = cost
            min_index = i
    mst.clear()
    for i in range(1, n+1):
        create_tree(i)
    rank = [0 for x in range(n + 1)]
    second_best_edges = [edge for edge in edges if edge != edges[min_index]]
    cost = 0
    for edge in second_best_edges:
        x, y, w = edge
        if get_tree(x) != get_tree(y):
            mst.append(edge)
            cost += w
            tree_union(x, y)
    return mst, cost


n, m, edges = getInput()
parent = [0 for x in range(n + 1)]
rank = [0 for x in range(n + 1)]

mst, best_cost = Kruskral(n, m, edges)
print("Primul")
print("Cost", best_cost)
print("Muchii")
for line in mst:
    print(line)
mst, cost = KruskralSecondBest(n, m, edges, best_cost)
print("Al Doilea")
print("Cost", cost)
print("Muchii")
for line in mst:
    print(line)