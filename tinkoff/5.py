def build_graph(city_amount, roads):
    graph = {(i + 1): [] for i in range(city_amount)}

    for v, u, w in roads:
        graph[v].append((u, w))
        graph[u].append((v, w))

    return graph


def find_connected_components(graph):
    def dfs(node, component):
        visited[node] = True
        component.append(node)

        for neighbor, _ in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor, component)

    visited = {node: False for node in graph}
    components = []

    for node in graph:
        if not visited[node]:
            component = []
            dfs(node, component)
            components.append(component)

    return components


def find_maximum_removal_weight(graph, amount_of_components):
    def is_ok(graph):
        return len(find_connected_components(graph)) == amount_of_components

    edges = get_all_edges_weights(graph)
    length = 0

    while is_ok(graph) and edges:
        curr_edge = edges.pop()

        for path in graph[curr_edge[0]]:
            if path == curr_edge[1:]:
                graph[curr_edge[0]].remove(curr_edge[1:])
        length = curr_edge[2]

    return length - 1


def get_all_edges_weights(graph):
    tmp = []

    for key, val in graph.items():
        for v in val:
            tmp.append((key, *v))

    tmp.sort(key=lambda x: x[2], reverse=True)

    return tmp


def test():
    graph = build_graph(2, [
        [1, 2, 6],
        [2, 1, 9]
    ])
    components_amount = len(find_connected_components(graph))
    result = find_maximum_removal_weight(graph, components_amount)
    assert result == 8

    graph = build_graph(5, [
        [1, 2, 8],
        [2, 3, 6],
        [2, 3, 2],
        [3, 1, 4],
        [5, 4, 1],
        [4, 5, 8]
    ])
    components_amount = len(find_connected_components(graph))
    result = find_maximum_removal_weight(graph, components_amount)
    assert result == 5

    graph = build_graph(8, [
        [1, 2, 10],
        [2, 3, 11],
        [3, 1, 1],
        [1, 3, 1],
        [4, 5, 10],
        [5, 6, 10],
        [6, 4, 1],
        [6, 5, 1],
        [7, 8, 10],
        [8, 7, 1],
    ])
    components_amount = len(find_connected_components(graph))
    result = find_maximum_removal_weight(graph, components_amount)
    assert result == 9

    graph = build_graph(6, [
        [1, 2, 10],
        [2, 1, 1],
        [3, 4, 10],
        [4, 3, 1],
        [5, 6, 10],
        [6, 5, 1],

    ])
    components_amount = len(find_connected_components(graph))
    result = find_maximum_removal_weight(graph, components_amount)
    assert result == 9

    graph = build_graph(6, [
        [1, 2, 10],
        [2, 1, 1],
        [2, 3, 9],
        [3, 2, 1],
        [3, 4, 8],
        [4, 3, 1],
        [4, 5, 7],
        [5, 4, 1],
        [5, 6, 6],
        [6, 5, 1],
    ])
    components_amount = len(find_connected_components(graph))
    result = find_maximum_removal_weight(graph, components_amount)
    assert result == 5

    graph = build_graph(6, [
        [1, 2, 1],
        [2, 1, 1],
        [2, 3, 9],
        [3, 2, 1],
        [3, 4, 8],
        [4, 3, 1],
        [4, 5, 7],
        [5, 4, 1],
        [5, 6, 6],
        [6, 5, 1],
        [1, 3, 10],
        [1, 4, 10],
        [1, 5, 10],
        [1, 6, 10],
        [1, 1, 2],
        [2, 2, 2],
        [3, 3, 2],
        [4, 4, 2],
        [5, 5, 2],
        [6, 6, 2],
    ])
    components_amount = len(find_connected_components(graph))
    result = find_maximum_removal_weight(graph, components_amount)
    assert result == 8, result

    graph = build_graph(6, [
        [1, 2, 1],
        [2, 1, 1],
        [2, 3, 9],
        [3, 2, 1],
        [3, 4, 8],
        [4, 3, 1],
        [4, 5, 7],
        [5, 4, 1],
        [5, 6, 6],
        [6, 5, 1],
        [1, 3, 10],
        [1, 4, 10],
        [1, 5, 10],
        [1, 6, 10],
        [1, 1, 100],
        [2, 2, 100],
        [3, 3, 100],
        [4, 4, 100],
        [5, 5, 100],
        [6, 6, 100],
    ])
    components_amount = len(find_connected_components(graph))
    result = find_maximum_removal_weight(graph, components_amount)
    assert result == 8


test()


def main():
    n, m = tuple(map(int, input().split()))
    arr = [None] * m
    for i in range(m):
        arr[i] = tuple(map(int, input().split()))
    paths = build_graph(n, arr)
    states = find_connected_components(paths)
    print(find_maximum_removal_weight(paths, len(states)))


main()
