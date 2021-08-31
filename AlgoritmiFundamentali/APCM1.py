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


def Kruskral(n, m, edges):
    # varianta O(n^2 + m*log(n))
    tree_id = [x for x in range(n + 1)]
    edges = sorted(edges, key=lambda x: x[2])

    mst = []
    for edge in edges:
        x, y, w = edge
        if tree_id[x] != tree_id[y]:
            old_id = tree_id[y]
            new_id = tree_id[x]
            for i in range(1, n + 1):
                if tree_id[i] == old_id:
                    tree_id[i] = new_id
            mst.append(edge)
    return mst


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


def KruskralDSU(n, m, edges): #disjoint set union
    # varianta O(m*log(n))

    for i in range(1, n+1):
        create_tree(i)
    edges = sorted(edges, key=lambda x: x[2])

    mst = []
    for edge in edges:
        x, y, w = edge
        if get_tree(x) != get_tree(y):
            mst.append(edge)
            tree_union(x, y)
    return mst


n, m, edges = getInput()
parent = [0 for x in range(n + 1)]
rank = [0 for x in range(n + 1)]

print(Kruskral(n, m, edges))  # varianta O(n^2 + m*log(n))
print(KruskralDSU(n, m, edges))  # varianta O(m*log(n))
