def getInput():
    f = open("input.txt", "r")
    continut_fisier = f.read()
    inputList = continut_fisier.split('\n')
    n = int(inputList[0])
    input = inputList[1].split()
    node_values = [int(x) for x in input]
    m = int(inputList[2])
    inputList.pop(0)
    edges = []
    for i in range(2, len(inputList)):
        line = inputList[i]
        input = line.split()
        x, y = int(input[0]), int(input[1])
        edges.append((x, y))
    return n, m, edges, node_values


INF = -1
n, m, edges, node_values = getInput()

# sortare topologica
dependencies = [0 for x in range(n + 1)]
dep_list = [[] for x in range(n + 1)]
for edge in edges:
    x, y = edge
    dep_list[x].append(y)
    dependencies[y] += 1

node_queue = []
time = [INF for x in range(n + 1)]
curr_min = INF
curr_max = -1
# depistare noduri libere
for i in range(1, n + 1):
    if dependencies[i] == 0:
        node_queue.append(i)
        time[i] = 0

# node_queue contine noduri care nu primesc muchii (sunt libere)
while len(node_queue) > 0:
    node = node_queue.pop(0)
    for x in dep_list[node]:  # dep_list[node] contine nodurile catre care "node" trimite muchii
        time[x] = max(time[x],
                      time[node] + node_values[node - 1])  # eliberam nodul "x" si comparam noul timp de completare
        dependencies[x] -= 1
        if dependencies[x] == 0:
            node_queue.append(x)

# resetam vectorul de dependente pentru depistare de activitati critice
for edge in edges:
    x, y = edge
    dependencies[y] += 1
start_dependencies = [x for x in dependencies]

# recreeam node_queue
for i in range(1, n + 1):
    if dependencies[i] == 0:
        node_queue.append(i)
        time[i] = 0

final_time = [time[x] + node_values[x - 1] for x in range(n + 1)] # timpul in care s-a ajuns la "x" + timpul de executare
print(max(final_time))
print("Activitati critice:", end=" ")


# depistare de activitati care intarzie progresul
while len(node_queue) > 0:
    node = node_queue.pop(0)
    node_start_time = time[node]
    node_end_time = time[node] + node_values[node - 1]
    for x in dep_list[node]:
        x_start_time = time[x]
        x_end_time = time[x] + node_values[x - 1]
        dependencies[x] -= 1
        if node_end_time == x_start_time and start_dependencies[x] > 1:
            print(node, end=" ")
        if dependencies[x] == 0:
            node_queue.append(x)

# ultimul nod
for x in range(1, n + 1):
    if time[x] + node_values[x - 1] == max(final_time):
        print(x, end=" ")

print()

for i in range(1, n + 1):
    print(i, ":", time[i], time[i] + node_values[i - 1])
