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
        x, y, w = int(input[0])-1, int(input[1])-1, int(input[2])
        edges.append((x, y, w))
    return n, m, edges

INF = 1000000

def Prim1(n, m, edges): #versiunea O(n^2)
    m_adiacenta = [[INF for y in range(n)] for x in range(n)] #INF unde nu avem muchii
    for edge in edges:
        x, y, w = edge
        m_adiacenta[x][y] = w
        m_adiacenta[y][x] = w
    selected = [False for i in range(n)]
    min_outgoing_edge = [(INF, -1) for x in range(n)] # (greutate muchie minima, celalalt capat al muchiei)
    min_outgoing_edge[0] = (0, -1) # trebuie sa incepem de undeva
    for i in range(n):
        node = -1
        for j in range(n):
            if not selected[j] and (node == -1 or min_outgoing_edge[j][0] < min_outgoing_edge[node][0]):
                node = j    # garantat alegem un nod, si posibil gasim o muchie cu greutate mai mica
        selected[node] = True
        if min_outgoing_edge[node][1] != -1: # daca a fost modificat, inseamna ca deja i-am gasit muchia minima, afisam direct
            print(node, min_outgoing_edge[node][1])
        for j in range(n):
            if m_adiacenta[node][j] < min_outgoing_edge[j][0]: #cautam pentru fiecare vecin daca nodul curent are o muchie mai mica
                min_outgoing_edge[j] = (m_adiacenta[node][j], node)

def Prim2(n, m, edges):
    selected = [False for i in range(n)]
    lista_adiacenta = [[] for x in range(n)]
    for edge in edges:
        x, y, w = edge
        lista_adiacenta[x].append((y, w))
        lista_adiacenta[y].append((x, w))
    min_outgoing_edge = [(INF, -1) for x in range(n)]
    min_outgoing_edge[0] = (0, -1)
    dict = {0: 0}
    for i in range(n):
        node_w = min(dict.keys())
        node = dict[node_w]
        dict.pop(node_w)
        selected[node] = True
        if min_outgoing_edge[node][1] != -1:
            print(node, min_outgoing_edge[node][1])
        for edge in lista_adiacenta[node]:
            y, w = edge
            if not selected[y] and w < min_outgoing_edge[y][0]:
                if min_outgoing_edge[y][0] in dict:
                    dict.pop(min_outgoing_edge[y][0])
                min_outgoing_edge[y] = (w, node)
                dict[w] = y


n, m, edges = getInput()

Prim1(n, m, edges)
Prim2(n, m, edges)
