from deg import get_adjacency_list

def read_data():
    file = open("data.txt", "r")
    lines = file.readlines()
    file.close()

    lines = [list(map(int, line.replace("\n", "").split())) for line in lines]

    num_nodes = lines[0][0]
    num_edges = lines[0][1]
    edges = lines[1:]

    return num_nodes, num_edges, edges

def neighbour_degrees(adjacency_list):
    degrees = []

    for node, neighbours in adjacency_list.items():
        count = 0

        for neighbour in neighbours:
            count += len(adjacency_list[neighbour])

        degrees.append(count)

    return degrees

if __name__ == '__main__':
    num_nodes, num_edges, edges = read_data()

    adj_list = get_adjacency_list(num_nodes, edges)
    degrees = neighbour_degrees(adj_list)

    print(" ".join(list(map(str, degrees))))