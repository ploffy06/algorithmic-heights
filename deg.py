def read_data():
    file = open("data.txt", "r")
    lines = file.readlines()
    file.close()

    lines = [list(map(int, line.replace("\n", "").split())) for line in lines]

    n, m = lines[0][0], lines[0][1]
    edges = lines[1:]

    return n, m, edges

def get_adjacency_list(n, edges):
    adjacency_list = {i+1: [] for i in range(n)}

    for pair in edges:
        v1, v2 = pair[0], pair[1]
        adjacency_list[v1].append(v2)
        adjacency_list[v2].append(v1)

    return adjacency_list

if __name__ == '__main__':
    n, m, edges = read_data()
    adjacency_list = get_adjacency_list(n, edges)
    degrees = [len(neighbours) for v, neighbours in adjacency_list.items()]
    print(" ".join(list(map(str, degrees))))
