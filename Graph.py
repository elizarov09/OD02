class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node1, node2):
        if node1 not in self.graph:
            self.graph[node1] = []
        if node2 not in self.graph:
            self.graph[node2] = []
        self.graph[node1].append(node2)
        self.graph[node2].append(node1)

# Пример: навигация и карты
graph = Graph()
graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('B', 'D')
graph.add_edge('C', 'D')
graph.add_edge('C', 'E')
graph.add_edge('D', 'E')

# Функция для отображения графа
def display_graph(graph):
    for node, edges in graph.items():
        print(f"{node}: {', '.join(edges)}")

display_graph(graph.graph)
# Вывод:
# A: B, C
# B: A, D
# C: A, D, E
# D: B, C, E
# E: C, D

# Функция поиска кратчайшего пути (алгоритм BFS)
from collections import deque

def bfs_shortest_path(graph, start, goal):
    visited = set()
    queue = deque([[start]])

    if start == goal:
        return [start]

    while queue:
        path = queue.popleft()
        node = path[-1]
        if node not in visited:
            neighbors = graph[node]
            for neighbor in neighbors:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
                if neighbor == goal:
                    return new_path
            visited.add(node)
    return []

# Поиск кратчайшего пути от A до E
path = bfs_shortest_path(graph.graph, 'A', 'E')
print("Кратчайший путь от A до E:", " -> ".join(path))
# Вывод:
# Кратчайший путь от A до E: A -> C -> E
