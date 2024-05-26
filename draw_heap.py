import uuid

import networkx as nx
import matplotlib.pyplot as plt


def draw_heap(heap):
    graph = nx.DiGraph()
    pos = {}
    level = 0
    index = 0

    # Додавання кореня
    root_id = str(uuid.uuid4())
    graph.add_node(root_id, color="skyblue", label=heap[0])
    pos[root_id] = (0, 0)

    # Додавання інших вершин
    for i in range(1, len(heap)):
        if i == 2 ** (level + 1) - 1:
            level += 1
            index = 0

        parent_index = (i - 1) // 2
        parent_id = list(graph.nodes())[parent_index]

        node_id = str(uuid.uuid4())
        graph.add_node(node_id, color="skyblue", label=heap[i])
        pos[node_id] = (pos[parent_id][0] + (-1) ** index * 2 ** (-(level + 1)), -level)

        graph.add_edge(parent_id, node_id)

        index += 1

    # Візуалізація купи
    colors = [node[1]['color'] for node in graph.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in graph.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(graph, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

# Приклад бінарної купи
heap = [8, 5, 6, 2, 3, 4, 1]

# Відображення купи
draw_heap(heap)
