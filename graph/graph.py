from collections import deque


def print_graph(node):
    visited = set()
    queue = deque([node])

    while queue:
        current = queue.popleft()
        if current in visited:
            continue

        visited.add(current)
        print(f"Node {current.val}: {[n.val for n in current.neighbors]}")

        for neighbor in current.neighbors:
            if neighbor not in visited:
                queue.append(neighbor)
