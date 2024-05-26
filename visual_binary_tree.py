import uuid
import networkx as nx
import matplotlib.pyplot as plt
from copy import deepcopy


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.color = None
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)
    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


def dfs_traversal(node, colors):
    if node:
        node.color = generate_color(colors)
        colors.append(node.color)
        print("Вузол:", node.val, "Колір:", node.color)
        dfs_traversal(node.left, colors)
        dfs_traversal(node.right, colors)


def bfs_traversal(root, colors):
    queue = [(root, 1)]
    while queue:
        node, level = queue.pop(0)
        if node:
            node.color = generate_color(colors)
            colors.append(node.color)
            print("Вузол:", node.val, "Рівень:", level, "Колір:", node.color)
            queue.append((node.left, level + 1))
            queue.append((node.right, level + 1))


def generate_color(colors, intensity=70):
    r = min(abs(int(0x7F - intensity * (len(colors) + 1))), 0xFF)
    g = min(abs(int(0x1D - intensity * (len(colors) + 1))), 0xFF)
    b = min(abs(int(0x1D + intensity / (len(colors) + 1))), 0xFF)
    # Формуємо рядок з RGB-значеннями
    color = "#{:02X}{:02X}{:02X}".format(r, g, b)
    return color


if __name__ == '__main__':
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right = Node(1)
    root.right.left = Node(3)
    root2 = deepcopy(root)

    # Обхід дерева та збереження кольорів
    colors_dfs = []
    colors_bfs = []

    print("Обхід у глибину (DFS):")
    dfs_traversal(root, colors_dfs)
    print("\nОбхід у ширину (BFS):")
    bfs_traversal(root2, colors_bfs)

    draw_tree(root)
    draw_tree(root2)
